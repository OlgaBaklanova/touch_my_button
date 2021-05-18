from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
import math

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


browser = webdriver.Chrome('C:\chromedriver\chromedriver.exe')
browser.get("http://suninjuly.github.io/explicit_wait2.html")

wait = WebDriverWait(browser, 12)
element = wait.until(EC.text_to_be_present_in_element((By.ID,'price'), '100'))
# button = WebDriverWait(browser, 12).until(
#         EC.element_to_be_clickable((By.ID, "book"))
#     )
button = browser.find_element_by_id('book')
button.click()

x_element = browser.find_element_by_id('input_value')
x = x_element.text
y = calc(x)

input1 = browser.find_element_by_id('answer')
input1.send_keys(y)

button = browser.find_element_by_css_selector('[type="submit"]')
button.click()
