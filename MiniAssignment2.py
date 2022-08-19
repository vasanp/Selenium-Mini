from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()
driver.implicitly_wait(5)
driver.get("http://webdriveruniversity.com/")
time.sleep(3)
buttonClick = driver.find_element(By.XPATH, '//div//h1[text()="BUTTON CLICKS"]')
dropdownCheckbox = driver.find_element(By.XPATH, '//div//h1[text()="DROPDOWN, CHECKBOXE(S) & RADIO BUTTON(S)"]')
textField = driver.find_element(By.XPATH, '//div//h1[text()="AUTOCOMPLETE TEXTFIELD"]')
scrollAround = driver.find_element(By.XPATH, '//div//h1[text()="SCROLLING AROUND"]')
todoList = driver.find_element(By.XPATH, '//div//h1[text()="TO DO LIST"]')
fileUpload = driver.find_element(By.XPATH, '//div//h1[text()="FILE UPLOAD"]')
actionsWork = driver.find_element(By.XPATH, '//div//h1[text()="ACTIONS"]')
prnwnd = driver.current_window_handle
actions = ActionChains(driver)

# Button Clicks task

actions.move_to_element(buttonClick).click().perform()
chwnd = driver.window_handles[1]
driver.switch_to.window(chwnd)
driver.implicitly_wait(5)
driver.find_element(By.XPATH,
                    '//h2[text()="WebElement Click"]//following-sibling::div//following-sibling::div//span//p').click()
driver.implicitly_wait(5)
time.sleep(3)
driver.find_element(By.XPATH,
                    "//div//p[text()='Well done for successfully using the ']//..//following-sibling::div//button[text()='Close']").click()
time.sleep(3)
driver.close()
driver.switch_to.window(prnwnd)

# dropdownCheckbox
actions.move_to_element(dropdownCheckbox).click().perform()
chwnd = driver.window_handles[1]
driver.switch_to.window(chwnd)
time.sleep(3)
select = Select(driver.find_element(By.ID, 'dropdowm-menu-1'))
time.sleep(1)
select.select_by_visible_text('Python')
driver.find_element(By.XPATH, "//label[text()='Option 1']").click()
time.sleep(1)
driver.find_element(By.XPATH, "//div//form[text()='Green']").click()
time.sleep(2)
driver.close()
driver.switch_to.window(prnwnd)

# textField entry

actions.move_to_element(textField).click().perform()
chwnd = driver.window_handles[1]
driver.switch_to.window(chwnd)
time.sleep(3)
driver.find_element(By.XPATH, "//div//input[@name='food-item']").send_keys("pizza")
time.sleep(1)
driver.find_element(By.XPATH, "//input[@id='submit-button']").click()
time.sleep(2)
driver.close()
driver.switch_to.window(prnwnd)

# Scrolling around
actions.move_to_element(scrollAround).click().perform()
chwnd = driver.window_handles[1]
driver.switch_to.window(chwnd)
time.sleep(3)

zone1 = driver.find_element(By.XPATH, "//div[@id='zone1']")
zone2 = driver.find_element(By.XPATH, "//div[@id='zone2']")
zone3 = driver.find_element(By.XPATH, "//div[@id='zone3']")

actions.move_to_element(zone1).perform()
actions.move_to_element(zone2).perform()
actions.move_to_element(zone3).perform()
time.sleep(2)
driver.close()
driver.switch_to.window(prnwnd)

# todoList

actions.move_to_element(todoList).click().perform()
chwnd = driver.window_handles[1]
driver.switch_to.window(chwnd)
time.sleep(3)
driver.find_element(By.XPATH, "//input[@type='text']").send_keys("Testing")
driver.find_element(By.XPATH, "//input[@type='text']").send_keys(Keys.RETURN)
time.sleep(2)
driver.close()
driver.switch_to.window(prnwnd)

# fileUpload

actions.move_to_element(fileUpload).click().perform()
chwnd = driver.window_handles[1]
driver.switch_to.window(chwnd)
time.sleep(3)
uploadfile = driver.find_element(By.XPATH, "//input[@name='filename']")
uploadfile.send_keys("/Users/vasanp/Documents/goku.webp")
time.sleep(3)
driver.find_element(By.XPATH, "//input[@type='submit']").click()
time.sleep(3)
Alert(driver).accept()
driver.close()
driver.switch_to.window(prnwnd)

# actionsWork

actions.move_to_element(actionsWork).click().perform()
chwnd = driver.window_handles[1]
driver.switch_to.window(chwnd)
time.sleep(3)
fromelement = driver.find_element(By.XPATH, "//p//b[text()='DRAG ME TO MY TARGET!']")
toelement = driver.find_element(By.XPATH, "//p//b[text()='DROP HERE!']")
doubleclickelement = driver.find_element(By.XPATH, "//h2[text()='Double Click Me!']")
hoverelement = driver.find_element(By.XPATH, "//button[text()='Hover Over Me First!']")
clickandholdelement = driver.find_element(By.XPATH, "//div[@id='click-box']")

actions.drag_and_drop(fromelement, toelement).perform()
time.sleep(2)
actions.double_click(doubleclickelement).perform()
time.sleep(2)
actions.move_to_element(hoverelement).perform()
time.sleep(2)
actions.click_and_hold(clickandholdelement).perform()
time.sleep(3)
driver.close()
driver.switch_to.window(prnwnd)

time.sleep(3)
driver.quit()
