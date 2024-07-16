from selenium import webdriver
from selenium.webdriver.common.by import By
import time


# URL of the webpage containing the dynamic content
url = 'https://flipp.com/en-us/weekly_ads/groceries?postal_code=77845'

# Initialize WebDriver
driver = webdriver.Chrome()

# Load the page
driver.get(url)
time.sleep(5)  # Adjust sleep time as needed to ensure page fully loads

#Click a-z
driver.find_element(By.XPATH, "//button[@title='Sort circulars alphabetically by store']").click()

#List of hrefs we want
adHREFs = ["aldi-weekly", "heb-weekly","kroger-weekly"]

#get hrefs in the div
hrefs = []
div_container = driver.find_elements(By.CLASS_NAME, 'flyer-container')
for i in div_container:
    href = i.get_attribute('href')
    for keys in adHREFs:
        if keys in href:
            hrefs.append("https://flipp.com" + href)

print(hrefs)


# Find the <flipp-translation> tag and get its 'title' attribute
#AdDate = driver.find_element('css selector', 'span.validity')
#print(AdDate.text)

# Close the WebDriver
#driver.quit()