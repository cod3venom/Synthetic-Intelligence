from fake_useragent import UserAgent
from Kernel.Global import __texts__, __levels__, __logger__


class AgencyFactory:

    def buildOwn(self):
        pass

    @property
    def getNewAgent(self):
        agent = UserAgent(verify_ssl=False).random
        __logger__.Print(0, __levels__.Info, __texts__.getText(3).format(agent))
        return agent
