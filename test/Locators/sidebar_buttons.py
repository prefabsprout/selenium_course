from selenium.webdriver.common.by import By


class SidebarButtons:
    HOME_BUTTON = (By.CSS_SELECTOR, ".sidebar-menu > li:nth-child(1) span")
    CONTACT_FORM_BUTTON = (By.CSS_SELECTOR, ".sidebar-menu > li:nth-child(2) span")
    SERVICE_BUTTON = (By.CSS_SELECTOR, ".sidebar-menu > li:nth-child(3) span")
    METALS_COLORS_BUTTON = (By.CSS_SELECTOR, ".sidebar-menu > li:nth-child(4) span")
    ELEMENTS_PACKS_BUTTON = (By.CSS_SELECTOR, ".sidebar-menu > li:nth-child(5) span")
    DIFFERENT_ELEMENTS_BUTTON = (By.CSS_SELECTOR, ".sidebar-menu > li:nth-child(3) li:nth-child(8)")
