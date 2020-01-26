from appium import webdriver
from resources.private.config import APPIUM_DRIVER_HOST, MOBILE_TYPE


class MobileDriverBase:
    __instance = None
    driver = None

    @staticmethod
    def get_instance():
        """ Static access method. """
        if MobileDriverBase.__instance is None:
            MobileDriverBase()
        return MobileDriverBase.__instance

    def __init__(self):
        if MobileDriverBase.__instance is None:
            MobileDriverBase.__instance = self
            desired_caps = {}

            if MOBILE_TYPE == "ANDROID":
                desired_caps['platformName'] = 'Android'
                desired_caps['platformVersion'] = '8.1'
                desired_caps['automationName'] = 'uiautomator2'
                desired_caps['deviceName'] = 'Android Emulator'
                desired_caps['app'] = "PATH('../../../apps/selendroid-test-app.apk')"

                MobileDriverBase.driver = webdriver.Remote(APPIUM_DRIVER_HOST, desired_caps)
            elif MOBILE_TYPE == "IOS":
                desired_caps['platformName'] = 'iOS'
                desired_caps['platformVersion'] = '11.4'
                desired_caps['automationName'] = 'xcuitest'
                desired_caps['deviceName'] = 'iPhone Simulator'
                desired_caps['app'] = "PATH('../../../apps/selendroid-test-app.apk')"

                MobileDriverBase.driver = webdriver.Remote(APPIUM_DRIVER_HOST, desired_caps)

    @staticmethod
    def get_driver():
        return MobileDriverBase.driver
