"""Workflow agent dispatches named platform workflows."""


def run_workflow(name, data):
    if name == "customer_signup":
        from workflows.customer_signup import customer_signup
        return customer_signup(data)
    return {"error": f"unknown workflow: {name}"}
