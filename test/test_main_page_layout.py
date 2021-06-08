from test.PageObjects.main_page import MainPage
from test.constants import HOMEPAGE_URL


class TestMainPageLayout:
    def test_is_main_page_open_correctly(self, browser):
        # Open browser and go to page
        main_page = MainPage(browser, HOMEPAGE_URL)
        main_page.open()

        # Assert browser title
        main_page.should_browser_title_be_correct()

    def test_guest_should_be_authorized(self, browser, user_credentials):
        # Open browser and go to page
        main_page = MainPage(browser, HOMEPAGE_URL)
        main_page.open()

        # Perform login and check if user authorized
        main_page.login(user_credentials["username"], user_credentials["password"])
        main_page.should_be_authorised(user_credentials["full_username"])

    def test_should_header_buttons_have_proper_names(self, browser):
        # Open browser and go to page
        main_page = MainPage(browser, HOMEPAGE_URL)
        main_page.open()

        # Assert that there are 4 items on the header section are displayed and they have proper texts
        main_page.should_header_buttons_have_proper_names()

    def test_should_icons_be_visible(self, browser):
        # Open browser and go to page
        main_page = MainPage(browser, HOMEPAGE_URL)
        main_page.open()

        # Assert that there are 4 images on the Index Page and they are displayed
        main_page.should_icons_be_visible()

    def test_should_texts_under_icons_be_proper(self, browser):
        # Open browser and go to page
        main_page = MainPage(browser, HOMEPAGE_URL)
        main_page.open()

        # Assert that there are 4 texts on the Index Page under icons and they have proper text
        main_page.should_texts_under_icons_be_proper()

    def test_should_any_iframe_with_frame_button_have_iframe(self, browser):
        # Open browser and go to page
        main_page = MainPage(browser, HOMEPAGE_URL)
        main_page.open()

        # Assert that there is the iframe with “Frame Button” exist
        main_page.should_iframes_with_frame_button_exist()

    def test_should_frame_button_exists_in_any_iframe(self, browser):
        # Open browser and go to page
        main_page = MainPage(browser, HOMEPAGE_URL)
        main_page.open()

        # Switch to the iframe and check that there is “Frame Button” in the iframe and switch to original window back
        main_page.should_any_iframe_with_frame_button_have_iframe()

    def test_should_sidebar_buttons_have_proper_text(self, browser):
        # Open browser and go to page
        main_page = MainPage(browser, HOMEPAGE_URL)
        main_page.open()

        # Assert that there are 5 items in the Left Section are displayed and they have proper text
        main_page.should_sidebar_buttons_have_proper_text()
