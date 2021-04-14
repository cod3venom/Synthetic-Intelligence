from Kernel.Global import __logger__, __levels__, __texts__


class ArgParser:
    __EMPTY = ""
    __SPACE = " "
    __EQUALITY = "="
    __DOUBLE_DASH = "--"
    __args = {}

    def setARgs(self, args: dict):
        self.__args = args

    def getArgs(self) -> dict:
        return self.__args

    def __splitOnEquality(self, param: str) -> list:
        return param.split(self.__EQUALITY)

    def sysArgvTOdict(self) -> dict:
        import sys
        for param in sys.argv:
            if self.__EQUALITY in param:
                onEquality = self.__splitOnEquality(param=param)
                try:
                    self.__args[onEquality[0]] = onEquality[1]
                except IndexError:
                    print("PARAMS INDEX ERROR")
            else:
                self.__args[param] = self.__EMPTY
        return self.getArgs()

    def getValueOf(self, key: str):
        for _key in self.__args.keys():
            if _key == key:
                return self.__args[_key]

        __logger__.Print(0, level=__levels__.Warning, message=__texts__.getText(10).format(key))
        return self.__EMPTY

    def keyEquals(self, key: str, value):
        if self.getValueOf(key=key) == value:
            return True
        return False

    def keyExists(self, key: str) -> bool:
        for _key in self.__args.keys():
            if key == _key:
                return True
        return False
