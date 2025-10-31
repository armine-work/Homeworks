import pytest

from fixtures.conftest import setup_driver
from pages.elements.links_page import LinksPage


@pytest.mark.ui
@pytest.mark.regression
@pytest.mark.links
def test_links_page_element(setup_driver):
    driver = setup_driver
    links_page = LinksPage(driver)
    links_page.open_links_page()

    #verify elements existence in Links page
    links_page.is_links_page_title_displayed()

    links_page.is_links_page_text_1_displayed()
    links_page.is_links_page_text_2_displayed()


@pytest.mark.ui
@pytest.mark.regression
@pytest.mark.links
@pytest.mark.parametrize("link_locator, link_text", [
    ("HOME_LINK", "Home"),
    ("HOMES_DYNAMIC_LINK", "Home ?"),
    ("CREATED_LINK", "Created"),
    ("NO_CONTENT_LINK", "No Content"),
    ("MOVED_LINK", "Moved"),
    ("BAD_REQUEST_LINK", "Bad Request"),
    ("UNAUTHORIZED_LINK", "Unauthorized"),
    ("FORBIDDEN_LINK", "Forbidden" ),
    ("NOT_FOUND_LINK", "Not Found"),
])
def test_links_existence(setup_driver, link_locator, link_text):
    driver = setup_driver
    links_page = LinksPage(driver)
    links_page.open_links_page()

    locator = getattr(links_page, link_locator)
    links_page.is_link_exists(locator)


@pytest.mark.smoke
@pytest.mark.regression
@pytest.mark.links
@pytest.mark.parametrize("link_locator, tab_url", [
    ("HOME_LINK", "demoqa.com"),
    ("HOMES_DYNAMIC_LINK", "demoqa.com")
])
def test_links_open_new_tab(setup_driver, link_locator, tab_url):
    driver = setup_driver
    links_page = LinksPage(driver)
    links_page.open_links_page()
    locator = getattr(links_page, link_locator)
    links_page.is_new_tab_opened_after_click(locator, tab_url)


@pytest.mark.smoke
@pytest.mark.regression
@pytest.mark.links
@pytest.mark.parametrize("link_locator, expected_text",[
    ("CREATED_LINK", "201"),
    ("NO_CONTENT_LINK", "204"),
    ("MOVED_LINK", "301"),
    ("BAD_REQUEST_LINK", "400"),
    ("UNAUTHORIZED_LINK", "401"),
    ("FORBIDDEN_LINK", "403" ),
    ("NOT_FOUND_LINK", "404")
])
def test_links_functionality(setup_driver, link_locator, expected_text):
    driver = setup_driver
    links_page = LinksPage(driver)
    links_page.open_links_page()

    locator = getattr(links_page, link_locator)
    links_page.is_API_link_clicked(locator, expected_text)



