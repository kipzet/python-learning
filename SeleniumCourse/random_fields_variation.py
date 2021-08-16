import time
import random
from selenium import webdriver

# генерация списка символов для формирования случаных наборов букв произвольной длины
letters = list(range(97, 123)) + list(range(65, 91))

# link = "http://suninjuly.github.io/registration1.html"
link = "http://suninjuly.github.io/registration2.html"

browser = webdriver.Chrome()
browser.get(link)

try:
    time.sleep(3)
    first = browser.find_element_by_css_selector("input.first[required]")
    # генерация текста для ввода в форму
    # альтернатива (''.join([chr(i) for i in random.sample(letters, random.randint(3, 15))]))
    first.send_keys("".join(map(chr, random.sample(letters, random.randint(3, 15)))))

    second = browser.find_element_by_css_selector("input.second[required]")
    # генерация текста для ввода в форму
    second.send_keys("".join(map(chr, random.sample(letters, random.randint(3, 15)))))

    third = browser.find_element_by_css_selector("input.third[required]")
    # генерация текста для ввода в форму
    third.send_keys("".join(map(chr, random.sample(letters, random.randint(3, 15)))))
    time.sleep(5)

    browser.find_element_by_css_selector("form[method=get] button[type=submit]").click()

    # проверка ответа после успешной отправки формы
    welcome_text_elt = browser.find_element_by_tag_name("h1")
    welcome_text = welcome_text_elt.text
    assert "Congratulations! You have successfully registered!" == welcome_text
    print("тест прошел успешно успешно")

finally:
    browser.quit()
