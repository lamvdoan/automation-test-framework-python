from selenium import webdriver

from resources.private.config import CHROME_DRIVER_PATH


class WebDriverBase:
    __instance = None
    driver = None

    def __init__(self):
        if WebDriverBase.__instance is None:
            WebDriverBase.__instance = self
            WebDriverBase.driver = webdriver.Chrome(CHROME_DRIVER_PATH)
            WebDriverBase.driver.implicitly_wait(2)

    @staticmethod
    def get_driver():
        return WebDriverBase.driver

    @staticmethod
    def close_browser():
        WebDriverBase.driver.quit()
