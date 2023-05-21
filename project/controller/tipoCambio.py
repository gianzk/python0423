import models.modelsCase as md

class TipoCambio:

    def __init__(self) -> None:
        self.model=md.TipoDeCambio()
    def insertData(self,data):
        #data tiene que ser una tupla
        data=self.getApi()
        self.model.insertData(data)
    def getApi(self):
        pass