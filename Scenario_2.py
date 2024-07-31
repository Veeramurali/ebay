from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

import time

#driver
driver = webdriver.Chrome()

#open url
driver.get("https://www.ebay.com")

driver.maximize_window()

#search bar
search = ("Macbook")
driver.find_element_by_xpath("/html/body/header/table/tbody/tr/td[3]/form/table/tbody/tr/td[1]/div[1]/div/input[1]").send_keys(search)

#drop_down
element = driver.find_element(By.XPATH,"//select[@id='gh-cat']").click()

#select value from drop_down
driver.find_element(By.XPATH,"(//option[@value='58058'])[1]").click()

#click on search bar
driver.find_element(By.XPATH,"//input[@id='gh-btn']").click()

#verify page name
print(driver.title)

#verify first name matches with the search string
# Locate the name of the first search result
first_result_name_element = driver.find_element(By.CSS_SELECTOR, "#item4d8cbf0397 > div > div.s-item__info.clearfix > a > div > span > span")

# Extract the text of the first search result name
first_result_name = first_result_name_element.text

# Compare the extracted name with the search string
if search in first_result_name:
    print(f"The first search result name '{first_result_name}' matches the search string '{search}'.")
else:
    print(f"The first search result name '{first_result_name}' does not match the search string '{search}'.")


time.sleep(5)

# Close the WebDriver
driver.quit()