import json
from Kernel.DataOps.StringBuilder import StringBuilder
from Kernel.Global import __levels__, __logger__


class FacebookCredentialsTObject:

    def __init__(self, USERNAME: str, PASSWORD: str):
        self.username = USERNAME
        self.password = PASSWORD

    @classmethod
    def TO(cls, jsData: str):
        try:
            if jsData != "":
                return cls(**json.loads(jsData))
            else:
                return cls(**{'USERNAME': 'empty', 'PASSWORD': 'empty'})
        except KeyError as KeyErr:
            __logger__.Print(0, __levels__.Error, str(KeyErr))

    def __str__(self):
        return self.repr()

    def repr(self):
        buffer = StringBuilder()
        buffer.append("<FacebookCredentialsTObject: ")
        buffer.append(" USERNAME= " + str(self.username))
        buffer.append(", PASSWORD= " + str(self.password))
        buffer.append(">")
        return buffer.string
