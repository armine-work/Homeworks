from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class LoginPage(BasePage):
    LOGIN_URL = "https://demoqa.com/login"
    LOGIN_PAGE_TITLE = (By.XPATH, "//h1[normalize-space()='Login']")
    LOGIN_PAGE_TEXT = (By.XPATH, "//h2[normalize-space()='Welcome,']")
    LOGIN_PAGE_TEXT_2 = (By.XPATH, "//h5[normalize-space()='Login in Book Store']")

    USERNAME_TEXT = (By.XPATH, "//label[@id='userName-label']")
    USERNAME_FIELD = (By.ID, "userName")
    #USERNAME_FIELD = (By.XPATH, "//input[@id='userName']")
    PASSWORD_TEXT = (By.XPATH, "//label[@id='password-label']")
    PASSWORD_FIELD = (By.ID, "password")
    #PASSWORD_FIELD = (By.ID, "/input[@id='password']")

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

    def is_login_button_displayed(self):
        return self.is_element_visible(self.LOGIN_BUTTON)

    def is_new_user_button_displayed(self):
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


class RegisterPage(BasePage):

    REGISTER_PAGE_TITLE = (By.XPATH, "//h1[normalize-space()='Register']")
    REGISTER_PAGE_TEXT = (By.XPATH, "//h4[normalize-space()='Register to Book Store']")

    FIRST_NAME_TEXT = (By.XPATH, "//label[@id='firstname-label']")
    #FIRST_NAME_FIELD = (By.XPATH, "//input[@id='firstName']")
    FIRST_NAME_FIELD = (By.ID, "firstname")
    LAST_NAME_TEXT = (By.XPATH, "//label[@id='lastname-label']")
    #LAST_NAME_FIELD = (By.XPATH, "//input[@id='lastName']")
    LAST_NAME_FIELD = (By.ID, "lastname")


    REGISTER_BUTTON = (By.ID, "register")
    BACK_TO_LOGIN_BUTTON = (By.ID, "gotologin")

    CAPTCHA_TEXT = (By.XPATH, "//label[@id='recaptcha-anchor-label']")
    CAPTCHA_CHECKBOX = (By.ID, "//div[@class='recaptcha-checkbox-border']")


    def is_register_title_displayed(self):
        assert self.is_element_visible(RegisterPage.REGISTER_PAGE_TITLE), "❌ Register page title was not displayed"
        return True

    def is_register_page_text_displayed(self):
        assert self.is_element_visible(RegisterPage.REGISTER_PAGE_TEXT), f"❌ Register page text is not displayed"
        return True

    def is_firstName_text_displayed(self):
        assert self.is_element_visible(RegisterPage.FIRST_NAME_TEXT), f"❌ First name text is not displayed"
        return True

    def is_firstName_field_displayed(self):
        assert self.is_element_visible(RegisterPage.FIRST_NAME_FIELD), f"❌ First name field is not displayed"
        return True

    def is_lastName_text_displayed(self):
        assert self.is_element_visible(RegisterPage.LAST_NAME_TEXT), f"❌ Last name text is not displayed"
        return True

    def is_lastName_field_displayed(self):
        assert self.is_element_visible(RegisterPage.LAST_NAME_FIELD), f"❌ Last name field is not displayed"
        return True

    def is_register_button_displayed(self):
        assert self.is_element_visible(RegisterPage.REGISTER_BUTTON), f"❌ Register button was not loaded"
        return True

    def is_back_to_login_button_displayed(self):
        assert self.is_element_visible(RegisterPage.BACK_TO_LOGIN_BUTTON), f"❌ Back to login button was not loaded"
        return True

    # def is_captcha_text_displayed(self):
    #     assert self.is_element_visible(RegisterPage.CAPTCHA_TEXT), f"❌ Captcha text was not displayed"
    #     return True

    def is_captcha_text_displayed(self):
        assert self.is_element_visible(RegisterPage.CAPTCHA_TEXT), f"❌ Captcha text was not displayed"
        return True


    def is_captcha_checkbox_displayed(self):
        assert self.is_element_visible(RegisterPage.CAPTCHA_CHECKBOX), f"❌ Captcha checkbox was not displayed"
        return True

    # def is_register_error_displayed(self):
    #     assert self.is_element_visible(RegisterPage.error), f"❌ Register error was not displayed"
    #     return True


