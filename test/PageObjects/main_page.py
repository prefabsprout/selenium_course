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

    def login(self, username, password):
        self.browser.find_element(*HeaderButtons.PROFILE_MENU_BUTTON).click()
        self.browser.find_element(*Forms.USER_NAME_FORM).send_keys(username)
        self.browser.find_element(*Forms.USER_PASSWORD_FORM).send_keys(password)
        self.browser.find_element(*HeaderButtons.LOGIN_BUTTON).click()

    def should_be_authorised(self, authorised_user_full_name):
        assert self.is_text_expected(TextSections.USER_NAME,
                                     authorised_user_full_name), "User is not authorised"

    def should_header_buttons_have_proper_names(self):
        assert self.is_text_expected(HeaderButtons.HOME_BUTTON, "HOME"), "Unexpected text on HOME button in header"
        assert self.is_text_expected(HeaderButtons.CONTACT_FORM_BUTTON, "CONTACT FORM"), \
            "Unexpected text on CONTACT FORM button in header"
        assert self.is_text_expected(HeaderButtons.SERVICE_DROPDOWN_BUTTON, "SERVICE"), \
            "Unexpected text on SERVICE button in header"
        assert self.is_text_expected(HeaderButtons.METALS_COLORS_BUTTON, "METALS & COLORS"), \
            "Unexpected text on METALS & COLORS button in header"

    def should_icons_be_visible(self):
        assert self.browser.find_element(*Icons.ICON_PRACTISE).is_displayed(), "Practise icon is not displayed"
        assert self.browser.find_element(*Icons.ICON_CUSTOM).is_displayed(), "Custom icon is not displayed"
        assert self.browser.find_element(*Icons.ICON_BASE).is_displayed(), "Base icon is not displayed"
        assert self.browser.find_element(*Icons.ICON_MULTI).is_displayed(), "Multi icon is not displayed"

    def should_texts_under_icons_be_proper(self):
        assert self.is_text_expected(TextSections.PRACTISE_TEXT,
                                     "To include good practices\n"
                                     "and ideas from successful\n"
                                     "EPAM project"), "Unexpected text under PRACTISE icon"
        assert self.is_text_expected(TextSections.CUSTOM_TEXT,
                                     "To be flexible and\n"
                                     "customizable"), "Unexpected text under CUSTOM icon"
        assert self.is_text_expected(TextSections.MULTI_TEXT,
                                     "To be multiplatform"), "Unexpected text under MULTI icon"
        assert self.is_text_expected(TextSections.BASE_TEXT,
                                     "Already have good base\n"
                                     "(about 20 internal and\n"
                                     "some external projects),\n"
                                     "wish to get more…"), "Unexpected text under BASE icon"

    def should_iframes_with_frame_button_exist(self):
        assert self.__get_list_of_iframes_with_frame_button()

    def should_sidebar_buttons_have_proper_text(self):
        assert self.is_text_expected(SidebarButtons.HOME_BUTTON, "Home"), "Unexpected text on Home button in sidebar"
        assert self.is_text_expected(SidebarButtons.CONTACT_FORM_BUTTON, "Contact form"), \
            "Unexpected text on Contact form button in sidebar"
        assert self.is_text_expected(SidebarButtons.SERVICE_DROPDOWN_MENU, "Service"), \
            "Unexpected text on Service button in sidebar"
        assert self.is_text_expected(SidebarButtons.METALS_COLORS_BUTTON, "Metals & Colors"), \
            "Unexpected text on Metals & Colors button in sidebar"
        assert self.is_text_expected(SidebarButtons.ELEMENTS_PACKS_BUTTON, "Elements packs"), \
            "Unexpected text on Elements packs button in sidebar"

    def should_any_iframe_with_frame_button_have_iframe(self):
        self.browser.switch_to.frame(self.__get_list_of_iframes_with_frame_button()[0])
        self.browser.find_element(*Buttons.FRAME_BUTTON)
        self.browser.switch_to.default_content()
