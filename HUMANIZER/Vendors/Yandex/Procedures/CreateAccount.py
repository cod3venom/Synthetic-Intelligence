import time

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
        self.__browser = Browser(incognito=True, appMode=self.__hostAddress)

    def __enterData(self) -> str:
        payload = self.__browser.getJsBundle().jsPackGet("CreateYandexMailAccount")
        payload = payload.replace("FIRSTNAME;", self.__account.FirstName)
        payload = payload.replace("LASTNAME;", self.__account.LastName)
        payload = payload.replace("USERNAME;", self.__account.UserName)
        payload = payload.replace("PASSWORD;", self.__account.Password)
        payload += '''  return getCaptcha(runProcedure()).then(function(src){ return src; }); '''
        return self.__browser.getChromeDriver().execute_script(payload)  # Returns url address of captcha image

    def start(self):
        if self.__account.FirstName != "":
            captchaURL = self.__enterData()
            noCaptcha = NoCaptcha(captchaURL)
            noCaptcha.parseText()

            self.__browser.alive = True
            self.__browser.keepAlive()
        else:
            print("Not all fields are filled")
            return False
