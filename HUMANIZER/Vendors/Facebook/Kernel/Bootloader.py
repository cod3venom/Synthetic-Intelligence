import threading as thr
from Kernel.Context.Context import Context
from Kernel.DataOps.ArgParser import ArgParser
from Vendors.Facebook.Kernel.Pages.homePage import HomePage


class BootLoader:
    __ctx = Context()
    __argParser = ArgParser()
    __argParser.sysArgvTOdict()

    def __init__(self):
        self.__Load()

    def __Load(self):

        if self.__argParser.keyExists(self.__ctx.constants.pFACEBOOK):
            if self.__argParser.keyExists(self.__ctx.constants.pREALITY_ROUTINE):
                t_main = thr.Thread(target=HomePage(ctx=self.__ctx).initialize).start()
