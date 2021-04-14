from selenium.webdriver.remote.webelement import WebElement
from Kernel.Context.Context import Context


class ProposedFriends:
    __ctx: Context
    __proposedContainer: str = 'div[aria-label="People You May Know"]'

    def __init__(self, ctx: Context):
        self.__ctx = ctx

    def execute(self, ):
        self.__ctx.browser.Javascript.scrollHVkey(interval=20)
        self.__ctx.browser.Javascript.execute_bundleJS(codeName="Jquery")
        flag = self.__ctx.browser.Elements.findElementByCss(self.__proposedContainer)

        if type(flag) == WebElement:
            self.__ctx.browser.Javascript.scrollToElement(self.__proposedContainer)
            self.__ctx.browser.Javascript.execute_bundleJS('FB_peopleMayKnown')
