import glob
from Kernel.FileSystem.fSys import fSys
class JsBundle:
    jsPack = {}
    def __init__(self, js_payloads_path):
        self.__js_payloads_path = js_payloads_path
        self.loadTOmemory()

    def loadFiles(self) -> list:
        return glob.glob(f"{self.__js_payloads_path}/*.js")


    def loadTOmemory(self):
        files = self.loadFiles()
        for index, file in enumerate(files):
            file_name = fSys().getFilename(file)
            self.jsPackAdd(file_name, file)

    def jsPackExists(self, key):
        for k in self.jsPack.keys():
            if k == key:
                return True
        return False

    def jsPackAdd(self, key, value) -> bool:
        if not self.jsPackExists(key):
            self.jsPack[key] = value
            return True
        return False

    def jsPackRemove(self, key) -> bool:
        if self.jsPackExists(key):
            del self.jsPack[key]
            return True
        return False

    def jsPackGet(self, key) -> str:
        if self.jsPackExists(key):
            return fSys().readfile(self.jsPack[key])
        return ""


