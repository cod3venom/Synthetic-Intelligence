class StringBuilder:
    def __init__(self):
        self.string = ""

    def append(self, string):
        self.string += str(string)

    def __str__(self):
        return str(self.string)
