from selenium.webdriver.common.by import By


class DifferentElementsLocators:
    WATER_CHECKBOX = (By.CSS_SELECTOR, ".main-content-hg > div:nth-child(2) >label:nth-child(1) input")
    WIND_CHECKBOX = (By.CSS_SELECTOR, ".main-content-hg > div:nth-child(2) >label:nth-child(3) input")
    SELEN_RADIOBUTTON = (By.CSS_SELECTOR, ".main-content-hg > div:nth-child(3) >label:nth-child(4) input")
    ELEMENT_DROPDOWN = (By.CSS_SELECTOR, ".main-content-hg > div:nth-child(4) select")
    LOG_SECTION = (By.XPATH, "//ul[@class='panel-body-list logs']//li[1]")