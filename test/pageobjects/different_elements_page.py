from datetime import datetime

import allure
from selenium.webdriver.support.select import Select

from test.locators.text_sections import TextSections
from test.pageobjects.base_page import BasePage


class DifferentElementsPage(BasePage):
    def __init__(self, browser, url):
        super().__init__(browser, url)
        self.browser_title = "Different Elements"

    @allure.step("Select in dropdown. Assert there is a log for dropdown")
    def select_element_from_dropdown(self, dropdown_locator, element):
        dropdown_selector = Select(self.browser.find_element(*dropdown_locator))
        dropdown_selector.select_by_visible_text(element)
        current_time = datetime.now().strftime("%H:%M:%S")
        self.should_logs_about_dropdown_interaction_exist(element, current_time)

    @allure.step("Select checkboxes. Assert there is a log for each checkbox")
    def select_checkbox(self, checkbox_locator, checkbox_name):
        self.browser.find_element(*checkbox_locator).click()
        current_time = datetime.now().strftime("%H:%M:%S")
        self.should_logs_about_checkbox_interaction_exist(checkbox_name, current_time)

    @allure.step("Select radiobutton. Assert there is a log for radiobutton")
    def select_radiobutton(self, radiobutton_locator, radiobutton_name):
        self.browser.find_element(*radiobutton_locator).click()
        current_time = datetime.now().strftime("%H:%M:%S")
        self.should_logs_about_radiobutton_interaction_exist(radiobutton_name, current_time)

    def should_logs_about_checkbox_interaction_exist(self, checkbox_name, current_time):
        assert self.is_text_expected(TextSections.LOG_SECTION,
                                     f'{current_time} {checkbox_name}: condition changed to true'), \
            "Logs about checkbox interaction are not exist"

    def should_logs_about_radiobutton_interaction_exist(self, radiobutton_name, current_time):
        assert self.is_text_expected(TextSections.LOG_SECTION,
                                     f'{current_time} metal: value changed to {radiobutton_name}'), \
            "Logs about radiobutton interaction are not exist"

    def should_logs_about_dropdown_interaction_exist(self, value_from_dropdown, current_time):
        assert self.is_text_expected(TextSections.LOG_SECTION,
                                     f'{current_time} Colors: value changed to {value_from_dropdown}'), \
            "Logs about dropdown interaction are not exist"
