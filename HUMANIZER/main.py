import sys, os
import time

from Kernel.Global import __localSettings__, __logger__, __levels__
from Kernel.Browser.Browser import Browser
from Vendors.Facebook.Procedures.CreateAccount import CreateAccount

class Main:

    def cmain(self, argv: str) -> int:
        if argv == "crtFbAcc":
            crtAcc = CreateAccount(sys.argv[2])
            crtAcc.start()

if __name__ == '__main__':
    mainArgv: str
    try:
        mainArg = sys.argv[1]
    except IndexError:
        mainArgv = ""

    _main = Main()
    _main.cmain(mainArg)
