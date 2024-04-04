from time import sleep
from selenium.webdriver.common.by import By
from helpers.test_data import (
    url,
    name,
    email,
    invalid_pass
)
from helpers.locators import (
    lk_btn,
    builder_btn,
    logo_link,
    exit_btn,
    signup_btn,
    incorrecct_pass_msg,
    form_input_pass,
    form_input,
    enter_lbl,
    login_btn,
)

class TestRegistrFlow:
    def test_registr_negative(self, wb):
        wb.get(f'{url}/register')
        inputs = wb.find_elements(By.XPATH, form_input)
        inputs[0].send_keys(name)
        inputs[1].send_keys(email)
        wb.find_element(By.XPATH, form_input_pass).send_keys(invalid_pass)
        wb.find_element(By.XPATH, signup_btn).click()
        assert wb.find_element(By.XPATH, incorrecct_pass_msg), 'Сообщение об ошибке не найдено'

    def test_registr_positive(self, wb, fake_user):
        email, valid_pass = fake_user
        wb.get(f'{url}/register')
        inputs = wb.find_elements(By.XPATH, form_input)
        inputs[0].send_keys(name)
        inputs[1].send_keys(email)
        wb.find_element(By.XPATH, form_input_pass).send_keys(f'{valid_pass}')
        wb.find_element(By.XPATH, signup_btn).click()
        sleep(1)
        assert wb.find_element(By.XPATH, enter_lbl), 'Редирект на страницу входа не сработал'

    def test_enter(self, wb, fake_user):
        email, valid_pass = fake_user
        wb.get(f'{url}/login')
        wb.find_element(By.XPATH, form_input).send_keys(email)
        wb.find_element(By.XPATH, form_input_pass).send_keys(f'{valid_pass}')
        wb.find_element(By.XPATH, login_btn).click()
        wb.find_element(By.XPATH, lk_btn).click()
        sleep(1)
        assert wb.find_element(By.XPATH, f"//input[@value='{name}']"), 'Вход не сработал'
        wb.find_element(By.XPATH, exit_btn).click()
        assert wb.find_element(By.XPATH, enter_lbl), 'Редирект на страницу входа не сработал'

    def test_constructor_link(self, wb):
        wb.find_element(By.XPATH, builder_btn).click()
        assert wb.find_element(By.CSS_SELECTOR, 'h1').text == 'Соберите бургер', 'Заголовок главной страницы не совпадает с ожидаемым'

    def test_logo_link(self, wb):
        wb.find_element(By.CSS_SELECTOR, logo_link).click()
        assert wb.find_element(By.CSS_SELECTOR, 'h1').text == 'Соберите бургер', 'Заголовок главной страницы не совпадает с ожидаемым'