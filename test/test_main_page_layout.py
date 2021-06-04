from test.Locators.forms import Forms
from test.Locators.header_buttons import HeaderButtons
from test.Locators.icons import Icons
from test.Locators.sidebar_buttons import SidebarButtons
from test.Locators.text_sections import TextSections
from test.constants import HOMEPAGE_URL


def test_main_page_layout(user_credentials, driver):
    # 1.Open browser and go to page
    driver.get(HOMEPAGE_URL)

    # 2.Assert browser title
    assert driver.title == "Home Page"

    # 3.Perform login
    driver.find_element(*HeaderButtons.PROFILE_MENU_BUTTON).click()
    driver.find_element(*Forms.USER_NAME_FORM).send_keys(user_credentials["username"])
    driver.find_element(*Forms.USER_PASSWORD_FORM).send_keys(user_credentials["password"])
    driver.find_element(*HeaderButtons.LOGIN_BUTTON).click()

    # 4.Assert Username is logged
    assert driver.find_element(*TextSections.USER_NAME).text == user_credentials["full_username"]

    # 5.Assert that there are 4 items on the header section are displayed and they have proper texts
    assert driver.find_element(*HeaderButtons.HOME_BUTTON).text == "HOME"
    assert driver.find_element(*HeaderButtons.CONTACT_FORM_BUTTON).text == "CONTACT FORM"
    assert driver.find_element(*HeaderButtons.SERVICE_DROPDOWN_BUTTON).text == "SERVICE"
    assert driver.find_element(*HeaderButtons.METALS_COLORS_BUTTON).text == "METALS & COLORS"

    # 6.Assert that there are 4 images on the Index Page and they are displayed
    assert driver.find_element(*Icons.ICON_PRACTISE).is_displayed() is True
    assert driver.find_element(*Icons.ICON_CUSTOM).is_displayed() is True
    assert driver.find_element(*Icons.ICON_BASE).is_displayed() is True
    assert driver.find_element(*Icons.ICON_MULTI).is_displayed() is True

    # 7.Assert that there are 4 texts on the Index Page under icons and they have proper text
    assert driver.find_element(*TextSections.PRACTISE_TEXT).text == "To include good practices\n" \
                                                                    "and ideas from successful\n" \
                                                                    "EPAM project"
    assert driver.find_element(*TextSections.CUSTOM_TEXT).text == "To be flexible and\n" \
                                                                  "customizable"
    assert driver.find_element(*TextSections.MULTI_TEXT).text == "To be multiplatform"
    assert driver.find_element(*TextSections.BASE_TEXT).text == "Already have good base\n" \
                                                                "(about 20 internal and\n" \
                                                                "some external projects),\n" \
                                                                "wish to get more…"

    # 8.Assert that there is the iframe with “Frame Button” exist
    iframes_with_frame_button = driver.find_elements_by_id("frame")
    assert iframes_with_frame_button != []

    # 9.Switch to the iframe and check that there is “Frame Button” in the iframe
    driver.switch_to.frame(iframes_with_frame_button[0])
    driver.find_element(*HeaderButtons.FRAME_BUTTON)

    # 10.Switch to original window back
    driver.switch_to.default_content()

    # 11.Assert that there are 5 items in the Left Section are displayed and they have proper text
    assert driver.find_element(*SidebarButtons.HOME_BUTTON).text == "Home"
    assert driver.find_element(*SidebarButtons.CONTACT_FORM_BUTTON).text == "Contact form"
    assert driver.find_element(*SidebarButtons.SERVICE_BUTTON).text == "Service"
    assert driver.find_element(*SidebarButtons.METALS_COLORS_BUTTON).text == "Metals & Colors"
    assert driver.find_element(*SidebarButtons.ELEMENTS_PACKS_BUTTON).text == "Elements packs"
