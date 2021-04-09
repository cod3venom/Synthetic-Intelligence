import time

from selenium.common.exceptions import StaleElementReferenceException
from DAO.YandexCreateAccountTObject import YandexCreateAccountTObject
from Kernel.Global import __localSettings__, __logger__, __levels__
from Kernel.Browser.Browser import Browser
from Kernel.Browser.Hacking.NoCaptcha import NoCaptcha
from Kernel.FileSystem.fSys import fSys


class CreateAccount:
    __hostAddress: str = 'https://passport.yandex.ru/registration/mail?'
    __captchaImgAddress: str

    def __init__(self, profile_file):
        self.__account = YandexCreateAccountTObject.TO(fSys().readfile(profile_file))
        self.__browser = Browser(incognito=True, generateUserAgent=True)
        self.__browser.ChromeDriver.navigate(self.__hostAddress)

    def __removeLabelMasks(self):
        return self.__browser.execute_js('document.querySelectorAll("label").forEach(element => element.remove());')

    def __enterData(self):
        payload = self.__browser.JsBundle.jsPackGet("CreateYandexMailAccount")
        payload += '''  return getCaptcha(runProcedure()).then(function(src){ return src; }); '''
        self.__browser.execute_js(payload)

        captchaUrl = self.__browser.getChromeDriver().execute_script(payload)
        enterFirstName = self.__browser.Elements.clickAndInput(self.__browser.Elements.findByCss('input[name="firstname"]'), value=self.__account.FirstName, interval=1)
        enterLastname = self.__browser.Elements.clickAndInput(self.__browser.Elements.findByCss('input[name="lastname"]'), value=self.__account.LastName, interval=2)
        clickOnLogin = self.__browser.Elements.clickAndInput(self.__browser.Elements.findByCss('input[name="login"]'), value=self.__account.LastName, interval=2)
        enterPassword = self.__browser.Elements.clickAndInput(self.__browser.Elements.findByCss('input[name="password"]'), value=self.__account.Password, interval=2)
        enterPasswordConfirmation = self.__browser.Elements.clickAndInput(self.__browser.Elements.findByCss('input[name="password_confirm"]'), value=self.__account.Password, interval=2)
        enterSecurityQuestion = self.__browser.Elements.clickAndInput(self.__browser.Elements.findByCss('input[name="hint_answer"]'), value=self.__account.SecurityHint, interval=2)

        captchaCode = input('Enter captcha > ')
        enterCaptcha = self.__browser.Elements.clickAndInput(self.__browser.Elements.findByCss('input[name="captcha"]'), value=captchaCode, interval=2)

    def start(self):
        if self.__account.FirstName != "":
            self.__enterData()
            self.__browser.keepAlive()
        else:
            print("Not all fields are filled")
            return False
