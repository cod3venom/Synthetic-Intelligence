from selenium.webdriver.remote.webelement import WebElement

from Kernel.Browser.Browser import Browser


class CookiesModal:
    __modalMainContainer = 'div[data-testid="cookie-policy-dialog"]'
    __modalAcceptButton = 'button[title="Accept All"]'

    def __init__(self, browser: Browser):
        self.__browser = browser

    @property
    def isModalAppears(self) -> bool:
        return self.__browser.Elements.exists(self.__modalMainContainer)

    @property
    def modal(self) -> WebElement:
        return self.__browser.Elements.findByCss(self.__modalMainContainer)

    def accept(self) -> WebElement:
        if self.isModalAppears:
            return self.__browser.Elements.click(target=self.__browser.Elements.findByCss(self.__modalAcceptButton))

    def decline(self) -> bool:
        if self.isModalAppears:
            self.modal.clear()
            return True
        return False
