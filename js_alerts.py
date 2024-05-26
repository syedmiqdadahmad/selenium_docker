from icecream import ic
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome("/Users/syedmiqdadnahmad/Downloads/chromedriver-mac-arm64/chromedriver")
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
ic(driver.title)
ic(driver.current_url)

driver.find_element(By.ID, "name").send_keys("ahmad")
driver.find_element(By.ID, "alertbtn").click()

alert = driver.switch_to.alert
alert_text = alert.text
assert 'ahmad' in alert_text
ic(alert_text)
alert.accept()

# alert.dismiss() >> used to decline the popups

time.sleep(2)