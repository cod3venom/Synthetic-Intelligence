import requests as req
from Kernel.HTTP.httpClient import HttpClient
from Kernel.Logger.Logger import Logger, Levels, Texts
from DAO.LocalSettingsTObject import LocalSettingsTObject

__software_name__: str = "HUMANIZER"
__settings_file__: str = "/usr/bin/FBView/Humanizer/Settings/Settings.json"
__localSettings__ = LocalSettingsTObject(settings_file=__settings_file__, software_name=__software_name__)


__levels__ = Levels()
__logger__ = Logger(texts_file=__localSettings__.en_US, log_format=__localSettings__.LOG_FORMAT)

__texts__ = Texts(file=__localSettings__.en_US)
__texts__.loadTexts()

__http__ = HttpClient()
__http__.setSession(req.session())
