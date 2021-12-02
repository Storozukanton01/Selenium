from selenium import webdriver
import time 
import math
import os 

link = "http://suninjuly.github.io/file_input.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    button = browser.find_element_by_css_selector('button[type="submit"]')
    input1 = browser.find_element_by_css_selector('input[name="firstname"]')
    input1.send_keys("Ivan")
    input2 = browser.find_element_by_css_selector('input[name="lastname"]')
    input2.send_keys("Petrov")
    input3 = browser.find_element_by_css_selector('input[name="email"]')
    input3.send_keys("email@gmail.com")
    file = browser.find_element_by_css_selector('#file')
    current_dir = os.path.abspath(os.path.dirname(file))    # получаем путь к директории текущего исполняемого файла 
    file_path = os.path.join(current_dir, 'лр3_альтернативна_ТРСПО_Сторожук.pdf')           # добавляем к этому пути имя файла 
    file.send_keys(file_path)
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла