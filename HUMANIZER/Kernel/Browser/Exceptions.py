import sys


class Exceptions:

    def exChromeConfigIsEmpty(self):
        print("CHROME CONFIG IS NONE")
        sys.exit(1)
    def exEmptyBinaryPath(self):
        print("BINARY PATH IS EMPTY")
        sys.exit(1)

