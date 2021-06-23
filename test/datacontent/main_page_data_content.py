from test.locators.header_buttons import HeaderButtons
from test.locators.icons import Icons
from test.locators.sidebar_buttons import SidebarButtons
from test.locators.text_sections import TextSections


class MainPageDataContent:
    header_buttons_content = [{"button_locator": HeaderButtons.HOME_BUTTON, "button_name": "HOME"},
                              {"button_locator": HeaderButtons.CONTACT_FORM_BUTTON, "button_name": "CONTACT FORM"},
                              {"button_locator": HeaderButtons.SERVICE_DROPDOWN_BUTTON, "button_name": "SERVICE"},
                              {"button_locator": HeaderButtons.METALS_COLORS_BUTTON, "button_name": "METALS & COLORS"}]

    icons_content = [{"icon_locator": Icons.ICON_PRACTISE, "icon_name": "Practise"},
                     {"icon_locator": Icons.ICON_CUSTOM, "icon_name": "Custom"},
                     {"icon_locator": Icons.ICON_BASE, "icon_name": "Base"},
                     {"icon_locator": Icons.ICON_MULTI, "icon_name": "Multi"}]

    texts_under_icons_content = [{"text_section_locator": TextSections.PRACTISE_TEXT,
                                  "text": "To include good practices\n"
                                          "and ideas from successful\n"
                                          "EPAM project",
                                  "icon_name": "Practise"},
                                 {"text_section_locator": TextSections.CUSTOM_TEXT,
                                  "text": "To be flexible and\n"
                                          "oops, looks like something gone wrong...",
                                  "icon_name": "Custom"},
                                 {"text_section_locator": TextSections.MULTI_TEXT,
                                  "text": "To be multiplatform",
                                  "icon_name": "Multi"},
                                 {"text_section_locator": TextSections.BASE_TEXT,
                                  "text": "Already have good base\n"
                                          "(about 20 internal and\n"
                                          "some external projects),\n"
                                          "wish to get more…",
                                  "icon_name": "Base"}]

    sidebar_buttons_content = [{"button_locator": SidebarButtons.HOME_BUTTON, "button_name": "Home"},
                               {"button_locator": SidebarButtons.CONTACT_FORM_BUTTON, "button_name": "Contact form"},
                               {"button_locator": SidebarButtons.SERVICE_DROPDOWN_MENU, "button_name": "Service"},
                               {"button_locator": SidebarButtons.METALS_COLORS_BUTTON,
                                "button_name": "Metals & Colors"},
                               {"button_locator": SidebarButtons.ELEMENTS_PACKS_BUTTON,
                                "button_name": "Elements packs"}]
