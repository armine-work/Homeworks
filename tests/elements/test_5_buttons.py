import pytest

from fixtures.conftest import setup_driver
from pages.elements.buttons_page import ButtonsPage

@pytest.mark.ui
@pytest.mark.regression
def test_buttons_page_elements(setup_driver):
    driver = setup_driver
    buttons_page = ButtonsPage(driver)
    buttons_page.open_buttons_page()

    #verify the Buttons Page is displayed
    buttons_page.is_buttons_page_displayed()
    print(f"\n✅ The buttons page is displayed: [{buttons_page.get_text(buttons_page.BUTTONS_PAGE_TITLE)}].")

    #verify the Double Click Me button is displayed
    buttons_page.is_double_click_me_element_displayed()
    print(f"✅ The Double Click Me button is displayed: [{buttons_page.get_text(buttons_page.DOUBLE_CLICK_ME_BUTTON)}].")

    # verify the Right Click Me button is displayed
    buttons_page.is_right_click_me_element_displayed()
    print(f"✅ The Right Click Me button is displayed: [{buttons_page.get_text(buttons_page.RIGHT_CLICK_ME_BUTTON)}].")

    # verify the Click Me button is displayed
    buttons_page.is_click_me_element_displayed()
    print(f"✅ The Click Me button is displayed: [{buttons_page.get_text(buttons_page.CLICK_ME_BUTTON)}].\n")


@pytest.mark.smoke
@pytest.mark.regression
def test_double_click_me_action(setup_driver):
    driver = setup_driver
    buttons_page = ButtonsPage(driver)
    buttons_page.open_buttons_page()

    buttons_page.is_double_click_me_element_displayed()
    buttons_page.is_double_click_me_clicked()
    print(f"\n✅ The 'Double Click Me' button is clicked and the success message is:"
          f" [{buttons_page.get_text(buttons_page.DOUBLE_CLICK_ME_MESSAGE)}].\n")


@pytest.mark.smoke
@pytest.mark.regression
def test_right_click_me_action(setup_driver):
    driver = setup_driver
    buttons_page = ButtonsPage(driver)
    buttons_page.open_buttons_page()

    buttons_page.is_right_click_me_element_displayed()
    buttons_page.is_right_click_me_clicked()
    print(f"✅ The 'Right Click Me' button is clicked and the success message is:"
          f"[{buttons_page.get_text(buttons_page.RIGHT_CLICK_ME_MESSAGE)}].\n")

@pytest.mark.smoke
@pytest.mark.regression
def test_click_me_action(setup_driver):
    driver = setup_driver
    buttons_page = ButtonsPage(driver)
    buttons_page.open_buttons_page()

    buttons_page.is_click_me_element_displayed()
    buttons_page.is_click_me_clicked()
    print(f"\n✅ The 'Click Me' button is clicked and the success message is:"
          f"[{buttons_page.get_text(buttons_page.CLICK_ME_MESSAGE)}].")

