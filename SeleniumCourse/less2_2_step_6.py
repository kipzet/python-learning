from selenium import webdriver
import math
import os



def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


def print_ans(val):
    alert = val.switch_to.alert
    print(alert.text.split()[-1])
    alert.accept()


try:
    browser = webdriver.Chrome()
    browser.get('http://suninjuly.github.io/execute_script.html')
    browser.find_element_by_id('answer').send_keys(calc(browser.find_element_by_id('input_value').text))
    browser.execute_script("return arguments[0].scrollIntoView(true);", browser.find_element_by_css_selector('button.btn'))
    browser.find_element_by_css_selector('[for=robotCheckbox]').click()
    browser.find_element_by_css_selector('[for=robotsRule]').click()
    browser.find_element_by_css_selector('button.btn').click()


finally:
    print_ans(browser)
    browser.quit()
    print(os.path.abspath(__file__))
    print(os.path.abspath(os.path.dirname(__file__)))
