from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

import time

#driver
driver = webdriver.Chrome()

#get the desired website
driver. get("https://www.ebay.com/")
print(driver.title)

driver.maximize_window()

# Navigate to category
driver.find_element(By.ID,"gh-shop-ei").click()
time.sleep(5)

# navigate to electronics
driver.find_element(By.LINK_TEXT,"Electronics").click()

# navigate to  cellPhones & accesories
page = driver.find_element(By.LINK_TEXT,"Cell Phones, Smart Watches & Accessories").click()
time.sleep(5)

# operation on cell phone & smartphone in the left hand side
driver.find_element(By.LINK_TEXT,"Cell Phones & Smartphones").click()
time.sleep(5)

# Scroll down to the specific element
all_listing = driver.find_element(By.CLASS_NAME,"srp-format-tabs-h2")
driver.execute_script("arguments[0].scrollIntoView();", all_listing)
time.sleep(5)

# navigate to  "All filter"
driver.find_element(By.XPATH,"/html[1]/body[1]/div[4]/div[4]/div[3]/section[2]/section[1]/ul[1]/li[9]/button[1]").click()
time.sleep(5)


# apply Screen Size filter
driver.find_element(By.XPATH,"//span[normalize-space()='Screen Size']").click()
time.sleep(2)

# providing specifc input
driver.find_element(By.XPATH,"//input[@id='c3-subPanel-Screen%20Size_4.0%20-%204.4%20in_cbx']").click()
time.sleep(5)

# apply price filter
driver.find_element(By.XPATH,"/html[1]/body[1]/div[14]/div[2]/div[1]/form[1]/div[1]/div[1]/div[1]/div[23]").click()
time.sleep(5)

# provide specific input
driver.find_element(By.XPATH,"(//input[@type='text'])[2]").send_keys("50")
time.sleep(5)
driver.find_element(By.XPATH,"(//input[@type='text'])[3]").send_keys("70")
time.sleep(2)
driver.find_element(By.XPATH,"(//input[@type='text'])[3]").click()
time.sleep(5)

# apply item location filter
driver.find_element(By.XPATH,"//span[normalize-space()='Item Location']").click()
time.sleep(5)

# provide specific input
driver.find_element(By.XPATH,"//input[@value='US Only']").click()
time.sleep(5)


# apply all filter
driver.find_element(By.XPATH,"(//button[normalize-space()='Apply'])[1]").click()
time.sleep(5)

# check if specified filter has been applied
Filter = driver.find_element(By.XPATH,"(//span[normalize-space()='3 filters applied'])[1]").click()
time.sleep(5)
frame= driver.find_element(By.XPATH,"(//ul[@class='brm__aspect-list'])[1]").text

if str(frame) != 0:
    print(frame)
else:
    print("Filter not applied")

time.sleep(3)
driver.quit()
