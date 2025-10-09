from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep


driver = webdriver.Chrome()
driver.maximize_window()

try:
    # 1. https://demoqa.com/frames
    #     1. Open the page.
    #     2. Switch into the iframe "frame1".
    #     3. Extract and print the text inside it.
    #     4. Switch back to main page (default_content).
    #     5. Then go to https://demoqa.com/alerts.
    #     6. Trigger the “Click me” button that opens a timed alert.
    #     7. Handle the alert with .accept().
    #
    print("Exercise 1 started...")
    driver.get("https://demoqa.com/frames")
    frame_1 = driver.find_element(By.ID, "frame1")
    # print(f"✅ Frame 1: {frame_1.text} \n")
    driver.switch_to.frame(frame_1)
    #print("1.1, current page URL:", driver.current_url)
    ###### work in iframe
    text_in_frame_1 = driver.find_element(By.ID, "sampleHeading")
    print(f"✅ The text in frame_1 is: {text_in_frame_1.text}")
    driver.switch_to.default_content()
    #print("1:2 current page URL is:", driver.current_url)

    driver.get("https://demoqa.com/alerts")
    button_click_me = driver.find_element(By.ID, "timerAlertButton")
    driver.execute_script("arguments[0].scrollIntoView(true);", button_click_me)
    button_click_me.click()
    sleep(7)
    ###### work in alert
    alert_1 = driver.switch_to.alert
    print(f"✅ Alert 1: {alert_1.text} \n")
    alert_1.accept()

    driver.switch_to.default_content()
    print("Exersice 1 done! \n")

    # 2. https://demoqa.com/browser-windows
    #     1. Open the site.
    #     2. Use driver.switch_to.new_window("tab") to open a new tab.
    #     3. Navigate to https://demoqa.com/alerts in that new tab.
    #     4. Trigger an alert and accept it.
    #     5. Switch back to the original tab.

    print("Exercise 2 started...")
    driver.get("https://demoqa.com/browser-windows")
    handler_main = driver.current_window_handle
    driver.switch_to.new_window("tab")
    driver.get("https://demoqa.com/alerts")
    #print("2:1. current page url is:", driver.current_url)

    button_click = driver.find_element(By.ID, "alertButton").click()
    alert_2 = driver.switch_to.alert
    print(f"✅ Alert 2: {alert_2.text} ")
    alert_2.accept()
    sleep(2)

    driver.switch_to.window(handler_main)
    print("current page is:", driver.title)
    sleep(5)
    print("Exersice 2 done! \n")


    # 3. https://demoqa.com/browser-windows
    #     1. Click the “New Window” button.
    #     2. Switch to the new window.
    #     3. Print the message inside the new window.
    #     4. Switch back to the original window.
    #     5. Print the title of the original window.

    print("Exercise 3 started...")
    driver.get("https://demoqa.com/browser-windows")
    original_window = driver.current_window_handle
    #print("3.1 current page url is:", driver.current_url)
    click_button = driver.find_element(By.ID, "windowButton")
    driver.execute_script("arguments[0].scrollIntoView(true);", click_button)
    click_button.click()
    #print("3.2 current page url is:", driver.current_url)
    # new_window = driver.current_window_handle
    # driver.switch_to.window(new_window)

    all_windows_handles = driver.window_handles
    for window_handle in all_windows_handles:
        if window_handle != original_window:
            driver.switch_to.window(window_handle)
            #print("3.3.0 current page url is:", driver.current_url)
            break
    #print("3.3 current page url is:", driver.current_url)
    text_new_window = driver.find_element(By.XPATH, "//h1[@class='text-center']")
    print(f"✅ The message in a new window is: {text_new_window.text} \n")

    driver.switch_to.window(original_window)
    print(f"The original window title is:{driver.title} \n")
    print("Exersice 3 done! \n")
    print("3.4 current page url is:", driver.current_url)
    #
    # 4. https://demoqa.com/frames
    #     1. Switch to "frame1" → get the text.
    #     2. Switch to "frame2" → get the text.
    #     3. Return to main page and print "Iframe task completed".

    print("Exercise 4 started...")
    driver.get("https://demoqa.com/frames")
    frame_1_4 = driver.find_element(By.ID, "frame1")
    # driver.execute_script("arguments[0].scrollIntoView(true);", frame_1_4)
    # sleep(2)
    driver.switch_to.frame(frame_1_4)
    text_frame_1 = driver.find_element(By.XPATH, "//h1[@id='sampleHeading']").text
    print(f"✅ The message in the frame1 is: {text_frame_1}")
    driver.switch_to.default_content()


    frame_2_4 = driver.find_element(By.ID, "frame2")
    # driver.execute_script("arguments[0].scrollIntoView(true);", frame_2_4)
    # sleep(2)
    driver.switch_to.frame(frame_2_4)
    text_frame_2 = driver.find_element(By.XPATH, "//h1[@id='sampleHeading']").text
    print(f"✅ The message in the frame2 is: {text_frame_2}")

    driver.switch_to.default_content()
    print("Exersice 4 done! \n")


    # 5. https://demoqa.com/alerts
    #     1. Trigger the “Click me” alert → accept it.
    #     2. Trigger the Confirm Box → dismiss it.
    #     3. Trigger the Prompt Box → enter your name and accept.
    #     4. Print the result message from the page.

    print("Exercise 5 started...")
    driver.get("https://demoqa.com/alerts")
    alert_1_5 = driver.find_element(By.ID, "alertButton")
    driver.execute_script("arguments[0].scrollIntoView(true);", alert_1_5)
    alert_1_5.click()
    alert_1_5 = driver.switch_to.alert
    print(f"✅ Alert is: {alert_1_5.text}")
    alert_1_5.accept()
    driver.switch_to.default_content()

    ### click next button
    alert_2_5 = driver.find_element(By.ID, "confirmButton")
    driver.execute_script("arguments[0].scrollIntoView(true);", alert_2_5)
    alert_2_5.click()
    alert_2_5 = driver.switch_to.alert
    print(f"✅ Alert is: {alert_2_5.text}")
    alert_2_5.dismiss()
    driver.switch_to.default_content()


    confirmation = driver.find_element(By.ID, "confirmResult")
    confirmation_text = confirmation.text
    assert confirmation.is_displayed()
    print(f"✅ confirmation text is: {confirmation_text}")

    ### click next button
    alert_3_5 = driver.find_element(By.ID, "promtButton")
    driver.execute_script("arguments[0].scrollIntoView(true);", alert_3_5)
    alert_3_5.click()
    alert_3_5 = driver.switch_to.alert
    print(f"✅ Alert is: {alert_3_5.text}")
    alert_3_5.send_keys("Poghos")
    alert_3_5.accept()
    driver.switch_to.default_content()

    confirmation = driver.find_element(By.ID, "promptResult")
    confirmation_text = confirmation.text
    assert confirmation.is_displayed()
    print(f"✅ confirmation text is: {confirmation_text}")

    print("Exersice 5 done! \n")

except Exception as e:
    print(e)

finally:
    driver.quit()