import pytest
from selenium import webdriver


@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    driver.implicitly_wait(time_to_wait=5)
    return driver


@pytest.fixture()
def user_credentials():
    return {"username": "Roman",
            "password": "Jdi1234",
            "full_username": "ROMAN IOVLEV"}
