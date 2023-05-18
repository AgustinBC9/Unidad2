from ManejadorRegistro import ManejadorRegistro

if __name__=='__main__':
    

 ListaRegistro=ManejadorRegistro()
 
 ListaRegistro.abrirArchivo()
 
 print("\n  ****** MENU ******* ")
 print("1) - Mostrar para cada variable el dia y la hora de menor y mayor valor ")
 print("2) - Indicar la temperatura promedio mensual por cada hora ")
 print("3) - Dado un numero de dia listar los valores de las tres variables para cada hora del dia padre ")
 print("0) Salir ")
 
 opcion=int(input(' Ingrese opcion = '))
 
 while opcion != 0:
     
     if opcion==1:
        ListaRegistro.mostrarmayortemp() 
        ListaRegistro.mostrarmayorpresion()
        ListaRegistro.mostrarmayorhumedad()
     elif opcion==2:
        ListaRegistro.TempProm()
     elif opcion==3:
         dia=int(input("Ingrese numero de dia = "))
         ListaRegistro.mostrarvariables(dia)
     else:
      print(" Elija nuevamente una opcion = ")
         
      print("\n  ****** MENU ******* ")
      print("1) - Mostrar para cada variable el dia y la hora de menor y mayor valor ")
      print("2) - Indicar la temperatura promedio mensual por cada hora ")
      print("3) - Dado un numero de dia listar los valores de las tres variables para cada hora del dia padre ")
      print("0) Salir ")
      opcion=int(input(' Ingrese opcion = '))  
      
