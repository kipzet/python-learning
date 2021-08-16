from selenium import webdriver

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/huge_form.html")
    elements = browser.find_elements_by_css_selector("input[type='text']")
    for element in elements:
        element.send_keys("Мой ответ")

    button = browser.find_element_by_css_selector("button.btn")
    button.click()
    alert = browser.switch_to.alert
    alert_text = alert.text
    alert.accept()
finally:
    print(elements)
    print(type(elements[1]))
    print(type(1))
    print(type('hell'))
    print(alert_text.split()[-1])
    browser.quit()
