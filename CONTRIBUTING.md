# Contributing to GrossphereOne

## Overview

GrossphereOne is an AI workflow automation platform. Contributions can be new workflow templates, agent enhancements, integration connectors, or platform improvements.

## Workflow

1. Branch from `main`: `git checkout -b feat/workflow/your-workflow`
2. Write code with type hints and docstrings
3. Add tests
4. Open a PR describing the use case and expected behavior

## Adding a Workflow Template

```python
# workflows/your_workflow.py

from dataclasses import dataclass
from typing import Any

@dataclass
class WorkflowResult:
    success: bool
    output: dict[str, Any]
    steps_completed: int

def run(data: dict) -> dict:
    """
    Your workflow — describe what it does.
    
    Input:
        data: dict with required fields
    
    Returns:
        status, result, steps_completed
    """
    # Implementation
    return {"status": "ok", "result": {}, "steps_completed": 1}
```

Register in `workflows/__init__.py`.

## Commit Convention

```
feat(workflow): add invoice processing automation
feat(integration): add Stripe payment connector
fix: resolve async workflow timeout handling
docs: add API usage examples
```
