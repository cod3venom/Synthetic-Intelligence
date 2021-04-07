import enum
import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webelement import WebElement

from DAO.BrowserSettingsTObject import BrowserSettingsTObject
from Kernel.Browser.Drivers.Chromedriver.ChromeConfig import ChromeConfig
from Kernel.Browser.Hacking.JsBundle import JsBundle
from Kernel.Global import __localSettings__, __logger__


class Browser:
    __browserSettingsTObject: BrowserSettingsTObject
    __browserConfig: ChromeConfig
    __chromeDriver: webdriver.Chrome
    __jsBundle: JsBundle
    alive = False

    def __init__(self, tor=False, incognito=True, headless=False, cache_folder=""):
        self.__jsBundle = JsBundle(js_payloads_path=__localSettings__.JS_PAYLOADS_PATH)
        self.buildBrowserSettings(tor=tor, incognito=incognito, headless=headless, cache_folder=cache_folder)
        self.buildBrowserConfig()
        self.buildChromeDriver()

    def buildBrowserSettings(self, tor=False, incognito=True, headless=False,
                             cache_folder="") -> BrowserSettingsTObject:
        self.setBrowserSettings(BrowserSettingsTObject(tor=False, incognito=True, headless=False, cache_folder=""))
        return self.getBrowserSettings()

    def setBrowserSettings(self, browserSettings: BrowserSettingsTObject):
        self.__browserSettingsTObject = browserSettings

    def getBrowserSettings(self) -> BrowserSettingsTObject:
        return self.__browserSettingsTObject

    def buildBrowserConfig(self) -> ChromeConfig:
        self.__browserConfig = ChromeConfig(self.getBrowserSettings())
        return self.getBrowserConfig()

    def setBrowserConfig(self, browserConfig: ChromeConfig):
        self.__browserConfig = browserConfig

    def getBrowserConfig(self) -> ChromeConfig:
        return self.__browserConfig

    def setChromedriver(self, chromeDriver):
        self.__chromeDriver = chromeDriver

    def getChromeDriver(self) -> webdriver.Chrome:
        return self.__chromeDriver

    def buildChromeDriver(self) -> webdriver.Chrome:
        self.__chromeDriver = webdriver.Chrome(executable_path=__localSettings__.BINARY_PATH,
                                               chrome_options=self.__browserConfig.getOptions())
        return self.getBrowser()

    def setBrowser(self, chromeDriver: webdriver.Chrome):
        self.__chromeDriver = chromeDriver

    def getBrowser(self) -> webdriver.Chrome:
        return self.__chromeDriver

    def getSource(self):
        return self.__chromeDriver.page_source

    def getJsBundle(self) -> JsBundle:
        return self.__jsBundle

    def keepAlive(self):
        while self.alive:
            if not self.alive:
                break
            pass

    def navigate(self, navigate_to: str, invoke_adhd: bool = False, keep_alive: bool = False):
        """
        Navigate to certain web site address
        :param keep_alive:
        :type keep_alive:
        :param navigate_to:
        :type navigate_to:
        :param invoke_adhd:
        :type invoke_adhd:
        :return:
        :rtype:
        """
        self.__chromeDriver.get(navigate_to)
        if invoke_adhd:
            self.runMouseADHD()
        if keep_alive:
            while True:
                pass

    def Exists(self, target, searchType="css"):
        """
        Check if element exists
        :param target:
        :type target:
        :param searchType:
        :type searchType:
        :return:
        :rtype:
        """
        time.sleep(.4)
        try:
            if searchType == 'css':
                self.__chromeDriver.find_element_by_css_selector(target)
                return True
            if searchType == 'xpath':
                self.__chromeDriver.find_element_by_css_selector(target)
                return True
            return False
        except NoSuchElementException:
            return False

    def input(self, target, value, searchType="css"):
        """
        Input text into element
        :param target:
        :type target:
        :param value:
        :type value:
        :param searchType:
        :type searchType:
        :return:
        :rtype:
        """
        entered = False
        if self.Exists(target, searchType):
            self.findByCss(target).send_keys(value)

    def click(self, target, searchType="css"):
        """
        Click on element
        :param target:
        :type target:
        :param searchType:
        :type searchType:
        :return:
        :rtype:
        """
        if self.Exists(target, searchType):
            self.findByCss(target).send_keys(Keys.RETURN)

    def findByXpath(self, target) -> list:
        """
        Find element by xpath selector
        :param target:
        :type target:
        :return:
        :rtype:
        """
        try:
            return self.__chromeDriver.find_elements_by_xpath(target)
        except NoSuchElementException:
            pass

    def findByCss(self, target) -> WebElement:
        """
        Find element by css selector
        :param target:
        :type target:
        :return:
        :rtype:
        """
        try:
            return self.__chromeDriver.find_element_by_css_selector(target)
        except NoSuchElementException:
            pass

    def execute_js(self, code: str) -> dict:
        if self.__chromeDriver is not None:
            return self.__chromeDriver.execute_script(code)
        return {}

    def execute_cdp(self, code):
        if self.__chromeDriver is not None:
            return self.__chromeDriver.execute_cdp_cmd(code, "")
        return {}

    def runMouseADHD(self):
        self.execute_js(self.__jsBundle.jsPackGet(Payloads.MouseADHD))

    def installTheme(self, theme_num: int):
        jsTheme = self.__jsBundle.jsPackGet(Payloads.Theme)
        self.execute_js(jsTheme.replace('"THEME_NUM;"', str(theme_num)))


class Payloads:
    MouseADHD = "MouseADHD",
    Theme = "Theme"


class Drivers(enum.Enum):
    ChromeDriver = 0
    FirefoxDriver = 1
