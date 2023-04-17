from selenium.webdriver.common.by import By
import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_language(browser):
    browser.get(link)
    time.sleep(30)
    button = browser.find_element(By.CSS_SELECTOR, "[class='btn btn-lg btn-primary btn-add-to-basket']")
    assert button is not None, 'Error: "button not found"'
