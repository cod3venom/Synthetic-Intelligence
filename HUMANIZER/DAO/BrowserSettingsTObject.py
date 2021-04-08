from Kernel.DataOps.StringBuilder import StringBuilder
from Kernel.Global import __levels__, __logger__


class BrowserSettingsTObject:

    def __init__(self, tor: bool = False, incognito: bool = False, headless: bool = False, cache_folder: str = "",
                 appMode: str = "", generateUserAgent: bool = False):
        """
        Just initialize some chromedriver options variables to customize browser startup
        :param tor
        :param incognito:
        :param headless:
        :param cache_folder:
        """
        self.tor = tor
        self.incognito = incognito
        self.headless = headless
        self.cache_folder = cache_folder
        self.appMode = appMode
        self.generateUserAgent = generateUserAgent
        __logger__.Print(0, __levels__.Info, self.__str__())

    def __str__(self):
        return self.repr()

    def repr(self):
        buffer = StringBuilder()
        buffer.append("<BrowserSettingsTObject:")
        buffer.append(" TOR= " + str(self.tor))
        buffer.append(", INCOGNITO= " + str(self.incognito))
        buffer.append(", HEADLESS= " + str(self.headless))
        buffer.append(", CACHE FOLDER= " + self.cache_folder)
        buffer.append(" APP MODE= " + self.appMode)
        buffer.append(">")
        return buffer.string
