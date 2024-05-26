import time
from icecream import ic
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


driver = webdriver.Chrome('/Users/syedmiqdadnahmad/Downloads/chromedriver-mac-arm64/chromedriver')
driver.get("https://rahulshettyacademy.com/dropdownsPractise/")

ic(driver.title)
ic(driver.current_url)

driver.find_element(By.ID, 'autosuggest').send_keys('ind')
time.sleep(2)

countries = driver.find_elements(By.CSS_SELECTOR, "li[class='ui-menu-item'] a")
ic(len(countries))

for country in countries:
    if country.text == 'India':
        country.click()
        break











time.sleep(2)
driver.close()







