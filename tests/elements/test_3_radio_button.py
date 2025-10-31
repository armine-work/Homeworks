import pytest
from fixtures.conftest import setup_driver
from pages.elements.radio_buttons_page import RadioButtonsPage


@pytest.mark.ui
@pytest.mark.regression
def test_radio_buttons_page_elements(setup_driver):
    driver = setup_driver
    radio_buttons_page = RadioButtonsPage(driver)
    radio_buttons_page.open_radio_buttons_page()

    radio_buttons_page.is_radiobutton_page_displayed()
    radio_buttons_page.is_radiobutton_text_displayed()

    radio_buttons_page.is_Yes_radiobutton_displayed()
    radio_buttons_page.is_Impressive_radiobutton_displayed()
    radio_buttons_page.is_No_radiobutton_displayed()


@pytest.mark.smoke
@pytest.mark.regression
def test_radio_buttons_functionality(setup_driver):
    driver = setup_driver
    radio_buttons_page = RadioButtonsPage(driver)
    radio_buttons_page.open_radio_buttons_page()

    radio_buttons_page.is_Yes_radiobutton_clicked()
    radio_buttons_page.is_Impressive_radiobutton_clicked()
