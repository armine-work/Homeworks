from selenium import webdriver
from selenium.webdriver.common.by import By
#from selenium.webdriver import ActionChains
import time


driver = webdriver.Firefox()
#driver = webdriver.Chrome()

try:
    # 1. Open demoqa.com
    ####################
    driver.get("https://demoqa.com/elements")
    tab_handler = driver.current_window_handle
    driver.maximize_window()

    # 2. Navigate to Buttons
    ########################
    buttons_screen = driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div/div[1]/div/div/div[1]/div/ul/li[5]/span" )
    #buttons_screen = driver.find_element(By.CLASS_NAME, "text-center")
    buttons_screen.click()
    time.sleep(3)

    # verify correct page is opened
    page_name = driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div/div[2]/div[2]/h1")
    page_name_text = page_name.text
    assert page_name.is_displayed()
    print("Opened page should be [Buttons]")
    print("✅ Passed, page name is: ", page_name_text, "\n" )

    # 3. Click on Click Me
    ######################
    # click_buttons = driver.find_elements(By.CLASS_NAME, "btn btn-primary")
    # for click_button in click_buttons:
    #     click_buttons[2].click()

    click_me_button = driver.find_element(By.XPATH, "//button[text()='Click Me']")
    #### scroll till the element is visible
    # ActionChains(driver).move_to_element(click_me_button).perform()
    driver.execute_script("arguments[0].scrollIntoView();", click_me_button )

    click_me_button.click()
    time.sleep(3)


    # 4. Verify that it is clicked (Click Me)
    #########################################
    verification = driver.find_element(By.ID, "dynamicClickMessage")
    verification_text = verification.text
    assert verification.is_displayed()
    print("The text after clicking 'Click Me' button should be: [You have done a dynamic click]")
    print("✅ Passed, page text is: ", verification_text, "\n")

    # 5. Open a new tab and navigate to https://demoqa.com/radio-button
    ###################################################################
    driver.switch_to.new_window('tab')
    driver.get("https://demoqa.com/radio-button")
    time.sleep(5)

    # 6. Click on Impressive Radio Button
    #####################################
    radio_buttons = driver.find_elements(By.CLASS_NAME, "custom-control-label")

    for radio_button in radio_buttons:
        #ActionChains(driver).move_to_element(radio_button).perform()
        driver.execute_script("arguments[0].scrollIntoView();", radio_button)
        radio_buttons[1].click()
    time.sleep(3)

    # 7. Verify the result
    ######################
    verification = driver.find_element(By.CLASS_NAME, "mt-3") and driver.find_element(By.CLASS_NAME, "text-success")
    verification_text = verification.text
    assert verification.is_displayed()
    print("The text after selecting 'Impressive' radio button should be: [You have selected Impressive]")
    print("✅ Passed, radio button selection text is: ", verification_text, "\n")

    # 8. Close the tab
    ##################
    driver.close()
    driver.switch_to.window(tab_handler)

    # 9. In the first tab, go to Links, find all links and print the texts
    ######################################################################
    driver.get("https://demoqa.com/links")
    time.sleep(5)
    verification = driver.find_element(By.CLASS_NAME, "text-center")
    verification_text = verification.text
    print("Page name should be: [Links]")
    print("✅ Passed, page name is: ", verification_text, "\n")

    link_1 = driver.find_element(By.ID, "simpleLink")
    link_1_name = link_1.text
    assert link_1.is_displayed()
    print("✅ Passed, link [Home] is: ", link_1_name, "\n")

    link_2 = driver.find_element(By.ID, "dynamicLink")
    link_2_name = link_2.text
    assert link_2.is_displayed()
    print("✅ Passed, dynamic link's current name is: ", link_2_name, "\n")

    link_3 = driver.find_element(By.ID, "created")
    link_3_name = link_3.text
    assert link_3.is_displayed()
    print("✅ Passed, link [Created] is: ", link_3_name, "\n")

    link_4 = driver.find_element(By.ID, "no-content")
    link_4_name = link_4.text
    assert link_4.is_displayed()
    print("✅ Passed, link [No-Content] is: ", link_4_name, "\n")

    link_5 = driver.find_element(By.ID, "moved")
    link_5_name = link_5.text
    assert link_5.is_displayed()
    print("✅ Passed, link [Moved] name is: ", link_5_name, "\n")

    link_6 = driver.find_element(By.ID, "bad-request")
    link_6_name = link_6.text
    assert link_6.is_displayed()
    print("✅ Passed, link [Bad Request] is: ", link_6_name, "\n")

    link_7 = driver.find_element(By.ID, "unauthorized")
    link_7_name = link_7.text
    assert link_7.is_displayed()
    print("✅ Passed, link [Unauthorized] is: ", link_7_name, "\n")

    link_8 = driver.find_element(By.ID, "forbidden")
    link_8_name = link_8.text
    assert link_8.is_displayed()
    print("✅ Passed, link [Forbidden] is: ", link_8_name, "\n")

    link_9 = driver.find_element(By.ID, "invalid-url")
    link_9_name = link_9.text
    assert link_9.is_displayed()
    print("✅ Passed, link [Not Found] is: ", link_9_name, "\n")



except Exception as e:
    print("Exception error: ", e)
finally:
    driver.quit()

