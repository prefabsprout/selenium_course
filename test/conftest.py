import pytest
from selenium import webdriver


@pytest.fixture()
def browser():
    browser = webdriver.Chrome()
    browser.implicitly_wait(time_to_wait=5)
    yield browser
    browser.quit()


@pytest.fixture()
def user_credentials():
    return {"username": "Roman",
            "password": "Jdi1234",
            "full_username": "ROMAN IOVLEV"}
