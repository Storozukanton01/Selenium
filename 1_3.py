from selenium import webdriver
import time 
import math

link = "http://suninjuly.github.io/registration1.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)


    input1 = browser.find_element_by_tag_name('input')
    input1.send_keys("Ivan")
    input2 = browser.find_element_by_css_selector('.first_block .second')
    input2.send_keys("Petrov")
    input3 = browser.find_element_by_class_name('third')
    input3.send_keys("email@gmail.com")
    button = browser.find_element_by_css_selector('button[type="submit"]')
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла