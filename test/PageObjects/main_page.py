from test.Locators.buttons import Buttons
from test.Locators.forms import Forms
from test.Locators.header_buttons import HeaderButtons
from test.Locators.icons import Icons
from test.Locators.sidebar_buttons import SidebarButtons
from test.Locators.text_sections import TextSections
from test.PageObjects.base_page import BasePage


class MainPage(BasePage):
    def __init__(self, browser, url):
        super().__init__(browser, url)
        self.browser_title = "Home Page"

    def __get_list_of_iframes_with_frame_button(self):
        return self.browser.find_elements_by_id("frame")

    def go_to_different_elements_page(self):
        self.browser.find_element(*HeaderButtons.DIFFERENT_ELEMENTS_BUTTON).click()

    def login(self, username, password):
        self.browser.find_element(*HeaderButtons.PROFILE_MENU_BUTTON).click()
        self.browser.find_element(*Forms.USER_NAME_FORM).send_keys(username)
        self.browser.find_element(*Forms.USER_PASSWORD_FORM).send_keys(password)
        self.browser.find_element(*HeaderButtons.LOGIN_BUTTON).click()

    def open_service_sidebar_menu(self):
        self.browser.find_element(*HeaderButtons.SERVICE_DROPDOWN_BUTTON).click()
        return self

    def should_be_authorised(self, authorised_user_full_name):
        assert self.is_text_expected(TextSections.USER_NAME,
                                     authorised_user_full_name), "User is not authorised"

    def should_header_button_have_proper_name(self, button_locator, button_name):
        assert self.is_text_expected(button_locator, button_name), f"Unexpected text on {button_name} button in header"

    def should_icon_be_visible(self, icon_locator, icon_name):
        assert self.browser.find_element(*icon_locator).is_displayed(), f"{icon_name} icon is not displayed"

    def should_text_under_icon_be_proper(self, text_section_locator, text, icon_name):
        assert self.is_text_expected(text_section_locator, text), f"Unexpected text under {icon_name} icon"

    def should_iframes_with_frame_button_exist(self):
        assert self.__get_list_of_iframes_with_frame_button()

    def should_sidebar_buttons_have_proper_text(self, button_locator, button_name):
        assert self.is_text_expected(button_locator, button_name), f"Unexpected text on {button_name} button in sidebar"

    def should_any_iframe_with_frame_button_have_iframe(self):
        self.browser.switch_to.frame(self.__get_list_of_iframes_with_frame_button()[0])
        self.browser.find_element(*Buttons.FRAME_BUTTON)
        self.browser.switch_to.default_content()
