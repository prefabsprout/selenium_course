from datetime import datetime

from selenium.webdriver.support.select import Select

from locators.jdi_testing_locators import JdiTestingLocators
from locators.different_elements_locators import DifferentElementsLocators


def test_exercise_2(user_credentials, driver):
    # 1.Open browser and go to page
    driver.get(url="https://jdi-testing.github.io/jdi-light/index.html")

    # 2.Assert browser title
    assert driver.title == "Home Page"

    # 3.Perform login
    driver.find_element(*JdiTestingLocators.PROFILE_MENU).click()
    driver.find_element(*JdiTestingLocators.USER_NAME_FORM).send_keys(user_credentials["username"])
    driver.find_element(*JdiTestingLocators.USER_PASSWORD_FORM).send_keys(user_credentials["password"])
    driver.find_element(*JdiTestingLocators.LOGIN_BUTTON).click()

    # 4.Assert Username is loggined
    assert driver.find_element(*JdiTestingLocators.USER_NAME).text == user_credentials["full_username"]

    # 5.Open through the header menu Service -> Different Elements Page
    driver.find_element(*JdiTestingLocators.SIDEBAR_SERVICE_BUTTON).click()
    driver.find_element(*JdiTestingLocators.DIFFERENT_ELEMENTS_BUTTON).click()

    # 6-9.Select checkboxes. Assert there is a log for each checkbox
    driver.find_element(*DifferentElementsLocators.WIND_CHECKBOX).click()
    assert driver.find_element(*DifferentElementsLocators.LOG_SECTION).text == \
           f'{datetime.now().strftime("%H:%M:%S")} Wind: condition changed to true'

    driver.find_element(*DifferentElementsLocators.WATER_CHECKBOX).click()
    assert driver.find_element(*DifferentElementsLocators.LOG_SECTION).text == \
           f'{datetime.now().strftime("%H:%M:%S")} Water: condition changed to true'

    # 7-9.Select radiobutton. Assert there is a log for radiobutton
    driver.find_element(*DifferentElementsLocators.SELEN_RADIOBUTTON).click()
    assert driver.find_element(*DifferentElementsLocators.LOG_SECTION).text == \
           f'{datetime.now().strftime("%H:%M:%S")} metal: value changed to Selen'

    # 8-9.Select in dropdown. Assert there is a log for dropdown
    element_dropdown_select = Select(driver.find_element(*DifferentElementsLocators.ELEMENT_DROPDOWN))
    element_dropdown_select.select_by_visible_text("Yellow")
    assert driver.find_element(*DifferentElementsLocators.LOG_SECTION).text == \
           f'{datetime.now().strftime("%H:%M:%S")} Colors: value changed to Yellow'

    # 10.Close browser
    driver.quit()
