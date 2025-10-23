from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class LoginPage(BasePage):
    LOGIN_URL = "https://demoqa.com/login"
    USERNAME_FIELD = (By.ID, 'userName')
    PASSWORD_FIELD = (By.ID, 'password')
    LOGIN_BUTTON = (By.ID, 'login')
    LOGOUT_BUTTON = (By.XPATH, "//button[normalize-space()='Log out']")
    ERROR_MESSAGE = (By.XPATH, "//p[@id='name']")


    def open_login_page(self):
        self.open(self.LOGIN_URL)

    def login(self, username, password):
        self.type_text(self.USERNAME_FIELD, username)
        self.type_text(self.PASSWORD_FIELD, password)
        self.scroll_to_element(self.LOGIN_BUTTON)
        self.click(self.LOGIN_BUTTON)

    def is_login_loaded(self):
        return self.is_element_visible(self.LOGIN_BUTTON)

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



