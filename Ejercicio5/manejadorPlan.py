from Plan import PlanAhorro
import csv

class ManejadorPlan:
    __lista=[]
    
    def __init__(self):
        self.__lista=[]
        
    def abrirArchivo(self):
        
        archivo=open("planes.csv")
        reader=csv.reader(archivo,delimiter=';')
        
        fila = next(reader)
        bandera = fila[4]
        archivo.seek(0)
        
        for fila in reader:
            codigo=int(fila[0])
            modelo=fila[1]
            version=fila[2]
            valorVehi=int(fila[3])
            cantcuotas=int(fila[4])
            cantlicitar=int(fila[5])
            
            if bandera != cantcuotas:
                PlanAhorro.cantidadcuotaPlan=cantcuotas
                PlanAhorro.cantidadcuotasLic = cantlicitar
                bandera = cantcuotas
                unplan = PlanAhorro(codigo,modelo,version,valorVehi)
                self.__lista.append(unplan)                
            else:
                unplan = PlanAhorro(codigo,modelo,version,valorVehi)
                self.__lista.append(unplan)  
                
        archivo.close()
        
    def mostrarDatos(self):
         for plan in self.__lista:
             print(plan.mostrarDatos())
             
    def actualizarValor(self):
   
          for plan in self.__lista:
              print(plan.mostrarDatos())  
              valornuevo=int(input("\n Ingrese Valor nuevo del vehiculo: "))
              plan.modificarValor(valornuevo)
              
    def cuotainferior(self,v):
         
        for plan in self.__lista:
            print(plan)
            impor=plan.getvalorVehi()
            cant=PlanAhorro.getcantcuotasLic()
            valorcuota=(impor/cant) + impor * 0.1
            
            if valorcuota < v:
                print(plan.mostrarDatos())
             
    def montolicitar(self):
        for plan in self.__lista:
           print(plan) 
           impor=plan.getvalorVehi()
           cant=PlanAhorro.getcantcuotasLic()
           valorcuota=(impor/cant) + impor * 0.1
           cant2=PlanAhorro.getcantcuotasLic()
           montoLicitar=valorcuota*cant2
           print("\n El monto para licitar este vehiculo es de = :{:.2f} ".format(montoLicitar))
           
    def modificar(self,c):
        
        i=0
        band = False
        while i < len(self.__lista) and (band==False):
            
             if c == self.__listai[i].getCodigo():
                band = True
             else:
                i=i+1
                
        return band       
                
       


















       
            