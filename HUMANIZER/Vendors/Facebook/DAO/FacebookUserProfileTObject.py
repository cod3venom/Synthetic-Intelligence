import json

from Kernel.DataOps.StringBuilder import StringBuilder
from Kernel.Global import __levels__, __logger__


class FacebookUserProfileTObject:

    def __init__(self, USERNAME: str, FIRSTNAME: str, LASTNAME: str, LIVING_LOCATION: str, JOINED_AT: str = ""):
        self.USERNAME = USERNAME
        self.FIRSTNAME = FIRSTNAME
        self.LASTNAME = LASTNAME
        self.LIVING_LOCATION = LIVING_LOCATION
        self.JOINED_AT = JOINED_AT

    @classmethod
    def TO(cls, jsData: str):
        try:
            if jsData != "":
                return cls(**json.loads(jsData))
            else:
                return cls(**{'USERNAME': 'empty', 'FIRSTNAME': 'empty', 'LASTNAME': 'empty', 'LIVING_LOCATION': 'empty', 'JOINED_AT': 'empty'})
        except KeyError as KeyErr:
            __logger__.Print(0, __levels__.Error, str(KeyErr))

    def __str__(self):
        return self.repr()

    def repr(self):
        buffer = StringBuilder()
        buffer.append("<FacebookCredentialsTObject: ")
        buffer.append(" USERNAME= " + str(self.USERNAME))
        buffer.append(", FIRSTNAME= " + str(self.FIRSTNAME))
        buffer.append(", LASTNAME= " + str(self.LASTNAME))
        buffer.append(", LIVING_LOCATION= " + str(self.LIVING_LOCATION))
        buffer.append(", JOINED_AT= " + str(self.JOINED_AT))
        buffer.append(">")
        return buffer.string
