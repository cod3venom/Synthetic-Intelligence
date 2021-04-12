import enum
import sys
import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webelement import WebElement

from DAO.ChromeDriverSettingsTObject import ChromeDriverSettingsTObject
from Kernel.Browser.Drivers.Chromedriver.ChromeConfig import ChromeConfig
from Kernel.Browser.Hacking.JsBundle import JsBundle
from Kernel.FileSystem.fSys import fSys
from Kernel.Global import __localSettings__, __logger__, __levels__, __texts__


class Browser:
    alive = False

    def __init__(self, chromeDriverSettingsTObject: ChromeDriverSettingsTObject = None):
        self.__chromeDriver = ChromeDriver(settingsTObject=chromeDriverSettingsTObject)
        self.__jsBundle = JsBundle(js_payloads_path=__localSettings__.JS_PAYLOADS_PATH)
        self.__javascript = Javascript(_browser=self)

        self.__elements = Elements(_browser=self)
        self.__features = Features(_browser=self)
        self.__cookies = Cookies(_browser=self)

        self.__noNavigator = HideNavigatorFlag(_browser=self)
        self.__noHeadlessIndicator = HideHeadlessFlag(_browser=self)

    def keepAlive(self):
        self.alive = True
        while self.alive:
            if not self.alive:
                break
            pass

    def stopAlive(self):
        self.alive = False

    def openNewTab(self, navigate: str = "", interval: int = 0):
        self.Javascript.execute_js(f'window.open("{navigate}");')
        if interval > 0:
            time.sleep(interval)

    @property
    def ChromeDriver(self):
        return self.__chromeDriver

    @property
    def JsBundle(self):
        return self.__jsBundle

    @property
    def Elements(self):
        return self.__elements

    @property
    def Features(self):
        return self.__features

    @property
    def Cookies(self):
        return self.__cookies

    @property
    def Javascript(self):
        return self.__javascript


class ChromeDriver:
    __chromeDriver: webdriver.Chrome

    def __init__(self, settingsTObject: ChromeDriverSettingsTObject):
        if settingsTObject is None:
            settingsTObject = ChromeDriverSettingsTObject(incognito=True)
        self.__browserConfig = ChromeConfig(browserSettingsTObject=settingsTObject)
        self.buildChromeDriver()

    def buildChromeDriver(self) -> webdriver.Chrome:
        self.__chromeDriver = webdriver.Chrome(executable_path=__localSettings__.BINARY_PATH, chrome_options=self.__browserConfig.getOptions())
        return self.chromeDriver

    def navigate(self, navigate_to: str):
        self.__chromeDriver.get(navigate_to)

    @property
    def chromeDriver(self) -> webdriver.Chrome:
        return self.__chromeDriver

    def closeTab(self, index: int):
        self.chromeDriver.switch_to.window(self.chromeDriver.window_handles[index])
        self.chromeDriver.find_element_by_css_selector('body').send_keys(Keys.CONTROL + "W")

    def switchTab(self, index: int = 0):
        self.chromeDriver.switch_to.window(self.chromeDriver.window_handles[index])

    def takeScreenshot(self) -> str:
        filename = __localSettings__.YANDEX_CAPTCHA_DIR + fSys().generateRandomName() + '.png'
        self.chromeDriver.save_screenshot(filename=filename)
        return filename

    def consoleDebug(self):
        for entry in self.__chromeDriver.get_log('browser'):
            __logger__.Print(0, __levels__.Info, entry)


class Javascript:

    def __init__(self, _browser: Browser):
        self.__browser = _browser

    def scrollToElement(self, selector: str):
        return self.execute_js(self.__browser.JsBundle.jsPackGet('ScrollToElement').replace('SELECTOR;', f"{selector}"),
                               interval=1)

    def querySelectorAll(self, selector: str):
        code = self.__browser.JsBundle.jsPackGet('querySelectorAll').replace('SELECTOR;',
                                                                             f"{selector}") + "return querySelectorAll();"
        return self.execute_js(code=code)

    def execute_bundleJS(self, codeName: str, interval: int = 0):
        if self.__browser is not None:
            code = self.__browser.JsBundle.jsPackGet(codeName)
            retCode = self.execute_js(code=code, interval=interval)
            self.__browser.ChromeDriver.consoleDebug()
            return retCode

    def execute_js(self, code: str, *args, interval: int = 0):
        try:
            if self.__browser is not None:
                retCode = self.__browser.ChromeDriver.chromeDriver.execute_script(code, args)
                self.__browser.ChromeDriver.consoleDebug()
                if interval > 0:
                    time.sleep(interval)
                return retCode
            return {}
        except StaleElementReferenceException:
            return {}

    def execute_cdp(self, code, cmd_args):
        if self.__browser is not None:
            retCode = self.__browser.ChromeDriver.chromeDriver.execute_cdp_cmd(code, cmd_args)
            self.__browser.ChromeDriver.consoleDebug()
            return retCode
        return {}


class Elements:
    def __init__(self, _browser: Browser):
        self.__browser = _browser

    def exists(self, target) -> bool:
        time.sleep(.4)
        try:
            self.__browser.ChromeDriver.chromeDriver.find_element_by_css_selector(target)
            return True
        except NoSuchElementException:
            return False

    def input(self, target: WebElement, value) -> WebElement:
        if type(target) == WebElement:
            target.send_keys(value)
            self.__DEBUG(target=target, value=value)

        return target

    def click(self, target: WebElement) -> WebElement:
        if type(target) == WebElement:
            target.click()
            self.__DEBUG(target=target, value="")
        return target

    def findElementByCss(self, target) -> WebElement:
        try:
            return self.__browser.ChromeDriver.chromeDriver.find_element_by_css_selector(target)
        except NoSuchElementException:
            raise NoSuchElementException()

    def findElementsByCss(self, target) -> WebElement:
        try:
            return self.__browser.ChromeDriver.chromeDriver.find_elements_by_css_selector(target)
        except NoSuchElementException:
            raise NoSuchElementException()

    def findElementByXpath(self, target) -> WebElement:
        try:
            return self.__browser.ChromeDriver.chromeDriver.find_element_by_xpath(target)
        except NoSuchElementException:
            return None

    def findElementsByXpath(self, target) -> WebElement:
        try:
            return self.__browser.ChromeDriver.chromeDriver.find_elements_by_xpath(target)
        except NoSuchElementException:
            raise NoSuchElementException()

    def getElementPosition(self, target: WebElement) -> dict:
        if type(target) == WebElement:
            return target.location
        return {"x": 0, "y": 0}

    def setAttribute(self, target: WebElement, name: str, value: str = ""):
        self.__browser.ChromeDriver.chromeDriver.execute_script(f"arguments[0].setAttribute('{name}','{value}')",
                                                                target)

    def getAttribute(self, target: WebElement, name: str):
        return self.__browser.ChromeDriver.chromeDriver.execute_script(f"arguments[0].getAttribute('{name}')", target)

    def clickAndInput(self, target: WebElement, value: str = "", interval: int = 0):
        self.click(target=target)
        if interval > 0:
            time.sleep(interval)
        if len(value) > 0:
            self.input(target=target, value=value)
        return target

    def __DEBUG(self, target: WebElement, value: str) -> dict:
        try:
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
        except StaleElementReferenceException:
            return {}

    def passMask(self, value, passSign: str = '*') -> str:
        passChars: str = ""
        for i in range(len(value)):
            passChars += passSign
        return passChars

    def __elementClosestIdentifier(self, target: WebElement) -> str:
        try:
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
        except StaleElementReferenceException:
            return "ELEMENT WAS REMOVED"


class Cookies:

    def __init__(self, _browser: Browser):
        self.__browser = _browser

    def loadCookies(self) -> dict:
        return self.__browser.ChromeDriver.chromeDriver.get_cookies()

    def getCookieByName(self, name: str):
        return self.__browser.ChromeDriver.chromeDriver.get_cookie(name=name)


class HideNavigatorFlag:

    def __init__(self, _browser: Browser):
        """
        :param _browser:
        :type _browser:
        """
        self.__browser = _browser
        self.exploit()

    def removeFlag(self):
        return self.__browser.Javascript.execute_cdp(
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

    def __init__(self, _browser: Browser):
        """
        :param _browser:
        :type _browser:
        """
        self.__browser = _browser
        self.exploit()

    def __getUserAgent(self) -> str:
        return self.__browser.Javascript.execute_js('return navigator.userAgent;')

    def __replaceHeadlessAgent(self):
        actualAgent = self.__getUserAgent().replace("HeadlessChrome", "Chrome").replace("headlessChrome", "Chrome")
        self.__browser.Javascript.execute_cdp("Network.setUserAgentOverride", {"userAgent": actualAgent})
        return self.__getUserAgent()

    def exploit(self):
        self.__replaceHeadlessAgent()


class Features:
    def __init__(self, _browser: Browser):
        self.__browser = _browser

    def runMouseADHD(self):
        self.__browser.Javascript.execute_js(self.__browser.JsBundle.jsPackGet(Payloads.MouseADHD))

    def installTheme(self, theme_num: int):
        jsTheme = self.__browser.JsBundle.jsPackGet(Payloads.Theme)
        self.__browser.Javascript.execute_js(jsTheme.replace('"THEME_NUM;"', str(theme_num)))


class BrowserExceptions:
    pass


class Payloads:
    MouseADHD = "MouseADHD",
    Theme = "Theme"


class Drivers(enum.Enum):
    ChromeDriver = 0
    FirefoxDriver = 1
