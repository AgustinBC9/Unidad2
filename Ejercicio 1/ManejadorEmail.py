import csv
from claseEmail import Email

class ManejadorLista:
    __lista=[]
     
    def __init__(self):
       self.__lista=[]
       
    def agregarEmail(self,Correo1):
     self.__lista.append(Correo1)       
       
    def abrirArchivo(self):
         
      archivo = open('EMAIL LISTA.csv')
      reader = csv.reader(archivo,delimiter=';')
      bandera = True
   
      for linea in reader:
       if bandera:
          "saltear cabecera"
          bandera=not bandera 
      else:
          idCuenta=linea[0]
          dominio=linea[1]
          tipodominio=linea[2]
          contrasena=linea[3]
          Correo1=Email(idCuenta,dominio,tipodominio,contrasena)
          self.agregarEmail(Correo1)
    
      archivo.close()   
 
    def mostrarDatos(self):
     
     for i in range(len(self.__lista)):
         self.__lista[i].mostrarDatos()
         
    def buscarDom(self,dom):
     
     cont=0
     
     for i in range(len(self.__lista)):
         if(self.__lista[i].getDominio==dom):
           cont=cont+1
    
            
     return cont    