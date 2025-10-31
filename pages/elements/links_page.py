from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LinksPage(BasePage):
    LINKS_PAGE_URL = "https://demoqa.com/links"
    LINKS_PAGE_TITLE = (By.XPATH, "//h1[normalize-space()='Links']")

    LINKS_PAGE_TEXT_1 = (By.XPATH, "//strong[normalize-space()='Following links will open new tab']")

    HOME_LINK = (By.ID, "simpleLink")
    HOMES_DYNAMIC_LINK = (By.ID, "dynamicLink")

    LINKS_PAGE_TEXT_2 = (By.XPATH, "//strong[normalize-space()='Following links will send an api call']")

    CREATED_LINK = (By.ID, "created")
    NO_CONTENT_LINK = (By.ID, "no-content")
    MOVED_LINK = (By.ID, "moved")
    BAD_REQUEST_LINK = (By.ID, "bad-request")
    UNAUTHORIZED_LINK = (By.ID, "unauthorized")
    FORBIDDEN_LINK = (By.ID, "forbidden")
    NOT_FOUND_LINK = (By.ID, "invalid-url")

    LINK_MESSAGE = (By.ID, "linkResponse")

    def open_links_page(self):
        self.driver.get(self.LINKS_PAGE_URL)

    def is_links_page_title_displayed(self):
        assert self.is_element_visible(self.LINKS_PAGE_TITLE), f"❌ The Links page title is not displayed."
        print(f"\n✅ Links page is displayed: [{self.get_text(self.LINKS_PAGE_TITLE)}.]")
        return True

    def is_links_page_text_1_displayed(self):
        assert self.is_element_visible(self.LINKS_PAGE_TEXT_1), f"❌ The First section's text is not displayed in Links page."
        print(f"✅ The First section's text in Links page is displayed: [{self.get_text(self.LINKS_PAGE_TEXT_1)}].")
        return True

    def is_links_page_text_2_displayed(self):
        assert self.is_element_visible(self.LINKS_PAGE_TEXT_2), f"❌ The Second section's text is not displayed in Links page."
        print(f"✅ The Second section's text in Links page is displayed: [{self.get_text(self.LINKS_PAGE_TEXT_2)}].")
        return True

    #verify if links exists in the Links page
    def is_link_exists(self, locator):
        self.scroll_to_element(locator)
        assert self.is_element_visible(locator), f"❌ Link is not displayed"
        print(f"✅ The [{self.get_text(locator)}] link is visible.\n")
        return True

    #verify clicking on links open a new tab
    def is_new_tab_opened_after_click(self, locator, expected_url):
        old_tabs = self.driver.window_handles
        self.scroll_to_element(locator)
        self.click(locator)
        new_tab = self.is_new_tab_opened(old_tabs)

        self.driver.switch_to.window(new_tab)


        assert self.is_url_contains(expected_url), f"❌ Incorrect link opened"
        print(f"✅ New tab opened correctly with URL containing [{expected_url}]\n")

        self.driver.close()
        self.driver.switch_to.window(old_tabs[0])




    #verify clicking links send an API call
    def is_API_link_clicked(self, locator, expected_text):
        self.scroll_to_element(locator)
        self.click(locator)

        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.LINK_MESSAGE))
        actual_message = self.get_text(self.LINK_MESSAGE)

        assert expected_text in actual_message, f"❌ The success message is wrong after clicking link."
        print(f"✅ After clicking the [{self.get_text(locator)}], the success message is [{actual_message}]\n")
        return True

