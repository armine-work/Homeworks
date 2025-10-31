import pytest

from fixtures.conftest import setup_driver
from pages.book_sotre_aplication.login_page import LoginPage

@pytest.mark.ui
@pytest.mark.login
@pytest.mark.regression
def test_login_page_elements(setup_driver):
    # open Login page
    driver = setup_driver
    login_page = LoginPage(driver)
    login_page.open_login_page()

    # verify Login page Title
    login_page.is_login_title_displayed()
    print(f"✅ The Login page title is displayed: [{login_page.get_text(login_page.LOGIN_PAGE_TITLE)}].")

    # verify teh Welcome Text exists in Login Page
    login_page.is_login_page_text_displayed()
    print(f"✅ The Login page text is displayed: "
          f"[{login_page.get_text(login_page.LOGIN_PAGE_TEXT)} {login_page.get_text(login_page.LOGIN_PAGE_TEXT_2)}].")

    # verify the UserName text and field are exist in Login page
    login_page.is_username_text_displayed() and login_page.is_username_field_displayed()
    print(f"✅ The Username text and field are displayed: [{login_page.get_text(login_page.USERNAME_TEXT)}].")

    # verify the Password text and field are exist in Login page
    login_page.is_password_text_displayed() and login_page.is_password_field_displayed()
    print(f"✅ The password text and field are displayed: [{login_page.get_text(login_page.PASSWORD_TEXT)}].")

    # verify the Login Button exists in Login page
    login_page.scroll_to_element(login_page.LOGIN_BUTTON)
    login_page.is_login_button_displayed()
    print(f"✅ The Login button is displayed: [{login_page.get_text(login_page.LOGIN_BUTTON)}].")

    # verify the New User button exists in Login page
    login_page.scroll_to_element(login_page.NEW_USER_BUTTON)
    login_page.is_new_user_button_displayed()
    print(f"✅ The New User button is displayed: [{login_page.get_text(login_page.NEW_USER_BUTTON)}].\n")


