import json

from Kernel.DataOps.StringBuilder import StringBuilder
from Kernel.Global import __levels__, __logger__


class YandexCreateAccountTObject:

    def __init__(self, FirstName: str, LastName: str, UserName: str, Password:str,  Desktop: bool = True):
        self.FirstName = FirstName
        self.LastName = LastName
        self.UserName = UserName
        self.Password = Password
        self.Desktop = Desktop
        __logger__.Print(0, __levels__.Info, self.__str__())

    @classmethod
    def TO(cls, jsData: str):
        try:
            if jsData != "":
                return cls(**json.loads(jsData))
            else:
                return cls(**{'FirstName': 'empty', 'LastName': 'empty', 'UserName': 'empty', 'Password': 'empty', 'Desktop': 'empty'})
        except KeyError as KeyErr:
            __logger__.Print(0, __levels__.Error, str(KeyErr))

    def __str__(self):
        return self.repr()

    def repr(self):
        buffer = StringBuilder()
        buffer.append("<YandexCreateAccountTObject: ")
        buffer.append(" FirstName= " + str(self.FirstName))
        buffer.append(", LastName= " + str(self.LastName))
        buffer.append(", UserName= " + str(self.UserName))
        buffer.append(", Password= " + str(self.Password))
        buffer.append(" Desktop= " + str(self.Desktop))
        buffer.append(">")
        return buffer.string
