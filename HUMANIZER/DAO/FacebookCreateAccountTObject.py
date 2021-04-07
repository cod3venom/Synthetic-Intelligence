import json

from Kernel.DataOps.StringBuilder import StringBuilder
from Kernel.Global import __levels__, __logger__


class FacebookCreateAccountTObject:

    def __init__(self, FirstName: str, LastName: str, Email: str, Password:str, BirthMonth: str, BirthDay: str, BirthYear: str,
                 Gender: str, PhoneNumber: str = "", Desktop: bool = True):
        self.FirstName = FirstName
        self.LastName = LastName
        self.Email = Email
        self.Password = Password
        self.BirthMonth = BirthMonth
        self.BirthDay = BirthDay
        self.BirthYear = BirthYear
        self.Gender = Gender
        self.PhoneNumber = PhoneNumber
        self.Desktop = Desktop
        __logger__.Print(0, __levels__.Info, self.__str__())

    @classmethod
    def TO(cls, jsData: str):
        try:
            if jsData != "":
                return cls(**json.loads(jsData))
            else:
                return cls(**{'FirstName': 'empty', 'LastName': 'empty', 'Email': 'empty', 'Password': 'empty', 'BirthMonth': 'empty',
                              'BirthDay': 'empty', 'BirthYear': 'empty', 'Gender': 'empty', 'PhoneNumber': 'empty',
                              'Desktop': 'empty'})
        except KeyError as KeyErr:
            __logger__.Print(0, __levels__.Error, str(KeyErr))

    def __str__(self):
        return self.repr()

    def repr(self):
        buffer = StringBuilder()
        buffer.append("<FacebookCreateAccountTObject: ")
        buffer.append(" FirstName= " + str(self.FirstName))
        buffer.append(", LastName= " + str(self.LastName))
        buffer.append(", Email= " + str(self.Email))
        buffer.append(", Password= " + str(self.Password))
        buffer.append(", BirthMonth= " + str(self.BirthMonth))
        buffer.append(", BirthDay= " + str(self.BirthDay))
        buffer.append(", BirthYear= " + str(self.BirthYear))
        buffer.append(", Gender= " + str(self.Gender))
        buffer.append(", PhoneNumber= " + str(self.PhoneNumber))
        buffer.append(" Desktop= " + str(self.Desktop))
        buffer.append(">")
        return buffer.string
