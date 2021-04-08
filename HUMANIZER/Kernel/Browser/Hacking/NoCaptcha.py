import string
import random

from Kernel.Global import  __levels__, __logger__, __texts__, __localSettings__
from PIL import Image
import urllib.request
import pytesseract


class NoCaptcha:



    def parseText(self, fileName) -> str:
        captchaCode = pytesseract.image_to_string(Image.open(fileName), config='--psm 7')
        captchaCode.encode(__localSettings__.DEFAULT_ENCODING).decode(__localSettings__.DEFAULT_ENCODING).strip()
        if captchaCode != "":
            __logger__.Print(0, __levels__.Success, __texts__.getText(4).format(captchaCode))
        else:
            __logger__.Print(5, __levels__.Success)
        return captchaCode
