import random
import time

from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException, \
    ElementNotInteractableException, ElementClickInterceptedException
from selenium.webdriver.remote.webelement import WebElement
from Kernel.Global import __texts__, __levels__, __logger__
from Kernel.Browser.Browser import Browser

# XPATH SELECTORS
"""
    DETECT PROPOSED FRIENDS = //span[text()="People You May Know"]
    GET ADD BUTTONS = //span[text()="Add Friend"]
"""


class ProposedFriends:
    __proposedContainer: str = '//span[text()="People You May Know"]'

    def __init__(self, chromedriver: Browser):
        self.__browser = chromedriver

    def execute(self,):
        self.__browser.Javascript.scrollToElement('''div[data-pagelet="FeedUnit_{n}"]''')

        flag = self.__browser.Elements.findElementByXpath(self.__proposedContainer)
        if type(flag) == WebElement:
            self.__browser.Javascript.scrollToElement('div[aria-label="People You May Know"]')
            self.__browser.Javascript.execute_bundleJS('FacebookGetProposedPeopleContainer')
        time.sleep(5)


