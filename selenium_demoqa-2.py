from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Firefox()

try:
    # 1. Go to Text Box page → https://demoqa.com/text-box
    # Find the element of Full name field.
    # Using parent::, select its parent <div>.
    # Print the class name of that parent.
    driver.get("https://demoqa.com/text-box")
    driver.maximize_window()
    full_name_element = driver.find_element(By.XPATH, "//input[@placeholder='Full Name']/parent::div")
    class_name = full_name_element.get_attribute("class")
    print(f"✅ The [Full Name] field's parent class name is: {class_name} \n")


    #2. Go to Radio Button page → https://demoqa.com/radio-button
    # Locate radio button Yes.
    # Use following-sibling::label to select its label text.
    # Print the label text (Yes).
    driver.get("https://demoqa.com/radio-button" )
    driver.maximize_window()
    radio_button = driver.find_element(By.XPATH, "//input[@id='yesRadio']/following-sibling::label")
    radio_button_label = radio_button.text
    print(f"✅ The [Yes] radio button's label is: {radio_button_label} \n")


    # 3. Go to Check Box page → https://demoqa.com/checkbox
    # Find the element with text Home. Use following::span to get all nodes after it.
    # Print the count of the following span elements.
    driver.get("https://demoqa.com/checkbox")
    driver.maximize_window()
    checkbox_arrow = driver.find_element(By.XPATH, "//button[@title='Expand all']")
    checkbox_arrow.click()

    checkbox_element_nodes = driver.find_elements(By.XPATH, "//span[@class='rct-title']")
    checkbox_element__nodes_count = len(checkbox_element_nodes)
    print(f"✅ The checkbox's count after expanding [Home] is: {checkbox_element__nodes_count} \n")

except Exception as e:
    print(e)
finally:
    driver.quit()