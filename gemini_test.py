from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome(executable_path='/path/to/chromedriver')

driver.get("https://gemini.com/login")

# Login
username = driver.find_element(By.NAME, "username")
password = driver.find_element(By.NAME, "password")

#username.send_keys("")
#password.send_keys("")
#password.send_keys(Keys.RETURN)

time.sleep(5)
driver.get("https://gemini.com/chats")

time.sleep(5)

chats = driver.find_elements(By.CLASS_NAME, "chat-element-class")

for chat in chats:
    delete_button = chat.find_element(By.CLASS_NAME, "delete-button-class")
    delete_button.click()
    time.sleep(2)

driver.quit()
