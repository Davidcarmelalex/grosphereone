from fastapi import FastAPI
from pydantic import BaseModel

from agents.workflow_agent import run_workflow

app = FastAPI(title="GrossphereOne API")


class WorkflowRequest(BaseModel):
    name: str
    data: dict = {}


@app.get("/")
def root():
    return {"platform": "GrossphereOne"}


@app.post("/workflows/run")
def workflows_run(req: WorkflowRequest):
    return run_workflow(req.name, req.data)
