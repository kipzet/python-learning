from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import pytest
import time
import math

lst = []

links = [
    'https://stepik.org/lesson/236895/step/1',
    'https://stepik.org/lesson/236896/step/1',
    'https://stepik.org/lesson/236897/step/1',
    'https://stepik.org/lesson/236898/step/1',
    'https://stepik.org/lesson/236899/step/1',
    'https://stepik.org/lesson/236903/step/1',
    'https://stepik.org/lesson/236904/step/1',
    'https://stepik.org/lesson/236905/step/1'
]


@pytest.fixture(scope="session")
def browser():
    browser = webdriver.Chrome()
    yield browser
    browser.quit()
    print('')
    print(' '.join(lst))


@pytest.mark.parametrize('link', links)
def test_less_3_6_step3(browser, link):
    browser.implicitly_wait(5)
    browser.get(link)
    answer = math.log(int(time.time()))
    browser.find_element_by_css_selector(".ember-text-area").send_keys(str(answer))
    browser.find_element_by_css_selector(".submit-submission").click()
    WebDriverWait(browser, 5).until(EC.presence_of_element_located((By.CLASS_NAME, "smart-hints__hint")))
    txt = browser.find_element_by_css_selector('.smart-hints__hint').text
    if txt != "Correct!":
        lst.append(txt)
    assert txt == "Correct!", f'answer is "{txt}" not correct'


'''Вариация записи ответа в лог'''

# try:
#     assert "Correct!" in txt
# except:
#     with open("3_6_3_test_Errors.log", "a") as f:
#         f.write(txt)
#     raise AssertionError('Error! See "3_6_3_test_Errors.log"')
