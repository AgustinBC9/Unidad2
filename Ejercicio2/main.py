from ViajeroFrecuente import ViajeroFrecuente
from ManejadorListaViajero import ManejadorViajero

if __name__=='__main__':

 viajero = ViajeroFrecuente()    
 listaViajero = ManejadorViajero()
 listaViajero.LeerArchi()
 
 print(" Listado de Viajeros \n")
 
 listaViajero.mostrarDatos()

 print("\n1) Consultar Cantidad de millas ")
 print("2) Acumular millas ")
 print("3) Canjear millas ")
 print("0) Salir ")
 
 opcion=int(input(' Ingrese opcion = '))
 
 numero=int(input("\n Ingrese numero de viajero frecuente = "))
 pos=listaViajero.buscarViajero(numero)
 
 while opcion != 0:
     
     if pos==None:
        print("\n Viajero no existe ")
     elif opcion==1:
           print("\n Cantidad total de millas {} del viajero numero {} ".format(viajero.CantidadTotaldeMillas(),pos+1))
     elif opcion==2:
           smillas=input('Ingrese millas a acumular = ')
           print(" Millas actualizada a = ",viajero.acumularMillas(smillas))
     elif opcion==3:
           cantmillas_acum=input(" Ingrese cantidad de millas a canjear = ")
           print(" Valor de las millas acumuladas = ",viajero.canjearMillas(cantmillas_acum))
     else:
        print(" Elija nuevamente una opcion = ")
        
        print("1) Consultar Cantidad de millas ")
        print("2) Acumular millas ")
        print("3) Canjear millas ")
        print("0) Salir ")
        opcion=int(input(' Ingrese opcion = '))
