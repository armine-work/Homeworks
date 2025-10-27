import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common import NoSuchElementException



@pytest.fixture(params=["chrome", "firefox", "edge"])
def setup_driver(request):
    ################################################ Chrome options
    chrome_options = ChromeOptions()
    # chrome_options.add_argument("--headless")
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_argument("--incognito")

    ############################################## Firefox options
    firefox_options = FirefoxOptions()
    # firefox_options.add_argument("--headless")
    firefox_options.add_argument("--width=1920")
    firefox_options.add_argument("--height=1080")
    firefox_options.add_argument("--disable-extensions")
    ############################################## Edge options
    edge_options = EdgeOptions()
    # edge_options.add_argument("--headless")
    edge_options.add_argument("--start-maximized")
    edge_options.add_argument("--incognito")

    browser = request.param
    if browser == "firefox":
        driver = webdriver.Firefox(options=firefox_options)
    elif browser == "chrome":
        driver = webdriver.Chrome(options=chrome_options)
    elif browser == "edge":
        driver = webdriver.Edge(options=edge_options)
    else:
        raise ValueError("browser must be 'firefox' or 'chrome' or 'edge'")

    yield driver

    driver.quit()

@pytest.fixture(autouse=True)
def add_screenshot_on_fail(request, driver):
    yield
    if request.node.rep_call.faild:
        driver.save_screenshot(f"screenshot_{request.node.name}.png")

