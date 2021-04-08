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
from Kernel.FileSystem.fSys import fSys
from Kernel.Global import __localSettings__, __logger__, __levels__, __texts__


class Browser:
    __browserSettingsTObject: BrowserSettingsTObject
    __browserConfig: ChromeConfig
    __chromeDriver: webdriver.Chrome
    __jsBundle: JsBundle
    __alive = False

    def __init__(self, tor=False, incognito=True, headless=False, cache_folder="", appMode: str = "",
                 generateUserAgent: bool = False):
        self.__jsBundle = JsBundle(js_payloads_path=__localSettings__.JS_PAYLOADS_PATH)
        self.setBrowserSettings(
            BrowserSettingsTObject(tor=tor, incognito=incognito, headless=headless, cache_folder=cache_folder,
                                   appMode=appMode, generateUserAgent=generateUserAgent))
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

    def openNewTab(self, navigate: str = "", interval: int = 0):
        self.execute_js(f'window.open("{navigate}");')
        if interval > 0:
            time.sleep(interval)

    def closeTab(self, index: int):
        self.__chromeDriver.switch_to.window(self.__chromeDriver.window_handles[index])
        self.findByCss('body').send_keys(Keys.CONTROL + "W")

    def switchTab(self, index: int = 0):
        self.__chromeDriver.switch_to.window(self.__chromeDriver.window_handles[index])

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

    def takeScreenshot(self) -> str:
        filename = __localSettings__.YANDEX_CAPTCHA_DIR + fSys().generateRandomName() + '.png'
        self.__chromeDriver.save_screenshot(filename=filename)
        return filename




    # Elements API
    def input(self, target, value: str):
        """
        :param target:
        :type target:
        :param value:
        :type value:
        :return:
        :rtype:
        """
        self.__elements.input(target, value)

    def click(self, target):
        self.__elements.click(target=target)

    def findByCss(self, target) -> WebElement:
        return self.__elements.findByCss(target)

    def clickAndInput(self, target: WebElement, value: str = "", interval: int = 0):
        return self.__elements.clickAndInput(target=target, value=value, interval=interval)

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

    def input(self, target: WebElement, value) -> WebElement:
        """
        :param target:
        :type target:
        :param value:
        :type value:
        :return:
        :rtype:
        """
        if type(target) == WebElement:
            target.send_keys(value)
            self.__DEBUG(target=target, value=value)

        return target

    def click(self, target: WebElement) -> WebElement:
        """
        :param target:
        :type target:
        :param searchType:
        :type searchType:
        :return:
        :rtype:
        """
        if type(target) == WebElement:
            target.click()
            self.__DEBUG(target=target, value="")
        return target

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
            raise NoSuchElementException()

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
            raise NoSuchElementException()

    def getElementPosition(self, target: WebElement) -> dict:
        if type(target) == WebElement:
            return target.location
        return {"x": 0, "y": 0}

    def clickAndInput(self, target: WebElement, value: str = "", interval: int = 0):
        self.click(target=target)
        if interval > 0:
            time.sleep(interval)
        if len(value) > 0:
            self.input(target=target, value=value)
        return target

    def __DEBUG(self, target: WebElement, value: str) -> dict:
        identifier = self.__elementClosestIdentifier(target=target)
        elementTag = target.tag_name
        elementType = target.get_attribute('type')

        if target is not None:
            if value != "":
                if elementTag == "input" or elementTag == "textarea":
                    if elementType == "password":
                        value = self.passMask(value=value)
                    message = __texts__.getText(1).format(identifier, value)
                    return __logger__.Print(msg_num=0, level=__levels__.Info, message=message)
            else:
                message = __texts__.getText(2).format(identifier, elementTag)
                return __logger__.Print(msg_num=0, level=__levels__.Info, message=message)

        return {}

    def passMask(self, value, passSign: str = '*') -> str:
        passChars: str = ""
        for i in range(len(value)):
            passChars += passSign
        return passChars

    def __elementClosestIdentifier(self, target: WebElement) -> str:
        if type(target) == WebElement:
            if target.get_attribute('name') != '':
                return target.get_attribute('name')
            elif target.get_attribute('id') != '':
                return target.get_attribute('id')
            elif target.get_attribute('class') != '':
                return target.get_attribute('class')
            elif target.get_attribute('label') != '':
                return target.get_attribute('label')
            elif target.get_attribute('title') != '':
                return target.get_attribute('title')
            elif target.get_attribute('value') != '':
                return target.get_attribute('value')
            else:
                return target.tag_name
        else:
            return target.tag_name


class HideNavigatorFlag:

    def __init__(self, chromeDriver: Browser):
        """
        :param chromeDriver:
        :type chromeDriver:
        """
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
        """
        :param chromeDriver:
        :type chromeDriver:
        """
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
        """
        :param chromeDriver:
        :type chromeDriver:
        :param jsBundle:
        :type jsBundle:
        """
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
