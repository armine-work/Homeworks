import pytest

from fixtures.conftest import setup_driver
from pages.book_sotre_aplication.login_page import LoginPage


@pytest.mark.parametrize("username, password, expected_success", [
    ("test-user", "Abcd1234*", True),
    ("test-user", "Abcd", False),
    ("test", "Abcd1234*", False)
])

@pytest.mark.login
@pytest.mark.regression
@pytest.mark.smoke
def test_login_flow(setup_driver, username, password, expected_success):
    #open Login page
    driver = setup_driver
    login_page = LoginPage(driver)
    login_page.open_login_page()

    #verify the Login button is visible
    assert login_page.is_login_button_displayed(), "❌ Login page was not loaded"

    # verify Login functionality
    login_page.login(username, password)

    #verify the Logout button is visible after successfully logging in
    if expected_success:
        assert login_page.is_logout_loaded(), f"❌ Profile page was not loaded"
        print(f"✅ {username} is logged in. The logout button is displayed: [{login_page.get_text(LoginPage.LOGOUT_BUTTON)}].\n")
    else:
        assert login_page.is_login_error_displayed(), f" ❌ Error text was not shown for invalid username/password"
        print(f"✅ The Error message is displayed: [{login_page.get_error_message()}].\n")
