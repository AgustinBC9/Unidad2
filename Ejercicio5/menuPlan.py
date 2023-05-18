
class Menu:
    opcion=0
    
    def __init__(self,opcion=0):
        self.opcion=0
        
    def Menu(self,unaLista):
        
        salir = False

        while not salir:
            print("\n |------------------------------------Menu de opciones-------------------------------------------|")
            print("|1- Actualizar valor de vehiculo |")
            print("|2- Dado un valor, mostrar código del plan, modelo y versión del vehículo cuyo valor de la cuota sea inferior al valor dado.|")
            print("|3- Mostrar el monto que se debe haber pagado para licitar el vehículo |")
            print("|4- Dado el código de un plan, modificar la cantidad cuotas que debe tener pagas para licitar |")
            print("|5- Salir ")
            print("|-----------------------------------------------------------------------------------------------|")
            op = int(input("Elija una opción del menu: "))

            if op == 1:
                 unaLista.actualizarValor()
                 
            elif op == 2: 
                 v=int(input("\n Ingrese valor: "))
                 unaLista.cuotainferior(v)
    
            elif op == 3:
                unaLista.montolicitar()
                
            elif op == 4:
                c=int(input("\n Ingrese codigo: "))
                unaLista.modificar(c)
              
            elif op == 5:
                salir = True
            else:
                print("Opción incorrecta")
        