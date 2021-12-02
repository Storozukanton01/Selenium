from selenium import webdriver
import time 
import math
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://SunInJuly.github.io/execute_script.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    x_element = browser.find_element_by_id('input_value')
    x = x_element.text
    y = calc(x)
    button = browser.find_element_by_css_selector('button[type="submit"]')
    browser.execute_script("window.scrollBy(0, 200);")
    input1 = browser.find_element_by_id('answer')
    input1.send_keys(y)
    tick1 = browser.find_element_by_id('robotCheckbox')
    tick1.click()
    tick2 = browser.find_element_by_id('robotsRule')
    tick2.click()
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла