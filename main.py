import time
from icecream import ic
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome('/Users/syedmiqdadnahmad/Downloads/chromedriver-mac-arm64/chromedriver')
driver.get('https://rahulshettyacademy.com/angularpractice/')

print(driver.title)
print(driver.current_url)


# to get element by XPATH: //tagname [@attribute='value']
# to get element by CSS-Selector: tagname [attribute= 'value']


driver.find_element(By.XPATH, "//input [@name='name']").send_keys("mikivirus")
driver.find_element(By.XPATH, "//input [@name='email']").send_keys("testing@virus.com")
driver.find_element(By.ID, "exampleInputPassword1").send_keys("password")
driver.find_element(By.CSS_SELECTOR, "input[type='submit']").click()
driver.find_element(By.XPATH, "//input[@id='exampleCheck1'][1]").click()

message = driver.find_element(By.CLASS_NAME, 'alert-success').text
assert 'Success' in message


# use select class to handle static dropdowns
#pacakage: from selenium.webdriver.support.select import Select
# 3 methods available to handle static dropdowns
# 1> visible text.  2> by index. 3> by value


dropdown = Select(driver.find_element(By.ID, 'exampleFormControlSelect1'))
#dropdown.select_by_visible_text('Female')
dropdown.select_by_index(1)
#dropdown.select_by_value()


#


time.sleep(5)

driver.close()
