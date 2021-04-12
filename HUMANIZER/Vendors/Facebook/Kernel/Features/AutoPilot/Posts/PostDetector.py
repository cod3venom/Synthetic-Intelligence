from Vendors.Facebook.Kernel.globals import __DETECTED_POSTS__
from Kernel.Global import __texts__, __levels__, __logger__
from selenium.webdriver.remote.webelement import WebElement
from Kernel.Browser.Browser import Browser

# POST SELECTORS
"""
    MAIN CONTAINER = //div[@role="feed"]
    POST CONTAINER = //div[@role="feed"]/div[contains(@data-pagelet, "FeedUnit")]

"""


class PostDetector:
    __defaultPostSelector: str = '//div[@role="feed"]/div[contains(@data-pagelet, "FeedUnit")]'
    __restartTime = 30000

    def __init__(self, chromedriver: Browser):
        self.__browser = chromedriver
        self.__postStack = PostStack()

    def execute(self):

        posts = self.__browser.Elements.findElementsByXpath('//a')
        link: WebElement
        for link in posts:
            print(f"LINKS > {str(link.get_attribute('href'))}\r\n")
        return []
            # print(__DETECTED_POSTS__)


class PostStack:
    __AUTOID: int = 0

    def exists(self, targetPost: WebElement) -> bool:
        for postKey in __DETECTED_POSTS__.keys():
            if __DETECTED_POSTS__[postKey] == targetPost:
                return True
        return False

    def add(self, targetPost: WebElement) -> bool:
        if not self.exists(targetPost=targetPost):
            self.__AUTOID += 1
            __DETECTED_POSTS__[self.__AUTOID] = targetPost
            __logger__.Print(0, __levels__.Success, __texts__.getText(6).format(str(targetPost)))
            return True
        return False

    def remove(self, targetPost: WebElement) -> bool:
        for postKey in __DETECTED_POSTS__.keys():
            if __DETECTED_POSTS__[postKey] == targetPost:
                del __DETECTED_POSTS__[postKey]
                __logger__.Print(0, __levels__.Success, __texts__.getText(7).format(str(targetPost)))
                return True
        return False
