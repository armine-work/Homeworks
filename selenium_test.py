# 1. Set up Selenium Webdriver
from selenium import webdriver
import time

# 2. Open Firefox browser and
driver = webdriver.Firefox()

# 10. Do all with Chrome and Edge browsers
# driver = webdriver.Chrome()
# driver = webdriver.Edge()

try:
# 2.1. Navigate to https://www.armstqb.org/
    driver.get("https://www.armstqb.org/")
    first_tab_handle = driver.current_window_handle # Store the handle of the first tab
    time.sleep(2)

# 3. Maximize the browser
    driver.maximize_window()
    time.sleep(2)

# 4. Verify the title
    title = driver.title
    print("Title: ", title)
    assert title in "ArmSTQB"
    print(" ✅ Test Passed, current title is: ", title)

# 5. Create a new tab and navigate to https://www.armstqb.org/partners
    driver.switch_to.new_window('tab')
    driver.get("https://www.armstqb.org/partners")
    second_tab_handle = driver.current_window_handle  # Store the handle of the second tab
    time.sleep(2)

# 6. Verify the url
    url = driver.current_url
    assert url in "https://www.armstqb.org/partners"
    print(" ✅ Test Passed, current url is: ", url)

# 7. Close the tab
    driver.close()
    time.sleep(2)

# 8. Minimize the window
    driver.switch_to.window(first_tab_handle)
    driver.minimize_window()
    time.sleep(2)

# 9. Close the session
finally:
    driver.quit()

