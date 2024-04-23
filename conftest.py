import pytest
from faker import Faker
from selenium import webdriver
from helpers.test_data import url

@pytest.fixture(scope='function')
def wb():
    browser = webdriver.Chrome()
    browser.get(url)
    yield browser
    browser.quit()


@pytest.fixture(scope='session')
def fake_user():
    fake = Faker()
    email = fake.email()
    password = fake.password()
    return email, password