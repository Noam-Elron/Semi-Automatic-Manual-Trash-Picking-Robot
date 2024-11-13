import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time

#is_headless and check_os and get_data cant be static methods since they require use of instance variables from each other.
class DataSalvage:
    
    chrome_options = Options()
    
    def __init__(self, url, headless=None):
        self.url = url
        self.headless = headless
        self.is_headless()
        self.check_os()
        self.get_data()

    def is_headless(self):
        if self.headless != None:
            self.chrome_options = Options()
            self.chrome_options.add_argument("--headless")
            self.chrome_options.add_argument("--window-size=1920x1080")
            self.chrome_options.add_argument("--log-level=3")

    def check_os(self):
        if os.name == 'nt':
            self.driver = os.getcwd() + "/chromedriver"
        else:
            self.driver = "/usr/lib/chromium-browser/chromedriver"    
        self.driver = webdriver.Chrome(chrome_options=self.chrome_options, executable_path=self.driver)
        self.driver.get(self.url)

    def get_data(self):
        time.sleep(0.1)
        try:
            self.element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "text3")))
        except:
            self.driver.close()
        self.element = self.element.get_attribute("textContent")
        return self.element

'''
url = "https://peterporker.pythonanywhere.com"
peterporker = DataSalvage(url, True)
print(peterporker.element)
'''







  














'''
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
'''
