import pytest
from selenium.webdriver.common.by import By


class TestTabsMove:

    def test_tabs_init(self, wb):
        tabname = 'Булки'
        assert wb.find_element(By.XPATH, f"//*[text()='{tabname}']"), 'Не найдена ожидаемая вкладка'
        assert wb.find_element(By.XPATH, f"//h2[text()='{tabname}']"), 'Подзаголовок страницы не найден'

    @pytest.mark.parametrize('tabname', ['Соусы', 'Начинки'])
    def test_tabs_move(self, tabname, wb):
        wb.find_element(By.XPATH, f"//*[text()='{tabname}']").click()
        assert wb.find_element(By.XPATH, f"//h2[text()='{tabname}']"), 'Подзаголовок страницы не найден'