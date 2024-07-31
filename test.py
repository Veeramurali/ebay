from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pandas as pd

# Set up the driver
driver = webdriver.Chrome()

# Open eBay
driver.get("https://www.ebay.com/")
print(driver.title)

driver.maximize_window()

# Navigate to the categories menu
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "gh-shop-ei"))).click()

# Navigate to Electronics
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, "Electronics"))).click()

# Navigate to Cell Phones, Smart Watches & Accessories
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, "Cell Phones, Smart Watches & Accessories"))).click()

# Navigate to Cell Phones & Smartphones
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, "Cell Phones & Smartphones"))).click()

# Scroll down to the specific element
all_listing = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "srp-format-tabs-h2")))
driver.execute_script("arguments[0].scrollIntoView();", all_listing)

# Navigate to "All filters"
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html[1]/body[1]/div[4]/div[4]/div[3]/section[2]/section[1]/ul[1]/li[9]/button[1]"))).click()

# Apply Screen Size filter
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[normalize-space()='Screen Size']"))).click()

# Provide specific screen size input
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[@id='c3-subPanel-Screen%20Size_4.0%20-%204.4%20in_cbx']"))).click()

# Apply Price filter
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html[1]/body[1]/div[14]/div[2]/div[1]/form[1]/div[1]/div[1]/div[1]/div[23]"))).click()

# Provide specific price input
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "(//input[@type='text'])[2]"))).send_keys("50")
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "(//input[@type='text'])[3]"))).send_keys("70")
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "(//input[@type='text'])[3]"))).click()

# Apply Item Location filter
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[normalize-space()='Item Location']"))).click()

# Provide specific item location input
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[@value='US Only']"))).click()

# Apply all filters
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "(//button[normalize-space()='Apply'])[1]"))).click()

# Extract product details
products = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.XPATH, "//li[@class='s-item']")))
product_list = []

for product in products:
    try:
        title = product.find_element(By.XPATH, ".//h3[@class='s-item__title']").text
    except:
        title = "N/A"
    try:
        price = product.find_element(By.XPATH, ".//span[@class='s-item__price']").text
    except:
        price = "N/A"
    try:
        link = product.find_element(By.XPATH, ".//a[@class='s-item__link']").get_attribute("href")
    except:
        link = "N/A"
    product_list.append({"Title": title, "Price": price, "Link": link})

# Save to Excel in the specified project folder
output_file_path = r"C:\Users\VEERAMURALI T\OneDrive\Desktop\Selenium\Ebay_Automation\ebay_automation\ebay_products.xlsx"
df = pd.DataFrame(product_list)
df.to_excel(output_file_path, index=False)

print(f"Data saved to {output_file_path}")

# Close the driver
driver.quit()
