import document as document
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By

from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()
driver.implicitly_wait(5)
driver.get("https://the-internet.herokuapp.com/")
driver.find_element(By.XPATH, "//li//a[text()='JavaScript Alerts']").click()
driver.implicitly_wait(5)
driver.find_element(By.XPATH, "//button[text()='Click for JS Prompt']").click()
a = driver.switch_to.alert
text = a.text
a.send_keys("Ex-Test")
time.sleep(3)
a.accept()
body_text = driver.find_element(By.XPATH,"//p[@id='result']").text
assert 'Ex-Test' in body_text


time.sleep(3)
driver.quit()

