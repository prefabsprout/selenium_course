from datetime import datetime

from selenium.webdriver.support.select import Select

from test.Locators.buttons import Buttons
from test.Locators.different_elements_page_locators import Checkboxes
from test.Locators.dropdowns import Dropdowns
from test.Locators.forms import Forms
from test.Locators.icons import Icons
from test.Locators.radiobuttons import RadioButtons
from test.Locators.text_sections import TextSections
from test.constants import HOMEPAGE_URL


def test_different_element_page_functionality(user_credentials, driver):
    # 1.Open browser and go to page
    driver.get(HOMEPAGE_URL)

    # 2.Assert browser title
    assert driver.title == "Home Page"

    # 3.Perform login
    driver.find_element(*Buttons.PROFILE_MENU_BUTTON).click()
    driver.find_element(*Forms.USER_NAME_FORM).send_keys(user_credentials["username"])
    driver.find_element(*Forms.USER_PASSWORD_FORM).send_keys(user_credentials["password"])
    driver.find_element(*Buttons.LOGIN_BUTTON).click()

    # 4.Assert Username is logged
    assert driver.find_element(*TextSections.USER_NAME).text == user_credentials["full_username"]

    # 5.Open through the header menu Service -> Different Elements Page
    driver.find_element(*Buttons.SIDEBAR_SERVICE_BUTTON).click()
    driver.find_element(*Buttons.DIFFERENT_ELEMENTS_BUTTON).click()

    # 6-9.Select checkboxes. Assert there is a log for each checkbox
    driver.find_element(*Checkboxes.WIND_CHECKBOX).click()
    assert driver.find_element(*TextSections.LOG_SECTION).text == \
           f'{datetime.now().strftime("%H:%M:%S")} Wind: condition changed to true'

    driver.find_element(*Checkboxes.WATER_CHECKBOX).click()
    assert driver.find_element(*TextSections.LOG_SECTION).text == \
           f'{datetime.now().strftime("%H:%M:%S")} Water: condition changed to true'

    # 7-9.Select radiobutton. Assert there is a log for radiobutton
    driver.find_element(*RadioButtons.SELEN_RADIOBUTTON).click()
    assert driver.find_element(*TextSections.LOG_SECTION).text == \
           f'{datetime.now().strftime("%H:%M:%S")} metal: value changed to Selen'

    # 8-9.Select in dropdown. Assert there is a log for dropdown
    element_dropdown_select = Select(driver.find_element(*Dropdowns.ELEMENT_DROPDOWN))
    element_dropdown_select.select_by_visible_text("Yellow")
    assert driver.find_element(*TextSections.LOG_SECTION).text == \
           f'{datetime.now().strftime("%H:%M:%S")} Colors: value changed to Yellow'
