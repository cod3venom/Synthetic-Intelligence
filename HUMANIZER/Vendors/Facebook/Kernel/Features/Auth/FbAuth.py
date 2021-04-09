import time

from DAO.ChromeDriverSettingsTObject import ChromeDriverSettingsTObject
from Kernel.Browser.Browser import Browser
from Vendors.Facebook.DAO.FacebookCookiesTObject import FacebookCookiesTObject
from Vendors.Facebook.DAO.FacebookCredentialsTObject import FacebookCredentialsTObject
from Vendors.Facebook.Kernel.Features.Modals.CookiesModal import CookiesModal


class FbAuth:
    __mainPage = 'https://facebook.com'
    __mainMobilePage = 'https://m.facebook.com'
    __chromeSettingsTObject = ChromeDriverSettingsTObject(incognito=True, generateUserAgent=True)
    browser = Browser(chromeDriverSettingsTObject=__chromeSettingsTObject)
    __cookieModal = CookiesModal(browser=browser)

    __emailInputSelector = 'input[name="email"]'
    __passwordInputSelector = 'input[type="password"][name="pass"]'
    __submitButtonSelector = 'button[type="submit"][name="login"]'

    __cookiesTObject: FacebookCookiesTObject
    __cUser: str = 'c_user'

    def __init__(self, email: str, password: str, isMobile: bool = False):
        """
        :param email:
        :type email:
        :param password:
        :type password:
        """
        self.fbCredentials = FacebookCredentialsTObject(USERNAME=email, PASSWORD=password)
        self.isMobile = isMobile
        self.__preAuthActions()

    def isLogged(self, interval: int = 0) -> bool:
        if interval > 0:
            time.sleep(interval)
        cookieData = self.browser.Cookies.loadCookies()
        for cookie in cookieData:
            if type(cookie) == dict:
                if self.__cUser in str(cookie):
                    self.__cookiesTObject = FacebookCookiesTObject(name=cookie['name'], value=cookie['value'])
                    if self.__cookiesTObject.name == self.__cUser:
                        if len(self.__cookiesTObject.value) > 5:
                            return True
        return False

    def __openMainPage(self, keepAlive: bool = True) -> int:
        if self.isMobile:
            self.browser.ChromeDriver.navigate(self.__mainMobilePage)
            return 0  # is mobile version
        else:
            self.browser.ChromeDriver.navigate(self.__mainPage)
        return 1  # is pc version

    def __preAuthActions(self):
        self.__openMainPage()
        self.__cookieModal.accept()

    def doLogin(self) -> bool:
        if not self.isLogged():
            enterEmail = self.browser.Elements.clickAndInput(self.browser.Elements.findByCss(self.__emailInputSelector), value=self.fbCredentials.username, interval=1)
            enterPassword = self.browser.Elements.clickAndInput(self.browser.Elements.findByCss(self.__passwordInputSelector), value=self.fbCredentials.password, interval=2)
            clickLogin = self.browser.Elements.clickAndInput(self.browser.Elements.findByCss(self.__submitButtonSelector), interval=2)
        return self.isLogged()

