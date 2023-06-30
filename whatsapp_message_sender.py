import re
import time
from openpyxl import Workbook
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import urllib.parse
import pyautogui


def click_element_by_xpath(driver, xpath):
    try:
        element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, xpath)))
        element.click()
        print("Element clicked successfully!")
    except Exception as e:
        print("Error clicking element:", str(e))

#Type the group name and the message here
group_name = "Family Group"
input_message = "Happy New Year"

# URL-encode the input string
encoded_message = urllib.parse.quote(input_message)

# Set up the WebDriver
driver = webdriver.Chrome()

# Open WhatsApp Web and log in
driver.get('https://web.whatsapp.com/')

input('Press Enter after scanning the QR code and logging in to WhatsApp Web...')

# Locate the target group and click on it
search_box_xpath = "//*[@id='side']/div[1]/div/div/div[2]/div/div[1]"
search_box = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, search_box_xpath)))
search_box.send_keys(group_name)
group_xpath = f"//span[@title='{group_name}']"
group_element = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, group_xpath)))
group_element.click()

time.sleep(5)
# Find the group participants number using XPath
element = driver.find_element(By.XPATH, "//*[@id='main']/header/div[2]/div[2]/span")

# Get the element's content
element_content = element.get_attribute("innerHTML")

# Save the element's content to a file
with open("data.txt", "w", encoding="utf-8") as file:
    file.write(element_content)
time.sleep(5)
# Read the data from the file
with open('data.txt', 'r') as file:
    data = file.read()

# Extract phone numbers using regular expression
phone_numbers = re.findall(r'\+?\d{1,3}[-.\s]?\(?\d{1,3}\)?[-.\s]?\d{1,4}[-.\s]?\d{1,9}', data)

# Remove duplicate phone numbers
unique_phone_numbers = list(set(phone_numbers))

# Create a new Excel workbook
wb = Workbook()
ws = wb.active

# Write phone numbers to the worksheet
for index, phone_number in enumerate(unique_phone_numbers, start=1):
    ws.cell(row=index, column=1, value=phone_number)

# Save the workbook as an Excel file
wb.save('phone_numbers.xlsx')

# Format phone numbers
formatted_phone_numbers = [re.sub(r'[\s+]', '', number) for number in unique_phone_numbers]
i = 1
for number in formatted_phone_numbers:
    try:
        driver.get(f"https://wa.me/{number}?text={encoded_message}")
        time.sleep(2)
        if i == 1:  # Add a delay after the first loop
            time.sleep(20)
        i += 1
        click_element_by_xpath(driver, "//*[@id='action-button']/span")
        pyautogui.press('enter')
        print(f"Message Sent to {number} successfully!")
    except Exception as e:
        print(f"Error Send the Message to {number} :", str(e))

input('Press Enter to [Exit]')

# Close the browser
driver.quit()
