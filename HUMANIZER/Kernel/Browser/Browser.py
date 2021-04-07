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
    __alive = False

    def __init__(self, tor=False, incognito=True, headless=False, cache_folder="", appMode: str = ""):
        self.__jsBundle = JsBundle(js_payloads_path=__localSettings__.JS_PAYLOADS_PATH)
        self.setBrowserSettings(BrowserSettingsTObject(tor=tor, incognito=incognito, headless=headless, cache_folder=cache_folder, appMode=appMode))
        self.buildBrowserConfig()
        self.buildChromeDriver()

        self.__noNavigator = HideNavigatorFlag(chromeDriver=self)
        self.__noHeadlessIndicator = HideHeadlessFlag(chromeDriver=self)
        self.__elements = Elements(chromeDriver=self)
        self.__features = Features(chromeDriver=self, jsBundle=self.__jsBundle)

    def setBrowserSettings(self, browserSettings: BrowserSettingsTObject):
        """
        :param browserSettings:
        :type browserSettings:
        :return:
        :rtype:
        """
        self.__browserSettingsTObject = browserSettings

    def getBrowserSettings(self) -> BrowserSettingsTObject:
        """
        :return BrowserSettingsTObject:
        :rtype BrowserSettingsTObject:
        """
        return self.__browserSettingsTObject

    def buildBrowserConfig(self) -> ChromeConfig:
        """
        :return ChromeConfig:
        :rtype ChromeConfig:
        """
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

    def execute_js(self, code: str, *args):
        if self.__chromeDriver is not None:
            return self.__chromeDriver.execute_script(code, args)
        return {}

    def execute_cdp(self, code, cmd_args):
        if self.__chromeDriver is not None:
            return self.__chromeDriver.execute_cdp_cmd(code, cmd_args)
        return {}

    def keepAlive(self):
        self.__alive = True
        while self.__alive:
            if not self.__alive:
                break
            pass

    def stopAlive(self):
        self.__alive = False

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

    # Elements API
    def input(self, target, value, searchType="css"):
        self.__elements.input(target, value, searchType)

    def click(self, target):
        self.__elements.click(target=target)

    # Features API
    def runMouseADHD(self):
        self.__features.runMouseADHD()

    def installTheme(self, theme_num: int):
        self.__features.installTheme(theme_num)


class Elements:
    def __init__(self, chromeDriver: Browser):
        self.__chromeDriver = chromeDriver

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
                self.__chromeDriver.getChromeDriver().find_element_by_css_selector(target)
                return True
            if searchType == 'xpath':
                self.__chromeDriver.getChromeDriver().find_element_by_css_selector(target)
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
            return self.__chromeDriver.getChromeDriver().find_elements_by_xpath(target)
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
            return self.__chromeDriver.getChromeDriver().find_element_by_css_selector(target)
        except NoSuchElementException:
            pass


class HideNavigatorFlag:

    def __init__(self, chromeDriver: Browser):
        self.__chromeDriver = chromeDriver
        self.exploit()

    def removeFlag(self):
        return self.__chromeDriver.execute_cdp(
            "Page.addScriptToEvaluateOnNewDocument",
            {
                "source":
                    """
                        Object.defineProperty(window, 'navigator', {
                        value: new Proxy(navigator, {
                        has: (target, key) => (key === 'webdriver' ? false : key in target),
                        get: (target, key) =>
                            key === 'webdriver'
                            ? undefined
                            : typeof target[key] === 'function'
                            ? target[key].bind(target)
                            : target[key]
                                })
                        });
                        console.log = console.dir = console.error = function(){}
                        """
            },
        )

    def exploit(self):
        self.removeFlag()


class HideHeadlessFlag:

    def __init__(self, chromeDriver: Browser):
        self.__chromeDriver = chromeDriver
        self.exploit()

    def __getUserAgent(self) -> str:
        return self.__chromeDriver.execute_js('return navigator.userAgent;')

    def __replaceHeadlessAgent(self):
        actualAgent = self.__getUserAgent().replace("HeadlessChrome", "Chrome").replace("headlessChrome", "Chrome")
        self.__chromeDriver.execute_cdp("Network.setUserAgentOverride", {"userAgent": actualAgent})
        return self.__getUserAgent()

    def exploit(self):
        self.__replaceHeadlessAgent()


class Features:
    def __init__(self, chromeDriver: Browser, jsBundle: JsBundle):
        self.__chromeDriver = chromeDriver
        self.__jsBundle = jsBundle

    def runMouseADHD(self):
        self.__chromeDriver.execute_js(self.__jsBundle.jsPackGet(Payloads.MouseADHD))

    def installTheme(self, theme_num: int):
        jsTheme = self.__jsBundle.jsPackGet(Payloads.Theme)
        self.__chromeDriver.execute_js(jsTheme.replace('"THEME_NUM;"', str(theme_num)))


class Payloads:
    MouseADHD = "MouseADHD",
    Theme = "Theme"


class Drivers(enum.Enum):
    ChromeDriver = 0
    FirefoxDriver = 1
