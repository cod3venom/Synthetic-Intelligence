import time
from selenium.webdriver.remote.webelement import WebElement
from Kernel.Context.Context import Context


class dMayKnown:
    __ctx: Context
    __on: bool
    __finish: bool = False

    def __init__(self, ctx: Context):
        self.__ctx = ctx

    def ON(self):
        self.__on = True
        self.__detect()

    def OFF(self):
        self.__on = False

    @property
    def finish(self):
        return self.__finish

    @property
    def __lookupButtons(self) -> list:
        return self.__ctx.browser.Elements.findElementsByCss(Selectors.BUTTON_SELECTOR)

    def __detect(self, interval: int = 1):
        """
        :param interval:
        :type interval:
        :return:
        :rtype:
        """
        self.__ctx.browser.Javascript.scrollHVkey(interval=20)
        time.sleep(interval)
        self.__addFriend(element=self.__ctx.browser.Elements.findElementByCss(Selectors.MAIN_SELECTOR))

    def __addFriend(self, element: WebElement, interval: int = 5) -> bool:
        """
        :param element:
        :type element:
        :param interval:
        :type interval:
        :return:
        :rtype:
        """
        if element is not None:

            buttons = self.__lookupButtons
            if buttons is not None:

                button: WebElement
                for button in buttons:
                    button.click()
                    time.sleep(interval)
                self.__finish = True
            return True
        return False


class Selectors:
    MAIN_SELECTOR = '''div[aria-label='People You May Know']'''
    BUTTON_SELECTOR = 'div[aria-label="Add Friend"]'
    MARKER_CLASS = "dMayKnown"
