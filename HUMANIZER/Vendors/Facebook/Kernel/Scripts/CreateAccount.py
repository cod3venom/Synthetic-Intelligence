import time

from selenium.webdriver.remote.webelement import WebElement

from DAO.FacebookCreateAccountTObject import FacebookCreateAccountTObject
from Kernel.Global import __localSettings__, __logger__, __levels__, __texts__
from Kernel.Browser.Browser import Browser
from Kernel.FileSystem.fSys import fSys


class CreateAccount:

    __hostAddress: str = "https://facebook.com"

    def __init__(self, profile_file):
        self.__account = FacebookCreateAccountTObject.TO(fSys().readfile(profile_file))
        self.__browser = Browser(incognito=False)
        self.__browser.ChromeDriver.navigate(self.__hostAddress)
        self.__browser.Features.installTheme(4)

    def __enterData(self):
        payload = self.__browser.JsBundle.jsPackGet("CreateFacebookAccount")
        openRegistrationModal = self.__browser.execute_js(payload)
        time.sleep(3)

        # Enter text data
        enterFirstname = self.__browser.Elements.clickAndInput(target=self.__browser.Elements.findElementByCss('input[name="firstname"]'), value=self.__account.FirstName, interval=2)
        enterLastname = self.__browser.Elements.clickAndInput(target=self.__browser.Elements.findElementByCss('input[name="lastname"]'), value=self.__account.LastName, interval=2)
        enterEmail = self.__browser.Elements.clickAndInput(target=self.__browser.Elements.findElementByCss('input[name="reg_email__"]'), value=self.__account.Email, interval=2,)
        confirmEmail = self.__browser.Elements.clickAndInput(target=self.__browser.Elements.findElementByCss('input[name="reg_email_confirmation__"]'), value=self.__account.Email, interval=2)
        enterPassword = self.__browser.Elements.clickAndInput(target=self.__browser.Elements.findElementByCss('input[name="reg_passwd__"]'), value=self.__account.Password, interval=2)

        # Handle <SELECT> attribute
        showMonthList = self.__browser.Elements.clickAndInput(target=self.__browser.Elements.findElementByCss('select[name="birthday_month"]'), interval=2)
        selectBirthMonth = self.__browser.Elements.clickAndInput(target=self.__browser.Elements.findElementByCss(f'option[value="{self.__account.BirthMonth}"]'), interval=2)
        showDaysList = self.__browser.Elements.clickAndInput(target=self.__browser.Elements.findElementByCss('select[name="birthday_day"]'), interval=2)
        selectBirthDay = self.__browser.Elements.clickAndInput(target=self.__browser.Elements.findElementByCss(f'option[value="{self.__account.BirthDay}"]'), interval=2)
        showYearsList = self.__browser.Elements.clickAndInput(target=self.__browser.Elements.findElementByCss('select[name="birthday_year"]'), interval=2)
        selectBirthYear = self.__browser.Elements.clickAndInput(target=self.__browser.Elements.findElementByCss(f'option[value="{self.__account.BirthYear}"]'), interval=2)
        selectGender: WebElement
        if self.__account.Gender == "Female":
            selectGender = self.__browser.Elements.clickAndInput(target=self.__browser.Elements.findElementByCss('input[type="radio"][value="1"]'), interval=2)
        else:
            selectGender = self.__browser.Elements.clickAndInput(target=self.__browser.Elements.findElementByCss('input[type="radio"][value="2"]'), interval=2)

        # submitForm = self.__browser.Elements.clickAndInput(target=self.__browser.Elements.findElementByCss('button[type="submit"][name="websubmit"]'), interval=2)

    def start(self):
        self.__enterData()
        self.__browser.keepAlive()
