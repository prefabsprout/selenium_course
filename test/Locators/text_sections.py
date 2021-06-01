from selenium.webdriver.common.by import By


class TextSections:
    PRACTISE_TEXT = (By.CSS_SELECTOR, ".benefits > div:nth-child(1) .benefit-txt")
    CUSTOM_TEXT = (By.CSS_SELECTOR, ".benefits > div:nth-child(2) .benefit-txt")
    MULTI_TEXT = (By.CSS_SELECTOR, ".benefits > div:nth-child(3) .benefit-txt")
    BASE_TEXT = (By.CSS_SELECTOR, ".benefits > div:nth-child(4) .benefit-txt")
    LOG_SECTION = (By.XPATH, "//ul[@class='panel-body-list logs']//li[1]")
    USER_NAME = (By.ID, "user-name")
