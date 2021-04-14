import json

from Kernel.FileSystem.fSys import fSys


class LocalSettingsTObject:

    def __init__(self, settings_file: str, software_name: str):
        data = json.loads(fSys().readfile(settings_file))
        for JsonData in data[software_name]:
            self.VERSION = JsonData["VERSION"]
            self.en_US = JsonData['en_US']
            self.pl_PL = JsonData['pl_PL']
            self.TERMINAL_PREFIX = JsonData["TERMINAL_PREFIX"].format(self.VERSION)
            self.LOG_FORMAT = JsonData["LOG_FORMAT"]
            self.BINARY_PATH = JsonData["BINARY_PATH"]
            self.JS_PAYLOADS_PATH = JsonData["JS_PAYLOADS_PATH"]
            self.DEFAULT_ENCODING = JsonData["DEFAULT_ENCODING"]
            ################# FACEBOOK SETTINGS ########################
            self.FB_HOME_PC = JsonData["FB_HOME_PC"]
            self.FB_HOME_MOBILE = JsonData["FB_HOME_MOBILE"]

            ################# YANDEX SETTINGS ########################
            self.YANDEX_CAPTCHA_DIR = JsonData["YANDEX_CAPTCHA_DIR"]
