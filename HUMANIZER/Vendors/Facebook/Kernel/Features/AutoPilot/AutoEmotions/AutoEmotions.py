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


class AutoEmotions:
    __ctx: Context
    __clickableEmotionsList = 'div[aria-label="Like"]'
    __infiniteScrollToBottom = ''' setInterval(function() { window.scrollTo(0, document.body.scrollHeight); }, 2000); '''
    __autoID: int = 0

    def __init__(self, ctx: Context):
        self.__ctx = ctx
        self.__pack = AutoEmotionsPack()

    def execute(self):
        self.__detectButtons()

    def __detectButtons(self):
        likeContainers = self.__ctx.browser.Elements.findElementsByCss(self.__clickableEmotionsList)

        container: WebElement
        for index, container in enumerate(likeContainers):
            validButton = self.__pack.add(container)
            if validButton:
                self.__clickLike(target_button=container)
            if index == len(likeContainers):
                self.__ctx.browser.Javascript.scrollDownByKey(interval=3)

    def __clickLike(self, target_button: WebElement) -> bool:
        try:
            self.__autoID += 1
            self.__ctx.browser.Elements.setAttribute(target_button, 'HUMANIZER_ID', self.__autoID)
            self.__ctx.browser.Javascript.scrollToElement('*[HUMANIZER_ID]')
            target_button.click()
            time.sleep(3)

        except StaleElementReferenceException:
            return False
        except NoSuchElementException:
            return False
        except ElementNotInteractableException:
            return False
        except ElementClickInterceptedException:
            return False


class AutoEmotionsPack:
    __AUTOID: int = 0

    __REACT_STACK_ = {}

    def exists(self, targetReaction: WebElement) -> bool:
        for react in self.__REACT_STACK_.keys():
            if self.__REACT_STACK_[react] == targetReaction:
                return True
        return False

    def add(self, targetReaction: WebElement) -> bool:
        if not self.exists(targetReaction=targetReaction):
            self.__AUTOID += 1
            self.__REACT_STACK_[self.__AUTOID] = targetReaction
            __logger__.Print(0, __levels__.Success, __texts__.getText(8).format(str(targetReaction)))
            return True
        return False

    def remove(self, targetReaction: WebElement) -> bool:
        for react in self.__REACT_STACK_.keys():
            if self.__REACT_STACK_[react] == targetReaction:
                del self.__REACT_STACK_[react]
                __logger__.Print(0, __levels__.Success, __texts__.getText(9).format(str(targetReaction)))
                return True
        return False
