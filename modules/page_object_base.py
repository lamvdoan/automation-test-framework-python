from modules.web_driver_base import WebDriverBase


class PageObjectBase(WebDriverBase):
    IMPLICIT_WAIT_TIME = 5

    def navigate_to(self, url):
        self.get_driver().get(url)

    def get_current_url(self):
        return self.get_driver().current_url
