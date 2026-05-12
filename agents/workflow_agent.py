"""
GrossphereOne Workflow Agent

AI-powered agent that orchestrates workflow execution.
Each workflow is a named sequence of steps that can include
API calls, data transformations, and AI reasoning.
"""
from __future__ import annotations
import logging
from dataclasses import dataclass, field
from typing import Any, Callable
import importlib
import uuid
from datetime import datetime

logger = logging.getLogger("grosphereone.agent")

WORKFLOW_REGISTRY: dict[str, Callable] = {}


def register_workflow(name: str, fn: Callable) -> None:
    WORKFLOW_REGISTRY[name] = fn


@dataclass
class WorkflowExecution:
    id: str = field(default_factory=lambda: str(uuid.uuid4()))
    workflow_name: str = ""
    input_data: dict = field(default_factory=dict)
    status: str = "pending"   # pending | running | completed | failed
    result: dict | None = None
    error: str | None = None
    started_at: datetime | None = None
    completed_at: datetime | None = None


def run_workflow(name: str, data: dict) -> dict:
    """
    Execute a named workflow with the given input data.
    
    Dynamically loads workflow modules from the workflows/ package.
    Returns execution result or error details.
    """
    execution = WorkflowExecution(workflow_name=name, input_data=data)
    execution.started_at = datetime.utcnow()
    execution.status = "running"
    
    logger.info(f"Running workflow: {name} | id={execution.id}")
    
    # Try registry first
    if name in WORKFLOW_REGISTRY:
        fn = WORKFLOW_REGISTRY[name]
    else:
        # Dynamic module load
        try:
            module = importlib.import_module(f"workflows.{name}")
            fn = getattr(module, "run")
        except (ImportError, AttributeError) as e:
            execution.status = "failed"
            execution.error = f"Workflow not found: {name}"
            logger.error(f"Workflow load failed: {e}")
            return {"status": "error", "error": execution.error, "execution_id": execution.id}
    
    try:
        result = fn(data)
        execution.status = "completed"
        execution.result = result
        execution.completed_at = datetime.utcnow()
        duration_ms = int((execution.completed_at - execution.started_at).total_seconds() * 1000)
        logger.info(f"Workflow {name} completed in {duration_ms}ms")
        return {"status": "ok", "result": result, "execution_id": execution.id, "duration_ms": duration_ms}
    except Exception as e:
        execution.status = "failed"
        execution.error = str(e)
        execution.completed_at = datetime.utcnow()
        logger.error(f"Workflow {name} failed: {e}")
        return {"status": "error", "error": str(e), "execution_id": execution.id}
