import requests as req


class HttpClient:
    __address: str
    __useTor: bool
    __userAgent: str
    __session: req.Session
    __headers: dict

    def setAddress(self, address: str):
        self.__address = address

    def getAddress(self) -> str:
        return self.__address

    def setTorUsage(self, useTor: bool):
        self.__useTor = useTor

    def getTorUsage(self) -> bool:
        return self.__useTor

    def setUserAgent(self, agent: str):
        self.__userAgent = agent

    def getUserAgent(self) -> str:
        return self.__userAgent

    def generateUserAgent(self):
        pass

    def setSession(self, session: req.Session):
        self.__session = session

    def getSession(self) -> req.Session:
        return self.__session

    def setHeaders(self, headers: dict):
        self.__headers = headers

    def getHeaders(self) -> dict:
        return self.__headers

    def genDefaultHeaders(self) -> dict:
        return {
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9,pl;q=0.8',
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36'
        }

    def getRequest(self, address: str = "", stream: bool = False):
        target_host = ""
        if address != "":
            target_host = address
        else:
            target_host = self.__address
        return self.getSession().get(target_host, stream=stream)

    def postRequest(self, address: str, data: dict):
        target_host = ""
        if address != "":
            target_host = address
        else:
            target_host = self.__address
        response = self.getSession().post(target_host, data).text
        if response == '[]':
            return ""
        return response

    def getImage(self, address):
        return req.get(address, headers=self.genDefaultHeaders(), stream=True).raw
