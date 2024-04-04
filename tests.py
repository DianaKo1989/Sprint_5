from time import sleep
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from faker import Faker

url = 'https://stellarburgers.nomoreparties.site'
name = 'oleg'
email = '123@ya.ru'
invalid_pass = 'miami'

@pytest.fixture(scope='class')
def wb():
    browser = webdriver.Chrome()
    browser.get(url)
    yield browser
    browser.quit()


@pytest.fixture(scope='session', autouse=True)
def fake_user():
    fake = Faker()
    email = fake.email()
    password = fake.password()
    return email, password


class TestRegistrFlow:
    def test_registr_negative(self, wb):
        wb.get(f'{url}/register')
        wb.find_element(By.XPATH, '//*[@id="root"]/div/main/div/form/fieldset[1]/div/div/input').send_keys(name)
        wb.find_element(By.XPATH, '//*[@id="root"]/div/main/div/form/fieldset[2]/div/div/input').send_keys(email)
        wb.find_element(By.XPATH, '//*[@id="root"]/div/main/div/form/fieldset[3]/div/div/input').send_keys(invalid_pass)
        wb.find_element(By.XPATH, '//*[@id="root"]/div/main/div/form/button').click()
        assert wb.find_element(By.XPATH, '//*[@id="root"]/div/main/div/form/fieldset[3]/div/p')
        # sleep(3)

    def test_registr_positive(self, wb, fake_user):
        email, valid_pass = fake_user
        wb.get(f'{url}/register')
        wb.find_element(By.XPATH, '//*[@id="root"]/div/main/div/form/fieldset[1]/div/div/input').send_keys(name)
        wb.find_element(By.XPATH, '//*[@id="root"]/div/main/div/form/fieldset[2]/div/div/input').send_keys(email)
        wb.find_element(By.XPATH, '//*[@id="root"]/div/main/div/form/fieldset[3]/div/div/input').send_keys(f'{valid_pass}')
        wb.find_element(By.XPATH, '//*[@id="root"]/div/main/div/form/button').click()
        # sleep(3)

    def test_enter(self, wb, fake_user):
        email, valid_pass = fake_user
        wb.get(f'{url}/login')
        wb.find_element(By.XPATH, '//*[@id="root"]/div/main/div/form/fieldset[1]/div/div/input').send_keys(email)
        wb.find_element(By.XPATH, '//*[@id="root"]/div/main/div/form/fieldset[2]/div/div/input').send_keys(f'{valid_pass}')
        wb.find_element(By.XPATH, '//*[@id="root"]/div/main/div/form/button').click()
        # sleep(3)

    def test_constructor_link(self, wb):
        wb.find_element(By.XPATH, "//*[text()='Конструктор']").click()
        # sleep(3)

    def test_logo_link(self, wb):
        wb.find_element(By.CSS_SELECTOR, 'header div a').click()
        # sleep(3)

    def test_exit(self, wb):
        wb.find_element(By.XPATH, "//*[text()='Личный Кабинет']").click()
        sleep(2)
        wb.find_element(By.XPATH, "//*[text()='Выход']").click()
        # sleep(3)


class TestAuthForm:
    def test_enter_via_enter_button(self, wb):
        wb.find_element(By.XPATH, "//*[text()='Войти в аккаунт']").click()
        assert wb.find_element(By.XPATH, "//*[text()='Вход']")

    def test_enter_via_enter_cabinet(self, wb):
        wb.find_element(By.XPATH, "//*[text()='Личный Кабинет']").click()
        assert wb.find_element(By.XPATH, "//*[text()='Вход']")

    def test_enter_via_enter_registration_form(self, wb):
        wb.find_element(By.XPATH, "//*[text()='Личный Кабинет']").click()
        wb.find_element(By.XPATH, "//*[text()='Восстановить пароль']").click()
        assert wb.find_element(By.XPATH, "//*[text()='Восстановление пароля']")
        wb.find_element(By.XPATH, "//*[text()='Войти']").click()
        assert wb.find_element(By.XPATH, "//*[text()='Вход']")

    def test_enter_via_enter_restore_pass(self, wb):
        wb.find_element(By.XPATH, "//*[text()='Личный Кабинет']").click()
        wb.find_element(By.XPATH, "//*[text()='Зарегистрироваться']").click()
        assert wb.find_element(By.XPATH, "//*[text()='Регистрация']")
        wb.find_element(By.XPATH, "//*[text()='Войти']").click()
        assert wb.find_element(By.XPATH, "//*[text()='Вход']")


class TestTabsMove:
    @pytest.mark.parametrize('tabname', ['Соусы', 'Начинки', 'Булки'])
    def test_tabs_move(self, tabname, wb):
        wb.find_element(By.XPATH, f"//*[text()='{tabname}']").click()
        assert True