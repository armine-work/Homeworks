import pytest

from fixtures.conftest import setup_driver
from pages.book_sotre_aplication.login_page import LoginPage

@pytest.mark.ui
@pytest.mark.registration
@pytest.mark.regression
def test_register_page(setup_driver):
    driver = setup_driver
    login_page = LoginPage(driver)
    login_page.open_login_page()

    #verify clicking New User button
    login_page.scroll_to_element(login_page.NEW_USER_BUTTON)
    login_page.click(login_page.NEW_USER_BUTTON)

    #  verify the Register page elements
    # verify the Register page Title is displayed in Register page
    login_page.is_register_title_displayed()
    print(f"✅ The Register page title is displayed:[{login_page.get_text(login_page.REGISTER_PAGE_TITLE)}].")

    # verify the Register page text is displayed in Register page
    login_page.is_register_page_text_displayed()
    print(f"✅ The Register page text is displayed:[{login_page.get_text(login_page.REGISTER_PAGE_TEXT)}].")


    # verify First Name field and text are displayed in Register page
    login_page.scroll_to_element(login_page.FIRST_NAME_TEXT)
    login_page.is_firstName_text_displayed() and login_page.is_firstName_field_displayed()
    print(f"✅ The First Name text and field are displayed:[{login_page.get_text(login_page.FIRST_NAME_TEXT)}].")

    # verify Last Name field and text are displayed in Register page
    login_page.scroll_to_element(login_page.LAST_NAME_TEXT)
    login_page.is_lastName_text_displayed() and login_page.is_lastName_field_displayed()
    print(f"✅ The Last Name text and field are displayed:[{login_page.get_text(login_page.LAST_NAME_TEXT)}].")

    # verify the UserName text and field are exist in Register page
    login_page.scroll_to_element(login_page.USERNAME_TEXT)
    login_page.is_username_text_displayed() and login_page.is_username_field_displayed()
    print(f"✅ The Username text and field are displayed: [{login_page.get_text(login_page.USERNAME_TEXT)}].")

    # verify the Password text and field are exist in Register page
    login_page.scroll_to_element(login_page.PASSWORD_TEXT)
    login_page.is_password_text_displayed() and login_page.is_password_field_displayed()
    print(f"✅ The password text and field are displayed: [{login_page.get_text(login_page.PASSWORD_TEXT)}].")

    # verify the Register Button exists in Login page
    login_page.scroll_to_element(login_page.REGISTER_BUTTON)
    login_page.is_register_button_displayed()
    print(f"✅ The Register button is displayed: [{login_page.get_text(login_page.REGISTER_BUTTON)}].")


    # verify the New User button exists in Login page
    login_page.scroll_to_element(login_page.BACK_TO_LOGIN_BUTTON)
    login_page.is_back_to_login_button_displayed()
    print(f"✅ The New User button is displayed: [{login_page.get_text(login_page.BACK_TO_LOGIN_BUTTON)}].")


    # #verify the reCapcha is displayed
    # register_page.scroll_to_element(register_page.CAPTCHA_TEXT)
    # register_page.is_captcha_text_displayed() and register_page.is_captcha_checkbox_displayed()
    # print(f" The Capcha is displayed: [{register_page.get_text(register_page.CAPTCHA_TEXT)}]")
