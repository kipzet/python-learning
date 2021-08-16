from selenium import webdriver

link = "http://suninjuly.github.io/find_xpath_form"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    browser.find_element_by_tag_name('input').send_keys("Ivan")
    browser.find_element_by_name('last_name').send_keys("Petrov")
    browser.find_element_by_class_name('city').send_keys("Smolensk")
    browser.find_element_by_id('country').send_keys("Russia")
    browser.find_element_by_xpath("//button[@type='submit']").click()
    alert = browser.switch_to.alert
    alert_text = alert.text
    alert.accept()

finally:
    print(alert_text.split()[-1])
    browser.quit()
