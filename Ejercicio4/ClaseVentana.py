class Ventana:
   __titulo=""
   __superiorIzqX=0
   __superiorIzqY=0
   __inferiorDerX=500
   __inferiorDerY=500
   
   def __init__(self,titulo="",superiorIzqX=0,superiorIzqY=0,inferiorDerX=500,inferiorDerY=500):
       
       self.__titulo=titulo
       self.__superiorXIzq=superiorIzqX
       self.__superiorYIzq=superiorIzqY
       self.__inferiorXDer=inferiorDerX
       self.__inferiorYDer=inferiorDerY
   
   def mostrar(self):
       print(" Titulo: {}".format(self.__titulo))
       print("Vertice X sup. Izq:{}, Vertice Y sup. Izq:{} , Vertice X Inf. Der: {}, Vertice Y Inf Dere:{}".format(self.__superiorXIzq,self.__superiorYIzq,self.__inferiorXDer,self.__inferiorYDer))
       
   def getTitulo(self):
           return self.__titulo
       
   def alto(self):
        if self.__superiorYIzq == 0:
            alto=self.__superiorYIzq + self.__inferiorYDer
        else:
            alto=self.__superiorYIzq - self.__inferiorYDer

        return (alto)

   def ancho(self):
        if self.__superiorXIzq == 0:
            ancho=self.__superiorXIzq + self.__inferiorXDer
        else:
            ancho=self.__superiorXIzq - self.__inferiorXDer

        return (ancho)
    
   def moverDerecha(self,num):
        if type(num)==int:
            self.__inferiorXDer = self.__inferiorXDer + num
            self.__superiorXIzq = self.__superiorXIzq + num
        else:
            print("El valor pasado por parametro no es del tipo entero")

   def moverIzquierda(self,num):
        if type(num)==int:
            self.__superiorXIzq = self.__superiorXIzq - num
            self.__inferiorXDer = self.__inferiorXDer - num
        else:
            print("El valor pasado por parametro no es del tipo entero")

   def bajar(self,num=0):
        if type(num)==int:
            self.__superiorYIzq = self.__superiorYIzq + num
            self.__inferiorYDer = self.__inferiorYDer + num
        else:
            print("El valor pasado por parametro no es del tipo entero")

   def subir(self,num=0):
        if type(num)==int:
            self.__inferiorYDer = self.__inferiorYDer - num
            self.__superiorYIzq = self.__superiorYIzq - num
        else:
            print("El valor pasado por parametro no es del tipo entero")
       