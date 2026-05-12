"""
GrossphereOne Workflow Tests
"""
import pytest
from workflows.customer_signup import run


class TestCustomerSignupWorkflow:
    def test_successful_signup(self):
        result = run({"email": "test@example.com", "plan": "starter", "name": "Test User"})
        assert result["steps_completed"] == ["validate_input", "create_account", "send_welcome_email", "provision_resources", "notify_team"]
        assert "user_id" in result
        assert result["email"] == "test@example.com"
    
    def test_missing_email_raises(self):
        with pytest.raises(ValueError, match="email is required"):
            run({"plan": "starter"})
    
    def test_invalid_email_raises(self):
        with pytest.raises(ValueError, match="Invalid email"):
            run({"email": "not-an-email", "plan": "starter"})
    
    def test_default_plan_is_starter(self):
        result = run({"email": "test@example.com"})
        assert result["plan"] == "starter"
    
    def test_next_actions_provided(self):
        result = run({"email": "test@example.com"})
        assert len(result["next_actions"]) > 0
