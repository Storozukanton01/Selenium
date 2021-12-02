from selenium import webdriver
import time 
import math
from selenium.webdriver.support.ui import Select

link = "http://suninjuly.github.io/selects1.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    # x_element = browser.find_element_by_id('treasure').get_attribute("valuex")
    # x = x_element
    # y = calc(x)
    # input1 = browser.find_element_by_id('answer')
    # input1.send_keys(y)
    number1 = int(browser.find_element_by_id('num1').text)
    number2 = int(browser.find_element_by_id('num2').text)
    sum = str(number1 + number2);
    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_value(sum) 
    button = browser.find_element_by_css_selector('button[type="submit"]')
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла