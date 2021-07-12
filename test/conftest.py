from datetime import datetime

import allure
import pytest
from allure_commons.types import AttachmentType
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


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item):
    outcome = yield
    test_result = outcome.get_result()
    if test_result.when == 'call' and test_result.failed:
        allure.attach(item.funcargs['browser'].get_screenshot_as_png(),
                      name=f"{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}-failure",
                      attachment_type=AttachmentType.PNG)
