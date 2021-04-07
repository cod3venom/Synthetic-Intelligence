from Kernel.Global import __http__, __levels__, __logger__
import  requests

class NoCaptcha:

    def __init__(self, url=""):
        """
        :param url:
        :type url:
        """
        self.__url = url


    def parseText(self):
        image = requests.get(self.__url, stream=True)
        print(image)
