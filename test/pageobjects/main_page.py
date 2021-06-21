import allure

from test.locators.buttons import Buttons
from test.locators.forms import Forms
from test.locators.header_buttons import HeaderButtons
from test.locators.text_sections import TextSections
from test.pageobjects.base_page import BasePage


class MainPage(BasePage):
    def __init__(self, browser, url):
        super().__init__(browser, url)
        self.browser_title = "Home Page"

    def __get_list_of_iframes_with_frame_button(self):
        return self.browser.find_elements_by_id("frame")

    def go_to_different_elements_page(self):
        self.browser.find_element(*HeaderButtons.DIFFERENT_ELEMENTS_BUTTON).click()

    @allure.step("Perform login")
    def login(self, username, password):
        self.browser.find_element(*HeaderButtons.PROFILE_MENU_BUTTON).click()
        self.browser.find_element(*Forms.USER_NAME_FORM).send_keys(username)
        self.browser.find_element(*Forms.USER_PASSWORD_FORM).send_keys(password)
        self.browser.find_element(*HeaderButtons.LOGIN_BUTTON).click()

    def open_service_sidebar_menu(self):
        self.browser.find_element(*HeaderButtons.SERVICE_DROPDOWN_BUTTON).click()
        return self

    @allure.step("Check if user authorized")
    def should_be_authorised(self, authorised_user_full_name):
        assert self.is_text_expected(TextSections.USER_NAME,
                                     authorised_user_full_name), "User is not authorised"

    @allure.step("Assert that there are item on the header section is displayed and it have proper text")
    def should_header_button_have_proper_name(self, button_locator, button_name):
        assert self.is_text_expected(button_locator, button_name), f"Unexpected text on {button_name} button in header"

    @allure.step("Assert that there are image on the Index Page and it's displayed")
    def should_icon_be_visible(self, icon_locator, icon_name):
        assert self.browser.find_element(*icon_locator).is_displayed(), f"{icon_name} icon is not displayed"

    @allure.step("Assert that there is text on the Index Page under icon and it have proper text")
    def should_text_under_icon_be_proper(self, text_section_locator, text, icon_name):
        assert self.is_text_expected(text_section_locator, text), f"Unexpected text under {icon_name} icon"

    @allure.step("Assert that there is the iframe with “Frame Button” exist")
    def should_iframes_with_frame_button_exist(self):
        assert self.__get_list_of_iframes_with_frame_button()

    @allure.step("Assert that there is item in the Left Section are displayed and it have proper text")
    def should_sidebar_buttons_have_proper_text(self, button_locator, button_name):
        assert self.is_text_expected(button_locator, button_name), f"Unexpected text on {button_name} button in sidebar"

    @allure.step("Switch to the iframe and check that there is “Frame Button” in the iframe")
    def should_any_iframe_with_frame_button_have_iframe(self):
        self.browser.switch_to.frame(self.__get_list_of_iframes_with_frame_button()[0])
        self.browser.find_element(*Buttons.FRAME_BUTTON)
        self.browser.switch_to.default_content()
