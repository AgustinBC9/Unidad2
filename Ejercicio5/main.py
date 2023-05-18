from manejadorPlan import ManejadorPlan
from menuPlan import Menu

if __name__ == '__main__':

 unaLista = ManejadorPlan()
 unaLista.abrirArchivo()
 unaLista.mostrarDatos()
 
 menu=Menu()
 
 menu.Menu(unaLista)

