class Email:
    __idCuenta = 'idCuenta'
    __dominio = 'dominio' 
    __tipodominio = 'tipodominio'
    __contrasena = 'contrasena'
    
    def __init__(self, idCuenta="", dominio="", tipodominio="", contrasena=""):
        self.__idCuenta = idCuenta
        self.__dominio = dominio
        self.tipodominio = tipodominio
        self.__contrasena = contrasena
        
    def mostrarDatos(self):
        print("Id Cuenta = {}, Dominio = {}, Tipo de dominio = {}, Contraseña = {}".format(self.__idCuenta,self.__dominio,self.__tipodominio,self.__contrasena))
        
    def retornaEmail(self):
            
            #print("\n Retorna Mail")
            emaail=self.__idCuenta+'@'+self.__dominio+'.'+self.__tipodominio
            return emaail
            
    def crearCuenta(self, prueba):
            
             print("\n Crear Cuenta ")
             prueba=prueba.split('@')
             self.__idCuenta=prueba[0]
             prueba=prueba[1].split('.')
             self.__dominio=prueba[0]
             self.__tipodominio=prueba[1]        
             
    def getDominio(self):
             
             #print("\n Retorna Dominio ")
             dom=self.__dominio
             return(dom)
        
    def CambiarContra(self):
            
            contra = input('\n Ingrese contraseña actual = ')
            if self.__contrasena == contra:
               self.__contrasena=input('\n Ingrese contraseña nueva = ')
            else:
                print('\n Contraseña ingresada incorrecta')
                