import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException

# Set up driver path and URL
# service = Service()  # Adjust path if needed
# driver = webdriver.Chrome(service=service)


usr = "lifoin92@gmail.com"
pas = "lifoin9212@"

browser = webdriver.Chrome()
browser.get('https://en-gb.facebook.com/')
user = browser.find_element(By.ID, "email")
user.clear()
user.send_keys(usr)

passwd = browser.find_element(By.ID, "pass")
passwd.clear()
passwd.send_keys(pas)

# Click the login button
login_button = browser.find_element(By.NAME, "login")
login_button.click()

y = 100
for timer in range(0,5000):
    browser.execute_script("window.scrollTo(0, "+str(y)+")")
    y += 100  
    time.sleep(1)

input()