import time
from selenium.webdriver.remote.webelement import WebElement
from DAO.ChromeDriverSettingsTObject import ChromeDriverSettingsTObject
from DAO.FacebookCreateAccountTObject import FacebookCreateAccountTObject
from Kernel.Global import __localSettings__
from Kernel.Browser.Browser import Browser
from Kernel.FileSystem.fSys import fSys


class CreateAccount:

    def __init__(self, chromedriver: Browser, profile_file: str):
        self.__account = FacebookCreateAccountTObject.TO(fSys().readfile(profile_file))
        self.__browser = chromedriver
        self.__browser.ChromeDriver.navigate(__localSettings__.FB_HOME_PC)

    def __enterData(self):
        openRegistrationModal = self.__browser.Javascript.execute_bundleJS("CreateFacebookAccount")
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
