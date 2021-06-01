from selenium.webdriver.common.by import By


class Buttons:
    PROFILE_MENU_BUTTON = (By.CLASS_NAME, "uui-profile-menu")
    LOGIN_BUTTON = (By.ID, "login-button")
    HOME_BUTTON = (By.CSS_SELECTOR, ".uui-header .nav > li:nth-child(1) > a")
    CONTACT_FORM_BUTTON = (By.CSS_SELECTOR, ".uui-header .nav > li:nth-child(2) > a")
    METALS_COLORS_BUTTON = (By.CSS_SELECTOR, ".uui-header .nav > li:nth-child(4) > a")
    SIDEBAR_HOME_BUTTON = (By.CSS_SELECTOR, ".sidebar-menu > li:nth-child(1) span")
    SIDEBAR_CONTACT_FORM_BUTTON = (By.CSS_SELECTOR, ".sidebar-menu > li:nth-child(2) span")
    SIDEBAR_SERVICE_BUTTON = (By.CSS_SELECTOR, ".sidebar-menu > li:nth-child(3) span")
    SIDEBAR_METALS_COLORS_BUTTON = (By.CSS_SELECTOR, ".sidebar-menu > li:nth-child(4) span")
    SIDEBAR_ELEMENTS_PACKS_BUTTON = (By.CSS_SELECTOR, ".sidebar-menu > li:nth-child(5) span")
    DIFFERENT_ELEMENTS_BUTTON = (By.CSS_SELECTOR, ".sidebar-menu > li:nth-child(3) li:nth-child(8)")
    FRAME_BUTTON = (By.ID, "frame-button")
    SERVICE_DROPDOWN_BUTTON = (By.CSS_SELECTOR, ".uui-header .nav > li:nth-child(3) > a")
