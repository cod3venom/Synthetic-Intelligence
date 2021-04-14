from Kernel.Browser.Browser import Browser


class FriendsMutator:

    def __init__(self, chromedriver: Browser, target_userID: str):
        self.__browser = chromedriver
