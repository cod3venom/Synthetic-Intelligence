from Vendors.Facebook.Life import Life


class Main:

    def cmain(self) -> int:
        Life().cmain()
        return 0


if __name__ == '__main__':
    try:
        _main = Main()
        _main.cmain()
    except IndexError as exp:
        print(str(exp))
