import time
from selenium.webdriver.remote.webelement import WebElement
from Kernel.Context.Context import Context


class dNotifications:
    __ctx: Context
    __on: bool

    def __init__(self, ctx: Context):
        self.__ctx = ctx

    def ON(self):
        self.__on = True
        self.__detect()

    def OFF(self):
        self.__on = False

    def __detect(self, interval: int = 1):
        """
        :param interval:
        :type interval:
        :return:
        :rtype:
        """
        while self.__on:

            time.sleep(interval)
            if not self.__on:
                return False

            newNotification = self.__ctx.browser.Elements.findElementByCss(Selectors.NOTIFICATIONS_ICON)
            self.__viewNotifications(element=newNotification)

    def __viewNotifications(self, element: WebElement, interval: int = 5) -> bool:
        if element is not None:
            element.click()
            time.sleep(interval)
            element.click()
            return True
        return False


class Selectors:
    POSTS_CONTAINER = '''//div[@role="main"]'''
    NOTIFICATIONS_ICON = '''div[aria-label *="Notifications, "] > span > span'''
    MARKER_CLASS = "dMayKnown"
