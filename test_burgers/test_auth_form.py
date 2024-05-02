from selenium.webdriver.common.by import By
from locators import (
    lk_btn, 
    login_btn, 
    enter_lbl,
    signin_btn,
    recovery_pass_lbl,
    recover_pass_btn,
    signup_btn,
    register_lbl
)

class TestAuthForm:
    def test_enter_via_enter_button(self, wb):
        wb.find_element(By.XPATH, signin_btn).click()
        assert wb.find_element(By.XPATH, enter_lbl), 'Страница входа недоступна'

    def test_enter_via_enter_cabinet(self, wb):
        wb.find_element(By.XPATH, lk_btn).click()
        assert wb.find_element(By.XPATH, enter_lbl), 'Страница входа недоступна'

    def test_enter_via_enter_registration_form(self, wb):
        wb.find_element(By.XPATH, lk_btn).click()
        wb.find_element(By.XPATH, recover_pass_btn).click()
        assert wb.find_element(By.XPATH, recovery_pass_lbl), 'Страница восстановления пароля недоступна'
        wb.find_element(By.XPATH, login_btn).click()
        assert wb.find_element(By.XPATH, enter_lbl), 'Страница входа недоступна'

    def test_enter_via_enter_restore_pass(self, wb):
        wb.find_element(By.XPATH, lk_btn).click()
        wb.find_element(By.XPATH, signup_btn).click()
        assert wb.find_element(By.XPATH, register_lbl), 'Страница регистрации недоступна'    
        wb.find_element(By.XPATH, login_btn).click()
        assert wb.find_element(By.XPATH, enter_lbl), 'Страница входа недоступна'