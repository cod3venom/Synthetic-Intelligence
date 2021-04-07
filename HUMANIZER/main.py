import sys, os
import time

from Kernel.Global import __localSettings__, __logger__, __levels__
from Kernel.Browser.Browser import Browser
from Vendors.Facebook.Procedures.CreateAccount import CreateAccount as fbAccount
from Vendors.Yandex.Procedures.CreateAccount import CreateAccount as yaAccount


class Main:

    def cmain(self, argv: str) -> int:
        if argv == "crtFbAcc":
            crtAcc = fbAccount(sys.argv[2])
            crtAcc.start()
        if argv == "crtYaAcc":
            crtAcc = yaAccount(sys.argv[2])
            crtAcc.start()
        return 0


if __name__ == '__main__':
    try:
        _main = Main()
        _main.cmain(sys.argv[1])
    except IndexError as exp:
        print(str(exp))

