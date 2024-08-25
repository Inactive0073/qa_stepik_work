import time

from selenium.webdriver.common.by import By

link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'


class TestPage:
    def test_page(self, browser):
        browser.implicitly_wait(10)
        browser.get(link)
        btn = browser.find_elements(By.CSS_SELECTOR, 'button.btn-add-to-basket')
        if len(btn) == 0:
            assert len(btn) == 1, 'Элемент не найден'
        if len(btn) > 1:
            assert len(btn) == 1, 'Найдено более одного элемента'
