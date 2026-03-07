"""Example workflow: customer onboarding."""


def create_user_account(data):
    return {"step": "create_user_account", "ok": True, "email": data.get("email")}


def provision_resources(data):
    return {"step": "provision_resources", "ok": True, "plan": data.get("plan", "starter")}


def notify_team(data):
    return {"step": "notify_team", "ok": True, "channel": data.get("notify", "slack")}


def customer_signup(data):
    results = [
        create_user_account(data),
        provision_resources(data),
        notify_team(data),
    ]
    return {"status": "customer onboarding complete", "results": results}
