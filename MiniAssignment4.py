import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from page_objects.temperature_page import Temperaturepage
from page_objects.moisturizers_page import Moisturizers
from page_objects.sunscreens_page import Sunscreen
from page_objects.checkout_page import CheckOut
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

class CreamSelection():

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()
    driver.get("https://weathershopper.pythonanywhere.com/")
    time.sleep(3)
    tempInDegree = driver.find_element(By.XPATH,Temperaturepage.temperature).text
    actualtemp = tempInDegree.split(" ")
    currentTemp = int(str(actualtemp[0]))

    if currentTemp >= 19:
        driver.find_element(By.XPATH,Temperaturepage.sunscr).click()
        time.sleep(5)

        elementlsit = driver.find_elements(By.XPATH, Sunscreen.listofElements)
        pricelist = []
        tofind = "SPF-50"
        for x in range(0, 6):
            s = elementlsit[x].text

            if tofind in s:
                price = elementlsit[x].find_element(By.XPATH, Sunscreen.pricefield).text
                currentprice = ''.join(filter(str.isdigit, price))
                pricelist.append(int(currentprice))

        leastAloeProduct = min(pricelist)
        driver.find_element(By.XPATH, Sunscreen.addtoCart.format(tofind, leastAloeProduct)).click()
        driver.find_element(By.XPATH, Sunscreen.cart_button).click()

        try:
            # wait 10 seconds before looking for element
            element = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "/html/body/div/div[@class='row top-space-30']/form/button")))
            element.click()

        except TimeoutException:
            print("Failed to load pay with card button")

        iframe = driver.find_element(By.XPATH,CheckOut.iframe)
        # switch to iframe
        driver.switch_to.frame(iframe)
        # fill all the form details
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "email")))
        element.send_keys(CheckOut.email_address)
        # self.driver.find_element(*CheckOut.email).send_keys(*CheckOut.email_address)

        for i in range(1, 6):
            driver.find_element(By.ID, CheckOut.card_number).send_keys(CheckOut.card_details)

        driver.find_element(By.ID, CheckOut.card_cvv).send_keys(CheckOut.cvv)
        driver.find_element(By.ID, CheckOut.zip).send_keys(CheckOut.zip_code)
        driver.find_element(By.ID, CheckOut.card_expiry).click()
        driver.find_element(By.ID, CheckOut.card_expiry).send_keys(CheckOut.expiry)
        driver.find_element(By.ID, CheckOut.card_expiry).send_keys(CheckOut.expiry)
        driver.find_element(By.ID, CheckOut.submit).click()


    else:
        driver.find_element(By.XPATH,Temperaturepage.moist).click()
        elementlsit = driver.find_elements(By.XPATH, Moisturizers.listofElements)
        pricelist = []
        tofind = "Almond"
        for x in range(0, 6):
            s = elementlsit[x].text

            if tofind in s:
                price = elementlsit[x].find_element(By.XPATH, Moisturizers.pricefield).text
                currentprice = ''.join(filter(str.isdigit, price))
                pricelist.append(int(currentprice))

        leastAloeProduct = min(pricelist)
        driver.find_element(By.XPATH, Moisturizers.addtoCart.format(tofind, leastAloeProduct)).click()
        driver.find_element(By.XPATH, Sunscreen.cart_button).click()

        try:
            # wait 10 seconds before looking for element
            element = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "/html/body/div/div[@class='row top-space-30']/form/button")))
            element.click()

        except TimeoutException:
            print("Failed to load pay with card button")

        iframe = driver.find_element(By.XPATH,CheckOut.iframe)
        # switch to iframe
        driver.switch_to.frame(iframe)
        # fill all the form details
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "email")))
        element.send_keys(CheckOut.email_address)
        # self.driver.find_element(*CheckOut.email).send_keys(*CheckOut.email_address)

        for i in range(1, 6):
            driver.find_element(By.ID, CheckOut.card_number).send_keys(CheckOut.card_details)

        driver.find_element(By.ID, CheckOut.card_cvv).send_keys(CheckOut.cvv)
        driver.find_element(By.ID, CheckOut.zip).send_keys(CheckOut.zip_code)
        driver.find_element(By.ID, CheckOut.card_expiry).click()
        driver.find_element(By.ID, CheckOut.card_expiry).send_keys(CheckOut.expiry)
        driver.find_element(By.ID, CheckOut.card_expiry).send_keys(CheckOut.expiry)
        driver.find_element(By.ID, CheckOut.submit).click()


    time.sleep(5)
    driver.quit()





