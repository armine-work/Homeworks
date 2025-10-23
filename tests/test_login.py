import pytest

from fixtures.conftest import setup_driver
from pages.book_sotre_aplication.login_page import LoginPage


def test_login_page_elements(setup_driver):
    # open Login page
    driver = setup_driver
    login_page = LoginPage(driver)
    login_page.open_login_page()

    # verify Login page Title
    if login_page.is_login_title_displayed():
        print(f"✅ The Login page title is displayed: [{login_page.get_text(login_page.LOGIN_PAGE_TITLE)}]")
    else:
        print("Error")
    # verify teh Welcome Text exists in Login Page
    if login_page.is_login_page_text_displayed():
        print(f"✅ The Login page text is displayed: [{login_page.get_text(login_page.LOGIN_PAGE_TEXT)} {login_page.get_text(login_page.LOGIN_PAGE_TEXT_2)}]")
    else:
        print("Error")
    # verify the UserName text and field are exist in Login page
    if login_page.is_username_text_displayed() and login_page.is_username_field_displayed():
        print(f"✅ The Username text and field are displayed: [{login_page.get_text(login_page.USERNAME_TEXT)}]")
    else:
        print("Error")
    # verify the Password text and field are exist in Login page
    if login_page.is_password_text_displayed() and login_page.is_password_field_displayed():
        print(f"✅ The password text and field are displayed: [{login_page.get_text(login_page.PASSWORD_TEXT)}]")
    else:
        print("Error")
    # verify the Login Button exists in Login page
    login_page.scroll_to_element(login_page.LOGIN_BUTTON)
    if login_page.is_login_button_loaded():
        print(f"✅ The Login button is displayed: [{login_page.get_text(login_page.LOGIN_BUTTON)}]")
    else:
        print("Error")
    # verify the New User button exists in Login page
    login_page.scroll_to_element(login_page.NEW_USER_BUTTON)
    if login_page.is_new_user_button_loaded():
        print(f"✅ The New User button is displayed: [{login_page.get_text(login_page.NEW_USER_BUTTON)}]")
    else:
        print("Error")


@pytest.mark.parametrize("username, password, expected_success", [
    ("test-user", "Abcd1234*", True),
    ("test-user", "Abcd", False),
    ("test", "Abcd1234*", False)
])

def test_login_flow(setup_driver, username, password, expected_success):
    #open Login page
    driver = setup_driver
    login_page = LoginPage(driver)
    login_page.open_login_page()

    #verify the Login button is visible
    assert login_page.is_login_button_loaded(), "❌ Login page was not loaded"
    # verify Login functionality
    login_page.login(username, password)
    #verify the Logout button is visible after successfully logging in

    if expected_success:
        assert login_page.is_logout_loaded(), f"❌ Profile page was not loaded"
        print(f"✅ {username} is logged in. The logout button is displayed: [{login_page.get_text(LoginPage.LOGOUT_BUTTON)}]")
    else:
        assert login_page.is_login_error_displayed(), f" ❌ Error text was not shown for invalid username/password"
        print(f"✅ The Error message is displayed: [{login_page.get_error_message()}]")
