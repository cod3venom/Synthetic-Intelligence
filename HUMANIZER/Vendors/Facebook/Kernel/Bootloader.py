from Kernel.Browser.Browser import Browser
import threading as thr

from Vendors.Facebook.Kernel.Features.AutoPilot.AutoEmotions.AutoEmotions import AutoEmotions
from Vendors.Facebook.Kernel.Features.AutoPilot.MayKnownDetector.ProposedFriends import ProposedFriends


class BootLoader:

    def __init__(self, isLogged: bool, browser: Browser):
        self.isLogged = isLogged
        self.__browser = browser
        if isLogged:
            self.__ruleOwnLife()

    def __ruleOwnLife(self):
        keepAlive = thr.Thread(target=self.__browser.keepAlive).start()
        ProposedFriends(chromedriver=self.__browser).execute()

        autoEmotions = AutoEmotions(chromedriver=self.__browser)
        while self.__browser.alive:
            autoEmotions.execute()
