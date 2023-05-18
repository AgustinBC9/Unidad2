
class ViajeroFrecuente:
    __num_viajero=0
    __dni=''
    __nombre=''
    __apell=''
    __millas_acum=0

    def __init__(self,xnum=0,xdni="",xnomb="",xapell="",xmillas=0):
    
     self.__num_viajero=xnum
     self.__dni=xdni
     self.__nombre=xnomb
     self.__apell=xapell
     self.__millas_acum=xmillas
     
    def mostrarDatos(self):
        
        print("Numero de viajero = {}, DNI = {}, Nombre = {}, Apellido = {}, Millas Acumuladas = {}".format(self.__num_viajero,self.__dni,self.__nombre,self.__apell,self.__millas_acum))
     
     
    def CantidadTotaldeMillas(self):
     return self.__millas_acum
     

    def acumularMillas(self,smillas):
     self.__millas_acum=self.__millas_acum+smillas
    
     return self.__millas_acum     
  
    def canjearMillas(self,cantmillas_acum):
    
     if cantmillas_acum <= self.millas_acum:
        self.__millas_acum=self.__millas_acum-cantmillas_acum
     else:
        print("Millas a canjear insuficientes")
        
        
     return self.__millas_acum 
 
    def getnumviajero(self):
        return self.__num_viajero
 
 
        
