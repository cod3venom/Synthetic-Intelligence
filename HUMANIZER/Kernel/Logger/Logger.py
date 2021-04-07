import datetime
import inspect
import os

from colorama import Fore


class Constants:
    EMPTY = ""
    HASHTAG = "#"
    DOLLAR = "$"
    NEWLINE = "\n"


class Levels:
    Info = "Info"
    Success = "Success"
    Warning = "Warning"
    Error = "Error"
    hackerType = "hackerType"


class Colors:
    Default = Fore.WHITE
    Success = Fore.GREEN
    Error = Fore.RED
    Warning = Fore.YELLOW
    Info = Fore.BLUE
    HackerType = Fore.LIGHTCYAN_EX


class Texts:
    file: str
    textStack: dict = {}
    constants = Constants()

    def __init__(self, file: str):
        self.file = file

    def loadTexts(self):
        if os.path.isfile(self.file):
            with open(self.file, "r", encoding="utf-8") as reader:
                content = reader.read()
                if self.constants.NEWLINE in content:
                    lines = content.split(self.constants.NEWLINE)
                for line in lines:
                    if self.constants.HASHTAG in line:
                        spl = line.split(self.constants.HASHTAG)
                        self.textStack[spl[0]] = spl[1]

    def textFromDict(self, number: int, target: dict) -> str:
        if self.textStack is not None:
            try:
                if str(number) in target.keys():
                    return target[str(number)]
            except KeyError:
                print("Text not found")
                return self.constants.EMPTY
        return self.constants.EMPTY

    def getText(self, number: int) -> str:
        return self.textFromDict(number, self.textStack)


class Logger:
    texts_file: str
    log_format: str

    def __init__(self, texts_file: str, log_format: str):
        self.texts_file = texts_file
        self.log_format = log_format
        self.texts = Texts(self.texts_file)
        self.texts.loadTexts()

        self.constants = Constants()
        self.level = Constants.EMPTY
        self.levels = Levels()
        self.time = Constants.EMPTY
        self.text = Constants.EMPTY
        self.color = Constants.EMPTY
        self.caller = Constants.EMPTY
        self.colors = Colors()

    def initColor(self):
        if self.level == self.levels.Info:
            self.color = self.colors.Info
        if self.level == self.levels.Success:
            self.color = self.colors.Success
        if self.level == self.levels.Warning:
            self.color = self.colors.Warning
        if self.level == self.levels.Error:
            self.color = self.colors.Error
        if self.level == self.levels.hackerType:
            self.color = self.colors.HackerType

    def Print(self, msg_num: int, level: Levels, message: str = None):
        self.level = level
        self.initColor()

        self.caller = inspect.stack()[1][0].f_locals["self"].__class__.__name__ + "." + inspect.stack()[
            1].function + self.constants.HASHTAG + str(inspect.stack()[1].lineno)
        self.time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        if msg_num > 0:
            self.text = self.texts.getText(msg_num)
        else:
            if message:
                self.text = str(message)

        text = self.log_format.format(self.colors.Success, self.colors.Warning + self.time,
                                      self.color + self.caller, "HUMANIZER", self.colors.Default + self.text)
        print(text)
        self.text = self.constants.EMPTY
        text = self.constants.EMPTY
