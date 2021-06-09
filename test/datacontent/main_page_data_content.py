from test.Locators.header_buttons import HeaderButtons
from test.Locators.icons import Icons
from test.Locators.sidebar_buttons import SidebarButtons
from test.Locators.text_sections import TextSections


class MainPageDataContent:
    header_buttons_content = [(HeaderButtons.HOME_BUTTON, "HOME"),
                              (HeaderButtons.CONTACT_FORM_BUTTON, "CONTACT FORM"),
                              (HeaderButtons.SERVICE_DROPDOWN_BUTTON, "SERVICE"),
                              (HeaderButtons.METALS_COLORS_BUTTON, "METALS & COLORS")]

    icons_content = [(Icons.ICON_PRACTISE, "Practise"),
                     (Icons.ICON_CUSTOM, "Custom"),
                     (Icons.ICON_BASE, "Base"),
                     (Icons.ICON_MULTI, "Multi")]

    texts_under_icons_content = [(TextSections.PRACTISE_TEXT,
                                  "To include good practices\n"
                                  "and ideas from successful\n"
                                  "EPAM project",
                                  "Practise"),
                                 (TextSections.CUSTOM_TEXT,
                                  "To be flexible and\n"
                                  "customizable",
                                  "Custom"),
                                 (TextSections.MULTI_TEXT,
                                  "To be multiplatform",
                                  "Multi"),
                                 (TextSections.BASE_TEXT,
                                  "Already have good base\n"
                                  "(about 20 internal and\n"
                                  "some external projects),\n"
                                  "wish to get more…",
                                  "Base")]

    sidebar_buttons_content = [(SidebarButtons.HOME_BUTTON, "Home"),
                               (SidebarButtons.CONTACT_FORM_BUTTON, "Contact form"),
                               (SidebarButtons.SERVICE_DROPDOWN_MENU, "Service"),
                               (SidebarButtons.METALS_COLORS_BUTTON, "Metals & Colors"),
                               (SidebarButtons.ELEMENTS_PACKS_BUTTON, "Elements packs")]
