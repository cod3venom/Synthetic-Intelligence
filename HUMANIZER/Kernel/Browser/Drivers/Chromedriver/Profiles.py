from DAO.ChromeDriverSettingsTObject import ChromeDriverSettingsTObject


class Profiles:

    def default(self) -> ChromeDriverSettingsTObject:
        return ChromeDriverSettingsTObject(incognito=True)
