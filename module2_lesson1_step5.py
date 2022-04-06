from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.get(link)
    
    # Считать значение для переменной х
    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
        
    # Посчитать математическую функцию от х  
    y = calc(x)
        
    # Ввести ответ в текстовое поле
    input = browser.find_element(By.ID,"answer")
    input.send_keys(y)
    
    #Отметить checkbox "I'm the robot"
    #Выбрать radiobutton "Robots rule!"
    input_checkbox = browser.find_element(By.ID,"robotCheckbox")
    input_checkbox.click()
    input_radiobutton = browser.find_element(By.ID,"robotsRule")
    input_radiobutton.click()
        
    # Отправить ответ
    button = browser.find_element(By.TAG_NAME, "button")
    button.click()
    time.sleep(4)
finally:
    
    # закрываем браузер после всех манипуляций
    browser.quit()
