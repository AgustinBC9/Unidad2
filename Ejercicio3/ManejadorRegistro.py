from Registro import Registro
import csv

class ManejadorRegistro: 
    __lista=[]
    
    def __init__(self):
       self.__lista=[]

    def agregarRegistro(self,unRegistro,dia,hora):
        self.__lista[dia-1][hora-1]= unRegistro

    def abrirArchivo(self):
        self.__lista=[[ 0 for column in range(24)]for fila in range (2)]
      
        archivo=open('Registro.csv')
        reader=csv.reader(archivo,delimiter=';')
        
        for fila in reader:
            dia=int(fila[0])
            hora=int(fila[1])
            Temperatura=int(fila[2])
            Presion=int(fila[3])
            Humedad=int(fila[4])
            unRegistro=Registro(Temperatura,Presion,Humedad)
            self.agregarRegistro(unRegistro,dia,hora)
            
        archivo.close()  
        
    def mostrarmayortemp(self):
         
        max=0
        min=999
        
        for i in range(len(self.__lista)): 
            for j in range(len(self.__lista[i])):
                if max < self.__lista[i][j].getTemp():
                    max = self.__lista[i][j].getTemp()
                    dia = i+1
                    hora = j
                if min > self.__lista[i][j].getTemp():
                    min=self.__lista[i][j].getTemp()
                    dia1=i+1
                    hora1=j
            
            
            
                    
        print("El dia : {} y la hora: {} de mayor temperatura fue de : {}".format(dia,hora,max))
        print("El dia : {} y la hora: {} de menor temperatura fue de : {}".format(dia1,hora1,min))     
      
        
    def mostrarmayorpresion(self):
        
        max=0
        min=999
        
        for i in range(len(self.__lista)): 
            for j in range(len(self.__lista[i])): 
                if max < self.__lista[i][j].getPresion():
                    max=self.__lista[i][j].getPresion()
                    dia=i+1
                    hora=j
                if min > self.__lista[i][j].getPresion():
                    min=self.__lista[i][j].getPresion()
                    dia1=i+1
                    hora1=j
                    
                    

                  
        print("El dia : {} y la hora: {} , de mayor humedad fue de : {}" .format(dia,hora,max))
        print("El dia : {} y la hora: {} , de menor humedad fue de : {}" .format(dia1,hora1,min))
      
    
    def mostrarmayorhumedad(self):
        
        max=0
        min=999
        for i in range(len(self.__lista)): 
            for j in range(len(self.__lista[i])): 
                if max < self.__lista[i][j].getHumedad():
                    max = self.__lista[i][j].getHumedad()
                    dia = i+1
                    hora = j
                if min > self.__lista[i][j].getHumedad():
                    min = self.__lista[i][j].getHumedad()
                    dia1 = i+1
                    hora1 = j     
                    
                    
        print("El dia : {} y la hora: {} , de mayor humedad fue de : {}" .format(dia,hora,max))
        print("El dia : {} y la hora: {} , de menor humedad fue de : {}" .format(dia1,hora1,min))
 
         
    def TempProm(self):
        
        i = 0
        while i < len(self.__lista[0]):
            j=0
            acum=0
            while j < len(self.__lista):
                acum = self.__lista[j][i].getTemp()+acum
                j=j+1
            promedio=acum/2
            print("Para la hora {} el promedio mensual de la temperatura es de {}".format(i+1, promedio))
            i=i+1
            
    def mostrarvariables(self,dia):
        H = "Hora"
        t ="Temperatura"
        hu = "Humedad"
        p = "Presion"
        #print("{:^15}{:^15}{:^15}{:^15}".format(H,t,hu,p))
        print(f"{H:^15}{t:^15}{hu:^15}{p:^15}")#desde python 3.6 y superior colocando la "f"
        for i in range(24):
            print("{:^15}{:^15}{:^15}{:^15}".format(i,self.__lista[dia][i].getTemp(),self.__lista[dia][i].getPresion(),self.__lista[dia][i].getHumedad()))       
         
        
    