

class PlanAhorro:
      cantidadcuotasPlan = 60
      cantidadcuotasLic = 10
      
      def __init__(self,codigo=0,modelo="",version="",valorVehi=0):
          self.__codigo=codigo
          self.__modelo=modelo
          self.__version=version
          self.__valorVehi=valorVehi
          
    @classmethod
    def getcantcuotasPlan(cls):
        return cls.cantidadcuotasPlan
    @classmethod
    def getcantcuotasLic(cls):
        return cls.cantidadcuuotasLic
    
    
     
    