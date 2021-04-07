from Kernel.Logger.Logger import Logger, Levels
from DAO.LocalSettingsTObject import LocalSettingsTObject

__software_name__: str = "HUMANIZER"
__settings_file__: str = "/usr/bin/FBView/Humanizer/Settings/Settings.json"
__localSettings__ = LocalSettingsTObject(settings_file=__settings_file__, software_name=__software_name__)


__levels__ = Levels()
__logger__ = Logger(texts_file=__localSettings__.en_US, log_format=__localSettings__.LOG_FORMAT)
