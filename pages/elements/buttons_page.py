from selenium.webdriver.common.by import By

from pages.base_page import BasePage

class ButtonsPage(BasePage):
    BUTTONS_PAGE_URL = "https://demoqa.com/buttons"
    BUTTONS_PAGE_TITLE = (By.CLASS_NAME, "text-center")

    DOUBLE_CLICK_ME_BUTTON = (By.ID, "doubleClickBtn")
    RIGHT_CLICK_ME_BUTTON = (By.ID, "rightClickBtn")
    CLICK_ME_BUTTON = (By.XPATH, "//button[normalize-space()='Click Me']")

    DOUBLE_CLICK_ME_MESSAGE = (By.ID, "doubleClickMessage")
    RIGHT_CLICK_ME_MESSAGE = (By.ID, "rightClickMessage")
    CLICK_ME_MESSAGE = (By.ID, "dynamicClickMessage")

    def open_buttons_page(self):
        self.driver.get(self.BUTTONS_PAGE_URL)

    # functions for testing buttons existence
    def is_buttons_page_displayed(self):
        assert self.is_element_visible(self.BUTTONS_PAGE_TITLE), f"❌ Buttons page title was not displayed."
        return

    def is_double_click_me_element_displayed(self):
        assert self.is_element_visible(self.DOUBLE_CLICK_ME_BUTTON), f"❌ The 'Double Click' Me button is not displayed"
        return True

    def is_right_click_me_element_displayed(self):
        assert self.is_element_visible(self.RIGHT_CLICK_ME_BUTTON), f"❌ The 'Right Click' Me button is not displayed"
        return True

    def is_click_me_element_displayed(self):
        assert self.is_element_visible(self.CLICK_ME_BUTTON), f"❌ The 'Click Me' button is not displayed"
        return True

    #functions for testing results after clicking buttons

    def is_double_click_me_clicked(self):
        self.scroll_to_element(self.DOUBLE_CLICK_ME_BUTTON)
        self.double_click(self.DOUBLE_CLICK_ME_BUTTON)
        assert self.is_element_visible(self.DOUBLE_CLICK_ME_MESSAGE), f"❌ The succeed message of 'Double Click Me' was not displayed"
        return True

    def is_right_click_me_clicked(self):
        self.scroll_to_element(self.RIGHT_CLICK_ME_BUTTON)
        self.right_click(self.RIGHT_CLICK_ME_BUTTON)
        assert self.is_element_visible(self.RIGHT_CLICK_ME_MESSAGE), f"❌ The succeed message of 'Right Click Me' was not displayed"
        return True

    def is_click_me_clicked(self):
        self.scroll_to_element(self.CLICK_ME_BUTTON)
        self.click(self.CLICK_ME_BUTTON)
        assert self.is_element_visible(self.CLICK_ME_MESSAGE), f"❌ The succeed message of 'Click Me' was not displayed"
        return True