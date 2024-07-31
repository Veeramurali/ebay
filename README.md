eBay Automation 

This project uses Selenium to automate the process of navigating and applying filters on eBay's website. The script performs the following tasks:
1. Opens eBay's homepage.
2. Navigates through the categories to "Cell Phones & Smartphones".
3. Applies specific filters for screen size, price, and item location.

 Prerequisites

To run this script, you need the following:

- Python 3.x installed on your machine.
- Google Chrome browser installed.
- ChromeDriver compatible with your version of Chrome browser.
- Selenium package installed in Python.

 Installation

1. Install Python: Download and install Python from [python.org](https://www.python.org/).

2. Install Selenium: Open your terminal or command prompt and run:
  
   pip install selenium
  

3. Download ChromeDriver: Download the ChromeDriver executable from [ChromeDriver](https://sites.google.com/chromium.org/driver/downloads) and ensure it's in your system's PATH or place it in the same directory as your script.

 Running the Script

1. Set Up the Chrome Driver: Ensure you have ChromeDriver installed and its path correctly set up.

2. Run the Script:
  
   python main.py


 Script Overview

The script performs the following steps:

1. Setting up the Chrome Driver.
2. Opening eBay's Homepage.
3. Navigating to Categories.
4. Navigating to Electronics.
5. Navigating to Cell Phones, Smart Watches & Accessories.
6. Navigating to Cell Phones & Smartphones.
7. Scrolling Down to "All Filters".
8. Clicking "All Filters".
9. Applying Screen Size Filter.
10. Applying Price Filter.
11. Applying Item Location Filter.
12. Applying All Filters.
13. Checking If Filters Have Been Applied.
14. Closing the Chrome Driver.

 Notes

- Make sure to adjust the sleep times and WebDriverWait durations according to your internet speed and website's response time.
- If the script fails to locate an element, verify the XPath or other locators, as eBay's web structure may change.
