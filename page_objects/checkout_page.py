from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#checkout class
class CheckOut:

    cart_button = (By.XPATH, "//button[contains(text(),'Cart')]")

    #pay with card button
    pay_with_card = "/html/body/div/div[@class='row top-space-30']/form/button"

    #iframe
    iframe = "/html/body/iframe[@name='stripe_checkout_app']"

    #card payment details
    email = "email"
    card_number = "card_number"
    card_expiry = "cc-exp"
    card_cvv = "cc-csc"
    submit ="submitButton"
    price = "/html/body/div/div[2]/table/tbody/tr/td[2]"
    zip = "billing-zip"
    email_address = "vasanthvsn.p@gmail.com"
    card_details = "4242 4242 4242 4242"
    expiry = "25"
    cvv = "123"
    zip_code = "641606"
    page_title = "Cart Items"


