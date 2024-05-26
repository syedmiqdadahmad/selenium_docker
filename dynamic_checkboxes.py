from icecream import ic
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


driver = webdriver.Chrome("/Users/syedmiqdadnahmad/Downloads/chromedriver-mac-arm64/chromedriver")
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
ic(driver.title)
ic(driver.current_url)

# handling checkboxes dynamically

checkboxes = driver.find_elements(By.XPATH, "//input[@type='checkbox']")
ic(len(checkboxes))
for checkbox in checkboxes:
    if checkbox.get_attribute("value") == "option2":
        checkbox.click()
        assert checkbox.is_selected()
        break


# handling radio buttons dynamically

radio_btns = driver.find_elements(By.XPATH, "//input[@type='radio']")
ic(len(radio_btns))

for radio_btn in radio_btns:
    if radio_btn.get_attribute("value") == "radio3":
        radio_btn.click()
        assert radio_btn.is_selected()
        break













time.sleep(2)
#driver.close()

