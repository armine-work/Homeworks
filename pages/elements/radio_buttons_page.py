from time import sleep

from selenium.webdriver.common.by import By

from pages.base_page import BasePage

class RadioButtonsPage(BasePage):
    RADIOBUTTON_PAGE_URL = "https://demoqa.com/radio-button"
    RADIOBUTTON_PAGE_TITLE = (By.XPATH, "//h1[normalize-space()='Radio Button']")
    RADIOBUTTON_PAGE_TEXT = (By.XPATH, "//div[normalize-space()='Do you like the site?']")
    YES_RB = (By.XPATH, "//label[text()='Yes']")
    #YES_RB = (By.ID, "yesRadio")
    IMPRESSIVE_RB = (By.XPATH, "//label[text()='Impressive']")
    #IMPRESSIVE_RB = (By.ID, "impressiveRadio")
    NO_RB= (By.XPATH, "//label[normalize-space()='No']")
    #NO_RB = (By.ID, "noRadio")
    SUCCESS_MESSAGE = (By.XPATH, "//p[@class='mt-3']")
    SUCCESS_MESSAGE_2 = (By.XPATH, "//span[@class='text-success']")

    def open_radio_buttons_page(self):
        driver = self.driver.get(self.RADIOBUTTON_PAGE_URL)

    def is_radiobutton_page_displayed(self):
        assert self.is_element_visible(self.RADIOBUTTON_PAGE_TITLE), f"❌ The Radio Button page is not displayed"
        print(f"\n✅ The Radio Button page is displayed: [{self.get_text(self.RADIOBUTTON_PAGE_TITLE)}]")

    def is_radiobutton_text_displayed(self):
        assert self.is_element_visible(self.RADIOBUTTON_PAGE_TEXT), f"❌ The text is not displayed in Radio Button page "
        print(f"✅ The Radio Button text is displayed: [{self.get_text(self.RADIOBUTTON_PAGE_TEXT)}]")

    def is_Yes_radiobutton_displayed(self):
        assert self.is_element_present(self.YES_RB), f"❌ The 'Yes' radio button is not displayed in Radio Button page "
        print(f"✅ The 'Yes' Radio Button is displayed: [{self.get_text(self.YES_RB)}]")

    def is_Impressive_radiobutton_displayed(self):
        assert self.is_element_present(self.IMPRESSIVE_RB), f"❌ The 'Impressive' radio button is not displayed in Radio Button page "
        print(f"✅ The 'Impressive' Radio Button is displayed: [{self.get_text(self.IMPRESSIVE_RB)}]")

    def is_No_radiobutton_displayed(self):
        assert self.is_element_present(self.NO_RB), f"❌ The 'No' radio button is not displayed in Radio Button page "
        print(f"✅ The 'No' Radio Button is displayed: [{self.get_text_of_disabled_element(self.NO_RB)}]\n")

    #functions testing the selections of radio-buttons
    def is_Yes_radiobutton_clicked(self):
        self.scroll_to_element(self.YES_RB)
        self.click(self.YES_RB)
        sleep(5)
        assert "Yes" in self.get_text(self.SUCCESS_MESSAGE_2), f"The success message was not displayed in Radio Button page"
        #assert self.get_text(self.YES_RB) == self.get_text(self.SUCCESS_MESSAGE), f"The success message was not displayed in Radio Button page"
        print(f"\n✅ After selecting 'Yes' radio-button, the message is displayed:"
              f" [{self.get_text(self.SUCCESS_MESSAGE)}]")

    def is_Impressive_radiobutton_clicked(self):
        self.scroll_to_element(self.IMPRESSIVE_RB)
        self.click(self.IMPRESSIVE_RB)
        assert "Impressive" in self.get_text(self.SUCCESS_MESSAGE_2), f"The success message was not displayed in Radio Button page"
        #assert self.IMPRESSIVE_RB == self.SUCCESS_MESSAGE_2, f"The success message was not displayed in Radio Button page"
        print(f"✅ After selecting 'Impressive' radio-button, the message is displayed:"
              f" [{self.get_text(self.SUCCESS_MESSAGE)}]\n")
