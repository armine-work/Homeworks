from selenium import webdriver
from selenium.common import ElementNotVisibleException, NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.edge.options import Options as EdgeOptions

## Use Options class for each browser.
## Add at least 3 arguments (--headless, --start-maximized, --incognito).
## options.add_argument("user-data-dir=PATH_TO_PROFILE")
## options.add_argument("profile-directory=Profile 2")

################################################ Chrome options
chrome_options = ChromeOptions()
#chrome_options.add_argument("--headless")
chrome_options.add_argument("--start-maximized")
chrome_options.add_argument("--incognito")

############################################## Firefox options
firefox_options = FirefoxOptions()
#firefox_options.add_argument("--headless")
firefox_options.add_argument("--start-maximized")
firefox_options.add_argument("--disable-extensions")

edge_options = EdgeOptions()
#edge_options.add_argument("--headless")
edge_options.add_argument("--start-maximized")
edge_options.add_argument("--incognito")
###################################################### get browser
def get_driver(browser="firefox"):
    if browser == "firefox":
        return webdriver.Firefox(options=firefox_options)
    elif browser == "chrome":
        return webdriver.Chrome(options=chrome_options)
    elif browser == "edge":
        return webdriver.Edge()
    else:
        raise ValueError("browser must be 'firefox' or 'chrome' or 'edge'")

try:
    driver = get_driver("edge")
    ## 1.Open https://demoqa.com/dynamic-properties.
    ## Set implicit wait = 10 seconds.
    ## Try to click on the button with ID enableAfter.
    ## Observe and explain the behavior in comments.

    print("Exersice 1.\U0001F6A9 \n")
    driver.implicitly_wait(20)
    driver.get("https://demoqa.com/dynamic-properties")
    button = driver.find_element(By.ID, "enableAfter")
    if button.is_enabled():
        button.click()
        print(f"Passed, button was clicked: {button.text}")
    else:
        print(f"Failed, button wasn't clicked: [{button.text}]")
        print("COMMENT: The implicitly_wait doesn't work here as the 'Visible After 5 second' button is not visible in the DOM")
    print("Exersice 1 done! ✅ \n")
########################################################################################################################

    print("Exersice 2.\U0001F6A9 \n")
    ## 2. Open https://the-internet.herokuapp.com/dynamic_loading/1.
    ## Click “Start”.Wait until the text “Hello World!” is visible.
    ## Print “Dynamic content loaded successfully.”

    driver.get("https://the-internet.herokuapp.com/dynamic_loading/1")
    start_button = driver.find_element(By.XPATH, "//button[normalize-space()='Start']")
    # print("start button is found", start_button.text)
    start_button.click()
    wait = WebDriverWait(driver, 10)
    dynamic_text = wait.until(EC.visibility_of_element_located((By.XPATH, "//h4[normalize-space()='Hello World!']")))
    print("“Dynamic content loaded successfully.”")
    print(f"dynamic text is: [{dynamic_text.text}]")
    print("Exersice 2 done! ✅ \n")
########################################################################################################################

    print("Exersice 3.\U0001F6A9 \n")
    ## 3. Open https://the-internet.herokuapp.com/javascript_alerts.
    ## Click the “Click for JS Alert” button.
    ## Wait for the alert and accept it.
    ## Print its text before closing.

    driver.get("https://the-internet.herokuapp.com/javascript_alerts")
    alert_button = driver.find_element(By.XPATH, "//button[normalize-space()='Click for JS Alert']")
    alert_button.click()
    alert_button =driver.switch_to.alert
    print(f"The text in alert is: [{alert_button.text}]")
    alert_button.accept()
    driver.switch_to.default_content()
    print("Exersice 3 done! ✅ \n")

########################################################################################################################
    print("Exersice 4.\U0001F6A9 \n")
    ##4. Open https://demoqa.com/automation-practice-form.
    ##Try to find a non-existing element ID (like "ghostButton").
    ##Catch the exception and print
    driver.get("https://demoqa.com/automation-practice-form")
    non_existing_element = driver.find_element(By.ID, 'ghostButton')
    print(f"The non-existing element is found: [{non_existing_element.text}] ")

except NoSuchElementException as e:
    print("ELEMENT IS NOT FOUND", e)
    print("Exersice 4 done! ✅ \n")


except Exception as e:
    print(f"Exception raised: {e}")

finally:
    driver.quit()