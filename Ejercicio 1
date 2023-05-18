from claseEmail import Email
from ManejadorEmail import ManejadorLista

if __name__=='__main__':
    
    
  Correo1 = Email()
  ListaCorreo = ManejadorLista() 
  prueba = 'alumnnopoo@gmail.com'
  Correo1.crearCuenta(prueba) 
  
  
  nomb=input("\n Ingrese Nombre = ")
  c=input(" Ingrese Correo = ")
  print(' Estimado {}'.format(nomb),'te enviaremos tus mensajes a la direccion {}'.format(c))
  
  Correo1.CambiarContra()
 
  c2 = input('\n Ingrese un correo nuevo = ')
  c2=c2.split('@')
  IdC=c2[0]
  c2[1]=c2[1].split('.')
  Iden=c2[0]
  tipD=c2[1]
  
  Correo2 = Email(IdC,Iden,tipD) 
  
  dom=input('\n Ingrese dominio a buscar = ')
  
  print("\n Hay {} dominios ingresados iguales ".format(ListaCorreo.buscarDom(dom)))
  
  ListaCorreo.abrirArchivo()
  ListaCorreo.mostrarArchivo()
