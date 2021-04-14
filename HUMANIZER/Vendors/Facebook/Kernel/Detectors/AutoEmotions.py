import random
import time
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException, \
    ElementNotInteractableException, ElementClickInterceptedException
from selenium.webdriver.remote.webelement import WebElement

from Kernel.Context.Context import Context
from Kernel.DataOps.DictParser import DictParser
from Kernel.Global import __texts__, __levels__, __logger__
from Kernel.Browser.Browser import Browser
import threading as thr

from Vendors.Facebook.Kernel.Features.Auth.FbAuth import FbAuth


class dAutoEmotions:
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
            self.__ctx.browser.Javascript.scrollDownByKey(interval=interval)
            if not self.__on:
                return False

            self.__hitEmotion()

    def __hitEmotion(self, interval: int = 5):
        emotionButtons = self.__ctx.browser.Elements.findElementsByCss(Selectors.EMOTION_SELECTOR)
        if emotionButtons is not None:
            button: WebElement
            for button in emotionButtons:
                self.__ctx.browser.Elements.click(target=button)
                time.sleep(interval)


class Selectors:
    EMOTION_SELECTOR = '''div[aria-label="Like"]'''
