from selenium.webdriver.common.by import By


class HeaderButtons:
    PROFILE_MENU_BUTTON = (By.CLASS_NAME, "uui-profile-menu")
    LOGIN_BUTTON = (By.ID, "login-button")
    HOME_BUTTON = (By.CSS_SELECTOR, ".uui-header .nav > li:nth-child(1) > a")
    CONTACT_FORM_BUTTON = (By.CSS_SELECTOR, ".uui-header .nav > li:nth-child(2) > a")
    METALS_COLORS_BUTTON = (By.CSS_SELECTOR, ".uui-header .nav > li:nth-child(4) > a")
    SERVICE_DROPDOWN_BUTTON = (By.CSS_SELECTOR, ".uui-header .nav > li:nth-child(3) > a")
    DIFFERENT_ELEMENTS_BUTTON = (By.CSS_SELECTOR, ".uui-header .nav > li:nth-child(3) > ul > :nth-child(8)")
