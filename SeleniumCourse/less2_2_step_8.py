from selenium import webdriver
import os


def print_ans(val):
    alert = val.switch_to.alert
    print(alert.text.split()[-1])
    alert.accept()


try:
    browser = webdriver.Chrome()
    browser.get('http://suninjuly.github.io/file_input.html')
    browser.find_element_by_name('firstname').send_keys('Test')
    browser.find_element_by_name('lastname').send_keys('Osteron')
    browser.find_element_by_name('email').send_keys('t100steron@test.ru')
    curr = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(curr, 'new.txt')
    browser.find_element_by_id('file').send_keys(file_path)
    browser.find_element_by_css_selector('button.btn').click()


finally:
    print_ans(browser)
    browser.quit()
