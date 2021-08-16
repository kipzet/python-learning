from selenium import webdriver
from selenium.webdriver.support.ui import Select


def print_ans(val):
    alert = val.switch_to.alert
    print(alert.text.split()[-1])
    alert.accept()


try:
    browser = webdriver.Chrome()
    browser.get('http://suninjuly.github.io/selects1.html')
    summ = str(int(browser.find_element_by_id('num1').text) + int(browser.find_element_by_id('num2').text))
    select = Select(browser.find_element_by_id("dropdown"))
    select.select_by_value(summ)
    browser.find_element_by_css_selector('button.btn').click()

finally:
    print_ans(browser)
    browser.quit()
