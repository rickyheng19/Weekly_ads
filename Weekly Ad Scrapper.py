from selenium import webdriver
from selenium.webdriver.common.by import By
import time


# URL of the webpage containing the dynamic content
url = 'https://flipp.com/weekly_ads'

# Initialize WebDriver
driver = webdriver.Chrome()

# Load the page
driver.get(url)
time.sleep(5)  # Adjust sleep time as needed to ensure page fully loads

#Click a-z
driver.find_element(By.XPATH, "//button[@title='Sort circulars alphabetically by store']").click()

# Find the <flipp-translation> tag and get its 'title' attribute
#AdDate = driver.find_element('css selector', 'span.validity')
#print(AdDate.text)

# Close the WebDriver
#driver.quit()