"""
Customer Signup Workflow

Automates the end-to-end customer onboarding process:
1. Validate input data
2. Create user account
3. Send welcome email
4. Provision initial resources
5. Notify internal team
"""
from __future__ import annotations
import logging

logger = logging.getLogger("workflow.customer_signup")


def run(data: dict) -> dict:
    """
    Customer signup automation workflow.
    
    Input:
        email (str): Customer email address
        plan (str): Subscription plan (starter | pro | enterprise)
        name (str, optional): Customer name
        company (str, optional): Company name
    
    Returns:
        status, user_id, steps_completed, next_actions
    """
    email = data.get("email")
    plan = data.get("plan", "starter")
    name = data.get("name", "")
    company = data.get("company", "")
    
    if not email:
        raise ValueError("email is required")
    
    steps_completed = []
    
    # Step 1: Validate
    logger.info(f"[1/5] Validating signup data for {email}")
    if "@" not in email:
        raise ValueError(f"Invalid email: {email}")
    steps_completed.append("validate_input")
    
    # Step 2: Create account (stub — integrate with your auth system)
    logger.info(f"[2/5] Creating account for {email} on {plan} plan")
    user_id = f"usr_{email.split('@')[0]}_{plan[:3]}"
    steps_completed.append("create_account")
    
    # Step 3: Send welcome email (stub — integrate with SMTP/SendGrid)
    logger.info(f"[3/5] Sending welcome email to {email}")
    steps_completed.append("send_welcome_email")
    
    # Step 4: Provision resources
    logger.info(f"[4/5] Provisioning {plan} resources for {user_id}")
    steps_completed.append("provision_resources")
    
    # Step 5: Notify team (stub — integrate with Slack/webhook)
    logger.info(f"[5/5] Notifying team of new signup: {email}")
    steps_completed.append("notify_team")
    
    return {
        "user_id": user_id,
        "email": email,
        "plan": plan,
        "steps_completed": steps_completed,
        "next_actions": ["complete_profile", "verify_email", "explore_dashboard"],
    }
