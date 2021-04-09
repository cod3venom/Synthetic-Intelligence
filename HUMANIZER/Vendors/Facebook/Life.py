from Vendors.Facebook.Kernel.Bootloader import BootLoader
from Vendors.Facebook.Kernel.Features.Auth.FbAuth import FbAuth
import threading as thr

class Life:

    def cmain(self, email: str, password: str, useIncognito: bool = False) -> int:
        fbAuth = FbAuth(email=email, password=password)
        BootLoader(isLogged=fbAuth.doLogin(), browser=fbAuth.browser)
        return 0



