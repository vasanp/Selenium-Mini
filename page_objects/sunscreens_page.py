class Sunscreen():
    listofElements = "//div[@class='row justify-content-center top-space-50']//div//p[1]"
    addtoCart = "//p[contains(text(),{})]//following-sibling::p[contains(text(),{})]//following-sibling::button"
    pricefield = ".//following-sibling::p"
    cart_button = "//button[contains(text(),'Cart')]"