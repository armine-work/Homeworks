from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class LoginPage(BasePage):
    LOGIN_URL = "https://demoqa.com/login"
    LOGIN_PAGE_TITLE = (By.XPATH, "//h1[normalize-space()='Login']")
    LOGIN_PAGE_TEXT = (By.XPATH, "//h2[normalize-space()='Welcome,']")
    LOGIN_PAGE_TEXT_2 = (By.XPATH, "//h5[normalize-space()='Login in Book Store']")
    USERNAME_TEXT = (By.XPATH, "//label[@id='userName-label']")
    USERNAME_FIELD = (By.ID, "userName")
    PASSWORD_TEXT = (By.XPATH, "//label[@id='password-label']")
    PASSWORD_FIELD = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login")
    NEW_USER_BUTTON = (By.ID, "newUser")
    ERROR_MESSAGE = (By.XPATH, "//p[@id='name']")

    LOGOUT_BUTTON = (By.XPATH, "//button[normalize-space()='Log out']")


    def open_login_page(self):
        self.open(self.LOGIN_URL)

    def is_login_title_displayed(self):
        assert self.is_element_visible(LoginPage.LOGIN_PAGE_TITLE), "❌ Login page title was not displayed"
        return True

    def is_login_page_text_displayed(self):
        assert self.is_element_visible(LoginPage.LOGIN_PAGE_TEXT), f"❌ Login page text is not displayed"
        assert self.is_element_visible(LoginPage.LOGIN_PAGE_TEXT_2), f"❌ Login page text 2 is not displayed"
        return True

    def is_username_text_displayed(self):
        assert self.is_element_visible(LoginPage.USERNAME_TEXT), f"❌ Username text is not displayed"
        return True

    def is_username_field_displayed(self):
        assert self.is_element_visible(LoginPage.USERNAME_FIELD), f"❌ Username field is not displayed"
        return True

    def is_password_text_displayed(self):
        assert self.is_element_visible(LoginPage.PASSWORD_TEXT), f"❌ Password text is not displayed"
        return True

    def is_password_field_displayed(self):
        assert self.is_element_visible(LoginPage.PASSWORD_FIELD), f"❌ Password field is not displayed"
        return True

    def is_login_button_loaded(self):
        return self.is_element_visible(self.LOGIN_BUTTON)

    def is_new_user_button_loaded(self):
        return self.is_element_visible(self.NEW_USER_BUTTON)

    def login(self, username, password):
        self.type_text(self.USERNAME_FIELD, username)
        self.type_text(self.PASSWORD_FIELD, password)
        self.scroll_to_element(self.LOGIN_BUTTON)
        self.click(self.LOGIN_BUTTON)



    def is_login_error_displayed(self):
        return self.is_element_visible(self.ERROR_MESSAGE)

    def get_error_message(self):
        return self.get_text(self.ERROR_MESSAGE)

    def logout(self):
        self.click(self.LOGOUT_BUTTON)

    def is_logout_loaded(self):
        return self.is_element_visible(self.LOGOUT_BUTTON)
    #
    # def is_logout_loaded(self, timeout=5):
    #     try:
    #         WebDriverWait(self.driver, timeout).until(
    #             EC.presence_of_element_located(self.LOGOUT_BUTTON)
    #         )
    #         return True
    #     except TimeoutException:
    #         return False



