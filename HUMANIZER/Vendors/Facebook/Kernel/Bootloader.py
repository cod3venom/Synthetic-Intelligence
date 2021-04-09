from Kernel.Browser.Browser import Browser
import threading as thr

from Vendors.Facebook.Kernel.Features.Detectors.PostDetector import PostDetector


class BootLoader:

    def __init__(self, isLogged: bool, browser: Browser):
        self.isLogged = isLogged
        self.__browser = browser
        if isLogged:
            self.__ruleOwnLife()

    def __ruleOwnLife(self):
        self.__autoDetection()

    def __autoDetection(self):
        keepAlive = thr.Thread(target=self.__browser.keepAlive).start()
        postDetector = PostDetector(chromedriver=self.__browser)
        postDetectionThread = thr.Thread(target=postDetector.execute)
        postDetectionThread.start()

    def __autoLikes(self):
        pass
