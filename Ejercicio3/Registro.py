class Registro:
    __Temperatura=0
    __Presion=0
    __Humedad=0
    
    def __init__(self,Temperatura=0,Presion=0,Humedad=0):
       self.__Temperatura=Temperatura
       self.__Presion=Presion
       self.__Humedad=Humedad
    
    def getTemp(self):
        return self.__Temperatura
    
    def getPresion(self):
        return self.__Presion
    
    def getHumedad(self):
        return self.__Humedad
    

