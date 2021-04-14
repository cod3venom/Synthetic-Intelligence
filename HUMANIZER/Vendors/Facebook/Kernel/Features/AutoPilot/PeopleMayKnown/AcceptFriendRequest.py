from selenium.webdriver.remote.webelement import WebElement
from Kernel.Context.Context import Context


class AcceptFriendsRequest:
    __ctx: Context
    __requestContainer: str = 'div[aria-label="Friend Requests"]'

    def __init__(self, ctx: Context):
        self.__ctx = ctx

    def execute(self):
        self.__ctx.browser.Javascript.scrollHVkey(interval=20)
        self.__ctx.browser.Javascript.execute_bundleJS(codeName="Jquery")
        flag = self.__ctx.browser.Elements.findElementByCss(self.__requestContainer)

        if type(flag) == WebElement:
            self.__ctx.browser.Javascript.scrollToElement(self.__requestContainer)
            self.__ctx.browser.Javascript.execute_bundleJS('FacebookGetProposedPeopleContainer')
