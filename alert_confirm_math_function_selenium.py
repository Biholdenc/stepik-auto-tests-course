from selenium import webdriver
import time
import math

try:

    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))


    link = "http://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    button = browser.find_element_by_css_selector('button.btn').click()

    confirm = browser.switch_to.alert.accept()

    find_x = browser.find_element_by_id('input_value').text
    find_sum_x = calc(find_x)

    input_number = browser.find_element_by_id('answer').send_keys(find_sum_x)

    button2 = browser.find_element_by_css_selector('button.btn').click()







finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()
