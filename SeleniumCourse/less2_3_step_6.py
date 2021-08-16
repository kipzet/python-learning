from selenium import webdriver
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


def print_ans(val):
    alert = val.switch_to.alert
    print(alert.text.split()[-1])
    alert.accept()


try:
    browser = webdriver.Chrome()
    browser.get('http://suninjuly.github.io/redirect_accept.html')
    browser.find_element_by_css_selector('button.btn').click()
    browser.switch_to.window(browser.window_handles[1])
    browser.find_element_by_id('answer').send_keys(calc(browser.find_element_by_id('input_value').text))
    browser.find_element_by_css_selector('button.btn').click()


finally:
    print_ans(browser)
    browser.quit()
