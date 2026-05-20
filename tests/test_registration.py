import pytest
from pages import RegistrationPage, DashboardPage


@pytest.mark.regression
@pytest.mark.registration
def test_successful_registration(registration_page: RegistrationPage, dashboard_page: DashboardPage):
    registration_page.visit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")
    registration_page.fill_login_form("test@test.com", "username", "password")
    registration_page.click_login_button()
    dashboard_page.check_visible_dashboard_title()
