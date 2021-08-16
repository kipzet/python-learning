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
    browser.get('http://suninjuly.github.io/get_attribute.html')
    x = browser.find_element_by_id("treasure").get_attribute("valuex")
    browser.find_element_by_id('answer').send_keys(calc(x))
    browser.find_element_by_id('robotCheckbox').click()
    browser.find_element_by_id('robotsRule').click()
    browser.find_element_by_css_selector('button.btn').click()


finally:
    print_ans(browser)
    browser.quit()
