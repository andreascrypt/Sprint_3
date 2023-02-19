import random

import pytest
from selenium import webdriver

default_email = "testdata1@yandex.ru"
default_password = "password"


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.get("https://stellarburgers.nomoreparties.site/")
    yield driver
    driver.quit()


#
@pytest.fixture
def random_login():
    return 'Andrey_Kramarov' + str(random.randint(100, 999)) + '@yandex.ru'


@pytest.fixture
def random_password():
    return random.randint(100000, 999999)
