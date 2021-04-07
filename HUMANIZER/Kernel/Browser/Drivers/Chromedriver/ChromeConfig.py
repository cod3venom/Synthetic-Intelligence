from selenium.webdriver.chrome.options import Options
from DAO.BrowserSettingsTObject import BrowserSettingsTObject
from Kernel.Browser.Exceptions import Exceptions


class ChromeConfig:

    def __init__(self, browserSettingsTObject: BrowserSettingsTObject):
        self.browserSettingsTObject = browserSettingsTObject
        self.exceptions = Exceptions()

    def getOptions(self):
        if self.browserSettingsTObject is None:
            raise self.exceptions.exChromeConfigIsEmpty()

        option = Options()
        option.add_argument('--disable-dev-shm-usage')
        option.add_argument('--disable-extensions')
        option.add_experimental_option("excludeSwitches", ["enable-automation"])
        option.add_argument("--disable-blink-features=AutomationControlled")

        if self.browserSettingsTObject.incognito:
            # Enable incognito mode
            option.add_argument('--incognito')

        if len(self.browserSettingsTObject.cache_folder) > 3:
            # Allow caching browser data
            option.add_argument('--user-data={}'.format(self.browserSettingsTObject.cache_folder))

        if len(self.browserSettingsTObject.appMode) > 3:
            option.add_argument("--app="+self.browserSettingsTObject.appMode)
        if self.browserSettingsTObject.tor == 1:
            # Use tor onions
            option.add_argument('--proxy-server=socks5://127.0.0.1:9050')
            option.add_argument('ignore-certificate-errors')

        if self.browserSettingsTObject.headless:
            # Use headless browser
            option.headless = True
            option.add_argument('disable-gpu')
        else:
            # Set browser window size
            option.add_argument('window-size=1700,1500')

        return option
