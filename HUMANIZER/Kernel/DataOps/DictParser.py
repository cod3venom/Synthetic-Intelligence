class DictParser:
    args: dict

    def __init__(self, args: dict):
        self.args = args

    def setDict(self, args: dict):
        self.args = args

    def keyExists(self, key: str):
        for key in self.args.keys():
            if self.args[key] != "":
                return True
        return False

    def keyEquals(self, key, value):
        for _key in self.args.keys():
            if _key == key:
                if self.args[_key] == value:
                    return True
        return False

    def getValue(self, key: str):
        if self.keyExists(key=key):
            return self.args[key]

    def addValue(self, key: str, value, overWrite: bool = False):
        if overWrite:
            self.args[key] = value
        else:
            if not self.keyExists(key=key):
                self.args[key] = value
        return self.args

    def removeByValue(self, value):
        for key in self.args.keys():
            if self.args[key] == value:
                del self.args[key]
                return True
        return False
