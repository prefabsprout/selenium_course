from selenium.webdriver.common.by import By


class Checkboxes:
    WATER_CHECKBOX = (By.CSS_SELECTOR, ".main-content-hg > div:nth-child(2) >label:nth-child(1) input")
    WIND_CHECKBOX = (By.CSS_SELECTOR, ".main-content-hg > div:nth-child(2) >label:nth-child(3) input")
