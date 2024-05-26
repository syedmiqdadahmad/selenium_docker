from telnetlib import EC
from selenium.webdriver.support import expected_conditions as EC

from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
import time
from icecream import ic
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options

driver = webdriver.Chrome('/Users/syedmiqdadnahmad/Downloads/chromedriver-mac-arm64/chromedriver')
driver.get('https://rahulshettyacademy.com/seleniumPractise/#/')

driver.implicitly_wait(5)

ic(driver.title)
ic(driver.current_url)

driver.find_element(By.CSS_SELECTOR, '.search-keyword').send_keys('ber')
time.sleep(2)
items = driver.find_elements(By.XPATH, "//div[@class='products']/div")
count = len(items)
print(count)

assert count > 0

for item in items:
    item.find_element(By.XPATH, "div/button").click()

driver.find_element(By.CSS_SELECTOR, "img[alt='Cart']").click()
driver.find_element(By.XPATH, "//button[text()='PROCEED TO CHECKOUT']").click()
# driver.find_element(By.CSS_SELECTOR, ".promoCode").send_keys("rahulshettyacademy")


# driver.find_element(By.XPATH, "//input[@class='promoCode']").send_keys("rahulshettyacademy")


# driver.find_element(By.XPATH, '//*[@id="root"]/div/div/div/div/div/input').send_keys("rahulshettyacademy")
driver.find_element(By.CSS_SELECTOR, '.promoCode').send_keys("rahulshettyacademy")
driver.find_element(By.XPATH, "//*[@id='root']/div/div/div/div/div/button").click()
wait = WebDriverWait(driver, 10)
#wait.until(unexpected_condition.presence_of_element_located((By.CSS_SELECTOR, ".promoInfo")))
wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".promoInfo")))

code_applied = (driver.find_element(By.CSS_SELECTOR, ".promoInfo").text)

assert 'Code applied ..!' in code_applied

if 'Code applied ..!' in code_applied:
    print("passed")
else:
    print("failed")



time.sleep(3)

driver.close()
