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
        assert self.browser.find_element(*TextSections.USER_NAME).text == authorised_user_full_name

    def should_header_buttons_have_proper_names(self):
        assert self.browser.find_element(*HeaderButtons.HOME_BUTTON).text == "HOME"
        assert self.browser.find_element(*HeaderButtons.CONTACT_FORM_BUTTON).text == "CONTACT FORM"
        assert self.browser.find_element(*HeaderButtons.SERVICE_DROPDOWN_BUTTON).text == "SERVICE"
        assert self.browser.find_element(*HeaderButtons.METALS_COLORS_BUTTON).text == "METALS & COLORS"

    def should_icons_be_visible(self):
        assert self.browser.find_element(*Icons.ICON_PRACTISE).is_displayed() is True
        assert self.browser.find_element(*Icons.ICON_CUSTOM).is_displayed() is True
        assert self.browser.find_element(*Icons.ICON_BASE).is_displayed() is True
        assert self.browser.find_element(*Icons.ICON_MULTI).is_displayed() is True

    def should_texts_under_icons_be_proper(self):
        assert self.browser.find_element(*TextSections.PRACTISE_TEXT).text == "To include good practices\n" \
                                                                              "and ideas from successful\n" \
                                                                              "EPAM project"
        assert self.browser.find_element(*TextSections.CUSTOM_TEXT).text == "To be flexible and\n" \
                                                                            "customizable"
        assert self.browser.find_element(*TextSections.MULTI_TEXT).text == "To be multiplatform"
        assert self.browser.find_element(*TextSections.BASE_TEXT).text == "Already have good base\n" \
                                                                          "(about 20 internal and\n" \
                                                                          "some external projects),\n" \
                                                                          "wish to get more…"

    def should_iframes_with_frame_button_exist(self):
        assert self.__get_list_of_iframes_with_frame_button()

    def should_sidebar_buttons_have_proper_text(self):
        assert self.browser.find_element(*SidebarButtons.HOME_BUTTON).text == "Home"
        assert self.browser.find_element(*SidebarButtons.CONTACT_FORM_BUTTON).text == "Contact form"
        assert self.browser.find_element(*SidebarButtons.SERVICE_DROPDOWN_MENU).text == "Service"
        assert self.browser.find_element(*SidebarButtons.METALS_COLORS_BUTTON).text == "Metals & Colors"
        assert self.browser.find_element(*SidebarButtons.ELEMENTS_PACKS_BUTTON).text == "Elements packs"

    def should_any_iframe_with_frame_button_have_iframe(self):
        self.browser.switch_to.frame(self.__get_list_of_iframes_with_frame_button()[0])
        self.browser.find_element(*Buttons.FRAME_BUTTON)
        self.browser.switch_to.default_content()
