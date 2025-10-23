import pytest

from fixtures.conftest import setup_driver
from pages.book_sotre_aplication.login_page import LoginPage

@pytest.mark.parametrize("username, password, expected_success", [
    ("test-user", "Abcd1234*", True),
    ("test-user", "Abcd", False),
    ("test", "Abcd1234*", False)
])

def test_login_flow(setup_driver, username, password, expected_success):
    driver = setup_driver
    login_page = LoginPage(driver)
    login_page.open_login_page()

    assert login_page.is_login_loaded(), "Login page was not loaded"

    login_page.login(username, password)
    # login_page.is_element_visible(login_page.LOGOUT_BUTTON)
    login_page.is_logout_loaded()
    print(f"logout button is visible {login_page.LOGOUT_BUTTON}")

    if expected_success:
        assert "profile" in driver.current_url, f"Profile page was not loaded"
        print(f"{username} is logged in")
    else:
        assert login_page.is_login_error_displayed(), f"Error page was not shown for invalid username/password"
        print(f"Error message: {login_page.get_error_message()}")
