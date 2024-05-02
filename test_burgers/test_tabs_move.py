from selenium.webdriver.common.by import By       
from locators import tab_template, tab_title_template         


class TestTabsMove:
    def test_tabs_move(self, wb):
        tabnames = ['Соусы', 'Начинки', 'Булки']
        for tabname in tabnames:
            tab_loc = tab_template % tabname
            title_loc = tab_title_template % tabname
            wb.find_element(By.XPATH, tab_loc).click()
            assert wb.find_element(By.XPATH, title_loc), 'Подзаголовок страницы не найден'
