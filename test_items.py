import time
from selenium.webdriver.common.by import By


link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_items(browser):

    browser.get(link)
    
    time.sleep(5)
    
    value = browser.find_element(By.NAME, "language").get_attribute("value")
    
    if value == "ru":
        assert browser.find_element(By.CSS_SELECTOR, ".btn-add-to-basket").text == "Добавить в корзину"
 
    elif value == "es":
        assert browser.find_element(By.CSS_SELECTOR, ".btn-add-to-basket").text == "Añadir al carrito"
        
    elif value == "fr":
        assert browser.find_element(By.CSS_SELECTOR, ".btn-add-to-basket").text == "Ajouter au panier"
    
    elif value == "de":
        assert browser.find_element(By.CSS_SELECTOR, ".btn-add-to-basket").text == "In Warenkorb legen"
    
 
    time.sleep(5)
    
        
    browser.close()
    

    
    

