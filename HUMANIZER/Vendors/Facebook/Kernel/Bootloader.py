import sys

from Kernel.Browser.Browser import Browser
import threading as thr

from Kernel.Browser.Drivers.Chromedriver.Profiles import Profiles
from Kernel.Context.Context import Context
from Kernel.DataOps.ArgParser import ArgParser
from Vendors.Facebook.Kernel.Features.Auth.FbAuth import FbAuth
from Vendors.Facebook.Kernel.Features.AutoPilot.AutoEmotions.AutoEmotions import AutoEmotions
from Vendors.Facebook.Kernel.Features.AutoPilot.PeopleMayKnown.AcceptFriendRequest import AcceptFriendsRequest
from Vendors.Facebook.Kernel.Features.AutoPilot.PeopleMayKnown.ProposedFriends import ProposedFriends
from Vendors.Facebook.Kernel.Features.mkAccont.CreateAccount import CreateAccount


class BootLoader:
    __ctx = Context()

    def __init__(self):
        self.__Load()

    def __Load(self):
        argParser = ArgParser()
        argParser.sysArgvTOdict()

        if argParser.keyEquals(self.__ctx.constants.pFACEBOOK, "True"):
            if argParser.keyEquals(self.__ctx.constants.pCREATE_ACCOUNT, "True"):
                self.run_createFbAccount()

            if argParser.keyExists(self.__ctx.constants.pEMAIL) and argParser.keyExists(self.__ctx.constants.pPASSWORD):
                fbAuth = FbAuth(argParser.getValueOf(self.__ctx.constants.pEMAIL),
                                password=argParser.getValueOf(self.__ctx.constants.pPASSWORD))
                fbAuth.doLogin()
                self.__ctx.browser = fbAuth.browser

                if argParser.keyExists(self.__ctx.constants.pAUTO_EMOTIONS):
                    self.run_fbAutoEmotions()
                if argParser.keyExists(self.__ctx.constants.pMAY_KNOWN_DETECTOR):
                    self.run_fbMayKnownDetector()
                if argParser.keyExists(self.__ctx.constants.pMAY_KNOWN_ACCEPT_REQUEST):
                    self.run_fbMayKnownAcceptRequest()

                if argParser.keyExists(self.__ctx.constants.pREALITY_ROUTINE):
                    self.run_realityRoutine()

                if argParser.keyExists(self.__ctx.constants.pKEEP_ALIVE):
                    self.keepAlive(keepAlive=True)

    def run_createFbAccount(self):
        profile = Profiles()
        browser = Browser(profile.default())
        return CreateAccount(chromedriver=browser, profile_file=sys.argv[3]).start()

    def run_fbAutoEmotions(self):
        while True:
            autoEmotions = AutoEmotions(ctx=self.__ctx)
            autoEmotions.execute()

    def run_fbMayKnownDetector(self):
        while True:
            proposedFriends = ProposedFriends(ctx=self.__ctx)
            proposedFriends.execute()

    def run_fbMayKnownAcceptRequest(self):
        while True:
            acceptFriendRequest = AcceptFriendsRequest(ctx=self.__ctx)
            acceptFriendRequest.execute()

    def run_realityRoutine(self):
        # tMayKnownAccept = thr.Thread(target=self.run_fbMayKnownAcceptRequest).start()

        self.run_fbMayKnownDetector()
        self.run_fbAutoEmotions()

    def keepAlive(self, keepAlive: bool = False):
        if keepAlive:
            self.__ctx.browser.keepAlive()
