class BasePage:
    def __init__(self, driver, url):
        self.browser = driver
        self.url = url
        self.browser_title = None

    def open(self):
        self.browser.get(self.url)

    def should_browser_title_be_correct(self):
        assert self.browser.title == self.browser_title
