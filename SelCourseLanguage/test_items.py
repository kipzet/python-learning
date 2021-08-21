def test_languages_less_3_6_step_9(browser):
    browser.implicitly_wait(5)
    browser.get("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/")
    elem = browser.find_elements_by_class_name("btn-add-to-basket")
    assert len(elem) == 1, f'The element was not found on this page or selector is not unique'
