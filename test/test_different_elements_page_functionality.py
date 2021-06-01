from datetime import datetime

from selenium.webdriver.support.select import Select

from test.Locators.checkboxes import Checkboxes
from test.Locators.dropdowns import Dropdowns
from test.Locators.forms import Forms
from test.Locators.header_buttons import HeaderButtons
from test.Locators.radiobuttons import RadioButtons
from test.Locators.text_sections import TextSections
from test.constants import HOMEPAGE_URL


def test_different_elements_page_functionality(user_credentials, browser):
    # 1.Open browser and go to page
    browser.get(HOMEPAGE_URL)

    # 2.Assert browser title
    assert browser.title == "Home Page"

    # 3.Perform login
    browser.find_element(*HeaderButtons.PROFILE_MENU_BUTTON).click()
    browser.find_element(*Forms.USER_NAME_FORM).send_keys(user_credentials["username"])
    browser.find_element(*Forms.USER_PASSWORD_FORM).send_keys(user_credentials["password"])
    browser.find_element(*HeaderButtons.LOGIN_BUTTON).click()

    # 4.Assert Username is logged
    assert browser.find_element(*TextSections.USER_NAME).text == user_credentials["full_username"]

    # 5.Open through the header menu Service -> Different Elements Page
    browser.find_element(*HeaderButtons.SERVICE_DROPDOWN_BUTTON).click()
    browser.find_element(*HeaderButtons.DIFFERENT_ELEMENTS_BUTTON).click()

    # 6-9.Select checkboxes. Assert there is a log for each checkbox
    browser.find_element(*Checkboxes.WIND_CHECKBOX).click()
    assert browser.find_element(*TextSections.LOG_SECTION).text == \
           f'{datetime.now().strftime("%H:%M:%S")} Wind: condition changed to true'

    browser.find_element(*Checkboxes.WATER_CHECKBOX).click()
    assert browser.find_element(*TextSections.LOG_SECTION).text == \
           f'{datetime.now().strftime("%H:%M:%S")} Water: condition changed to true'

    # 7-9.Select radiobutton. Assert there is a log for radiobutton
    browser.find_element(*RadioButtons.SELEN_RADIOBUTTON).click()
    assert browser.find_element(*TextSections.LOG_SECTION).text == \
           f'{datetime.now().strftime("%H:%M:%S")} metal: value changed to Selen'

    # 8-9.Select in dropdown. Assert there is a log for dropdown
    element_dropdown_select = Select(browser.find_element(*Dropdowns.ELEMENT_DROPDOWN))
    element_dropdown_select.select_by_visible_text("Yellow")
    assert browser.find_element(*TextSections.LOG_SECTION).text == \
           f'{datetime.now().strftime("%H:%M:%S")} Colors: value changed to Yellow'
