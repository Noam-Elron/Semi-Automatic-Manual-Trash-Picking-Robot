import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time


url = "https://peterporker.pythonanywhere.com"

chrome_options = Options()

chrome_options.add_argument("--headless")

chrome_options.add_argument("--window-size=1920x1080")
chrome_options.add_argument("--log-level=3");


if os.name == 'nt':
    driver = os.getcwd() + "/chromedriver"
else:
    driver = "/usr/lib/chromium-browser/chromedriver"

driver = webdriver.Chrome(chrome_options=chrome_options, executable_path=driver)

driver.get(url)

time.sleep(0.1)
  
def get_data():
    try:
        element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "text3")))
    except:
        driver.close()
    element = element.get_attribute("textContent")
    return element
print(get_data())














def repeat2(func):
    
    result = None
    for i in range(10):
        if result:
            break
        result = func()
    return result

@repeat2
def get_data2():
    try:
        element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "text3")))
    except:
        driver.close()
    element = element.get_attribute("textContent")
    return element
#get_data2()

