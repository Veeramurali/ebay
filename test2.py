from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Set up the Chrome driver
print("Setting up the Chrome driver...")
driver = webdriver.Chrome()

# Open the eBay website
print("Opening eBay...")
driver.get("https://www.ebay.com/")
print("Page title:", driver.title)
driver.maximize_window()

# Navigate to category
print("Navigating to categories menu...")
driver.find_element(By.ID, "gh-shop-ei").click()
time.sleep(5)

# Navigate to Electronics
print("Navigating to Electronics...")
driver.find_element(By.LINK_TEXT, "Electronics").click()
time.sleep(5)

# Navigate to Cell Phones, Smart Watches & Accessories
print("Navigating to Cell Phones, Smart Watches & Accessories...")
driver.find_element(By.LINK_TEXT, "Cell Phones, Smart Watches & Accessories").click()
time.sleep(5)

# Navigate to Cell Phones & Smartphones
print("Navigating to Cell Phones & Smartphones...")
driver.find_element(By.LINK_TEXT, "Cell Phones & Smartphones").click()
time.sleep(5)

# Scroll down to the specific element
print("Scrolling down to 'All filters'...")
all_listing = driver.find_element(By.CLASS_NAME, "srp-format-tabs-h2")
driver.execute_script("arguments[0].scrollIntoView();", all_listing)
time.sleep(5)

# Navigate to "All filters" using updated approach
print("Navigating to 'All filters'...")
try:
    all_filters_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[@aria-label='All Filters']"))
    )
    print("Found 'All filters' button, clicking...")
    all_filters_button.click()
except Exception as e:
    print("Error navigating to 'All filters':", e)
    driver.quit()
    exit()
time.sleep(5)

# Apply Screen Size filter
print("Applying Screen Size filter...")
driver.find_element(By.XPATH, "//span[normalize-space()='Screen Size']").click()
time.sleep(2)

# Provide specific screen size input
print("Selecting screen size '4.0 - 4.4 in'...")
driver.find_element(By.XPATH, "//input[@id='c3-subPanel-Screen%20Size_4.0%20-%204.4%20in_cbx']").click()
time.sleep(5)

# Apply Price filter using updated approach
print("Applying Price filter...")
try:
    price_filter = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//span[@class='x-overlay-aspect__label' and text()='Price']"))
    )
    print("Found 'Price' filter, clicking...")
    price_filter.click()
except Exception as e:
    print("Error navigating to 'Price' filter:", e)
    driver.quit()
    exit()
time.sleep(5)

# Provide specific price input
print("Setting price range: $50 to $70...")
driver.find_element(By.XPATH, "(//input[@type='text'])[2]").send_keys("50")
time.sleep(5)
driver.find_element(By.XPATH, "(//input[@type='text'])[3]").send_keys("70")
time.sleep(2)
driver.find_element(By.XPATH, "(//input[@type='text'])[3]").click()
time.sleep(5)

# Apply Item Location filter
print("Applying Item Location filter...")
driver.find_element(By.XPATH, "//span[normalize-space()='Item Location']").click()
time.sleep(5)

# Provide specific item location input
print("Selecting item location 'US Only'...")
driver.find_element(By.XPATH, "//input[@value='US Only']").click()
time.sleep(5)

# Apply all filters
print("Applying all filters...")
driver.find_element(By.XPATH, "(//button[normalize-space()='Apply'])[1]").click()
time.sleep(5)

# Check if specified filter has been applied
print("Checking if filters have been applied...")
try:
    filter_text = driver.find_element(By.XPATH, "(//span[normalize-space()='3 filters applied'])[1]").text
    print("Filters applied:", filter_text)
except Exception as e:
    print("Error checking filters:", e)

# Close the driver
print("Closing the Chrome driver...")
time.sleep(3)
driver.quit()
print("Done.")
