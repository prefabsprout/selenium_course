from test.locators.checkboxes import Checkboxes
from test.locators.dropdowns import Dropdowns
from test.locators.radiobuttons import RadioButtons
from test.pageobjects.different_elements_page import DifferentElementsPage
from test.pageobjects.main_page import MainPage
from test.constants import HOMEPAGE_URL


class TestDifferentElementsPageFunctionality:
    def test_checkboxes(self, browser, user_credentials):
        # Open browser and go to page
        main_page = MainPage(browser, HOMEPAGE_URL)
        main_page.open()

        # Perform login and check if user authorized
        main_page.login(user_credentials["username"], user_credentials["password"])
        main_page.should_be_authorised(user_credentials["full_username"])

        # Open through the header menu Service -> Different Elements Page
        main_page.open_service_sidebar_menu() \
            .go_to_different_elements_page()
        different_elements_page = DifferentElementsPage(browser=main_page.browser, url=main_page.browser.current_url)

        # Select checkboxes. Assert there is a log for each checkbox
        different_elements_page.select_checkbox(Checkboxes.WIND_CHECKBOX, "Wind")
        different_elements_page.select_checkbox(Checkboxes.WATER_CHECKBOX, "Water")

    def test_radiobutton(self, browser, user_credentials):
        # Open browser and go to page
        main_page = MainPage(browser, HOMEPAGE_URL)
        main_page.open()

        # Perform login and check if user authorized
        main_page.login(user_credentials["username"], user_credentials["password"])
        main_page.should_be_authorised(user_credentials["full_username"])

        # Open through the header menu Service -> Different Elements Page
        main_page.open_service_sidebar_menu() \
            .go_to_different_elements_page()
        different_elements_page = DifferentElementsPage(browser=main_page.browser, url=main_page.browser.current_url)

        # Select radiobutton. Assert there is a log for radiobutton
        different_elements_page.select_radiobutton(RadioButtons.SELEN_RADIOBUTTON, "Selen")

    def test_dropdown(self, browser, user_credentials):
        # Open browser and go to page
        main_page = MainPage(browser, HOMEPAGE_URL)
        main_page.open()

        # Perform login and check if user authorized
        main_page.login(user_credentials["username"], user_credentials["password"])
        main_page.should_be_authorised(user_credentials["full_username"])

        # Open through the header menu Service -> Different Elements Page
        main_page.open_service_sidebar_menu() \
            .go_to_different_elements_page()
        different_elements_page = DifferentElementsPage(browser=main_page.browser, url=main_page.browser.current_url)

        # Select in dropdown. Assert there is a log for dropdown
        different_elements_page.select_element_from_dropdown(Dropdowns.ELEMENT_DROPDOWN, "Yellow")
