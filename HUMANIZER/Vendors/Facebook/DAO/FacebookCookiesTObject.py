import json
from Kernel.DataOps.StringBuilder import StringBuilder
from Kernel.Global import __levels__, __logger__


class FacebookCookiesTObject:

    def __init__(self,  name: str, value: str):
        self.name = name
        self.value = value

    @classmethod
    def TO(cls, jsData: str):
        try:
            if jsData != "":
                return cls(**json.loads(jsData))
            else:
                return cls(**{'name': 'empty', 'value': 'empty'})
        except KeyError as KeyErr:
            __logger__.Print(0, __levels__.Error, str(KeyErr))

    def __str__(self):
        return self.repr()

    def repr(self):
        buffer = StringBuilder()
        buffer.append("<FacebookCookiesTObject: ")
        buffer.append(", name= " + str(self.name))
        buffer.append(", value= " + str(self.value))
        buffer.append(">")
        return buffer.string