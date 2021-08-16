from selenium import webdriver
import time

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/registration2.html")

    browser.find_element_by_css_selector(".first_block .first").send_keys("Тест")
    browser.find_element_by_css_selector(".first_block .second").send_keys("Остерон")
    browser.find_element_by_css_selector(".first_block .third").send_keys("t100steron@test.ru")

    browser.find_element_by_css_selector("button.btn").click()
    time.sleep(1)
    welcome_text = browser.find_element_by_tag_name("h1").text

    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    time.sleep(10)
    browser.quit()