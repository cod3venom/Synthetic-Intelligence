import sys

from Vendors.Facebook.Kernel.Scripts.CreateAccount import CreateAccount as fbAccount
from Vendors.Facebook.Life import Life
from Vendors.Yandex.Procedures.CreateAccount import CreateAccount as yaAccount


class Main:

    def cmain(self, argv: str) -> int:
        if argv == "crtFbAcc":
            crtAcc = fbAccount(sys.argv[2])
            crtAcc.start()
        if argv == "crtYaAcc":
            crtAcc = yaAccount(sys.argv[2])
            crtAcc.start()
        if argv == 'fbLife':
            fbLife = Life()
            fbLife.cmain(email=sys.argv[2], password=sys.argv[3], useIncognito=True)

        return 0


if __name__ == '__main__':
    try:
        _main = Main()
        _main.cmain(sys.argv[1])
    except IndexError as exp:
        print(str(exp))

