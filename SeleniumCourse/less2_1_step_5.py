from selenium import webdriver
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get('http://suninjuly.github.io/math.html')

    browser.find_element_by_id('answer').send_keys(calc(browser.find_element_by_id('input_value').text))
    browser.find_element_by_css_selector('[for=robotCheckbox]').click()
    browser.find_element_by_css_selector('[for=robotsRule]').click()
    browser.find_element_by_css_selector('button.btn').click()

    alert = browser.switch_to.alert
    alert_text = alert.text
    alert.accept()

finally:
    print(alert_text.split()[-1])
    browser.quit()

