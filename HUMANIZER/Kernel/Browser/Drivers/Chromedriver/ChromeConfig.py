from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.chrome.options import Options
from DAO.ChromeDriverSettingsTObject import ChromeDriverSettingsTObject
from Kernel.Browser.Exceptions import Exceptions
from Kernel.Cheater.AgencyFactory import AgencyFactory


class ChromeConfig:

    def __init__(self, browserSettingsTObject: ChromeDriverSettingsTObject):
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
            option.add_argument("--app=" + self.browserSettingsTObject.appMode)
        if self.browserSettingsTObject.tor == 1:
            # Use tor onions
            option.add_argument('--proxy-server=socks5://127.0.0.1:9050')
            option.add_argument('ignore-certificate-errors')

        if self.browserSettingsTObject.generateUserAgent:
            option.add_argument(f'user-agent={AgencyFactory().getNewAgent}')
        if self.browserSettingsTObject.disablePasswordService:
            passwordPreferences = {"credentials_enable_service": False, "profile.password_manager_enabled": False}
            option.add_experimental_option("prefs", passwordPreferences)

        if self.browserSettingsTObject.headless:
            # Use headless browser
            option.headless = True
            option.add_argument('disable-gpu')
        else:
            # Set browser window size
            option.add_argument('window-size=1700,1500')
            # option.add_argument('--kiosk')

        return option

    def getCapabilities(self) -> DesiredCapabilities:
        desiredCapabilities = DesiredCapabilities.CHROME
        desiredCapabilities['loggingPrefs'] = {'browser': 'ALL'}
        return desiredCapabilities
