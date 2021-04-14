import time

from Kernel.Context.Context import Context
from Kernel.DataOps.ArgParser import ArgParser
from Vendors.Facebook.Kernel.Detectors.AutoEmotions import dAutoEmotions
from Vendors.Facebook.Kernel.Detectors.dMayKnown import dMayKnown
import threading as thr

from Vendors.Facebook.Kernel.Detectors.dNotifications import dNotifications
from Vendors.Facebook.Kernel.Features.Auth.FbAuth import FbAuth


class HomePage:
    __ctx: Context
    __argParser = ArgParser()
    __argParser.sysArgvTOdict()
    __fbAuth: FbAuth

    def __init__(self, ctx: Context):
        self.__ctx = ctx
        self.d_mayKnown = dMayKnown(ctx=self.__ctx)
        self.d_notifications = dNotifications(ctx=self.__ctx)
        self.d_autoEmotions = dAutoEmotions(ctx=self.__ctx)

    def __doAuth(self) -> bool:
        if self.__argParser.keyExists(self.__ctx.constants.pEMAIL) and self.__argParser.keyExists(
                self.__ctx.constants.pPASSWORD):
            self.__fbAuth = FbAuth(email=self.__argParser.getValueOf(self.__ctx.constants.pEMAIL),
                                   password=self.__argParser.getValueOf(self.__ctx.constants.pPASSWORD))
            self.__fbAuth.doLogin()
            if self.__fbAuth.isLogged(5):
                self.__ctx.browser = self.__fbAuth.browser
                return True
        return False

    def initialize(self):

        if self.__doAuth():
            self.d_mayKnown.ON()
            if self.d_mayKnown.finish:
                t_Notifications = thr.Thread(target=self.__onNotification).start()
                t_AutoEmotions = thr.Thread(target=self.__onAutoEmotions).start()

    def __onNotification(self):
        self.d_notifications.ON()

    def __onMessage(self):
        pass

    def __onMayKnown_container(self):
        self.d_mayKnown.ON()

    def __onFriendRequest_container(self):
        pass

    def __onAutoEmotions(self):
        self.d_autoEmotions.ON()
