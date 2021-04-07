import time

from DAO.FacebookCreateAccountTObject import FacebookCreateAccountTObject
from Kernel.Global import __localSettings__, __logger__, __levels__
from Kernel.Browser.Browser import Browser
from Kernel.FileSystem.fSys import fSys


class CreateAccount:
    __hostAddress: str = "https://facebook.com"

    def __init__(self, profile_file):
        self.__account = FacebookCreateAccountTObject.TO(fSys().readfile(profile_file))
        self.__browser = Browser(incognito=False, appMode=self.__hostAddress)
        self.__browser.installTheme(2)

    def __enterData(self):
        payload = self.__browser.getJsBundle().jsPackGet("CreateFacebookAccount")
        payload = payload.replace("FIRSTNAME;", self.__account.FirstName).replace("LASTNAME;", self.__account.LastName)
        payload = payload.replace("EMAIL;", self.__account.Email).replace("PASSWORD;", self.__account.Password)
        payload = payload.replace("BIRTH_MONTH;", self.__account.BirthMonth).replace("BIRTH_DAY;", self.__account.BirthDay)
        payload = payload.replace("BIRTH_YEAR;", self.__account.BirthYear)
        if self.__account.Gender == "Male":
            payload = payload.replace("GENDER;", "1")
        else:
            payload = payload.replace("GENDER;", "2")

        self.__browser.execute_js(payload)

    def start(self):

        if self.__account.FirstName != "":
            self.__enterData()
            self.__browser.keepAlive()
        else:
            print("Not all fields are filled")
            return False
