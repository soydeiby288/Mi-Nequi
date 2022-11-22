#Mi Nequi

from getpass import getpass

class nequi:
    
    def registro(self):
        
        print("***REGISTRESE*** ")
        
        self.nombres = str(input("Escriba su nombre: "))
        self.apellidos = str(input("Escriba su apellido: "))
        self.telefono = int(input("Escriba su numero de telefono: "))
        self.edad = int(input("Escriba su edad: "))
        self.contraseña = int(input("Cree una contraseña: "))
        
        if self.edad < 18:
            print("Lo siento, debe de ser mayor de edad para poderse registrarse ")
            self.ingreso()
        else:
            print("***Registro Exitoso*** ")

class datos(nequi):
    
    def ingreso(self):
        
        print("===================")
        print("***BIENVENIDO***")
        print("   INGRESE ")
        
        u = int(input("Telefono: ")) 
        c = int(input("Contraseña: "))
        
        if u == self.telefono and c == self.contraseña:
            saldo = 0
            print("======================================")
            print("***Bienvenido "f"{self.nombres}***")
            print("el saldo de su cuenta es: ","$",saldo)
            print("¿desea recargar su cuenta? ")
            print("1) si")
            print("2) no")
            recargar = int(input("Eliga una opcion: "))
            print("================================================================")
            if recargar == 1:
                consignar = int(input("Escriba la cantidad de dinero que quiere consignar: "))
                total = consignar + saldo
                print("Consignacion Exitosa: ","$",consignar)
                print("===================================")
                print("¿Donde desea guardar su dinero?")
                print("1) *Cuenta de ahorro* ")
                print("2) *Cuenta corriente* ")
                print("3) *Salir* ")
                print("4) *Retirar* ")
                cuenta = int(input("Eliga una opcion: "))
                print("================================================================")
                
                if cuenta == 1:
                    print("Cuenta de ahorros #001")
                    print("saldo: ","$",saldo)
                    cuenta = int(input(("¿Cuanto desea consignar?, recuerde que el saldo disponible es:",consignar)))
                    if cuenta <= consignar:
                        print("================================================================")
                        print("Consignacion realizada con exito: $",cuenta)
                        print("saldo disponible: ",consignar-cuenta)
                        print("*Operacion finalizada*")
                        print("================================================================")
                        self.ingreso()
                    else:
                        if cuenta > consignar:    
                         print("*Saldo insuficiente*")
                         self.ingreso()
                        
                if cuenta == 3:
                    print("*Operacion finalizada*")
                    self.ingreso()
                    
                if cuenta == 2:
                    print("***Bienvenido a Cuenta corriente***")
                    print("saldo: ","$",saldo)
                    corriente = int(input(("¿Cuanto desea consignar?, recuerde que el saldo disponible es:",consignar)))
                    if corriente <= consignar:
                        print("================================================================")
                        print("Consignacion realizada con exito: $",corriente)
                        print("saldo disponible: ",consignar-corriente)
                        print("*Operacion finalizada*")
                        print("================================================================")
                        self.ingreso()
                    else:
                        if corriente > consignar:    
                         print("*Saldo insuficiente* ")
                         self.ingreso()
                        
                if cuenta == 4:
                    print("Cuando dinero desea retirar?: ")
                    print("Saldo disponible ","$",consignar)
                    retiro = int(input("$ = "))
                    if retiro <= consignar:
                       print("================================================================")
                       print("Retiro exitoso, su retiro fue de: ","$",retiro)
                       print("*Operacion finalizada*")
                       print("================================================================")
                       self.ingreso()
                    else:
                        if retiro > consignar:    
                         print("*Saldo insuficiente*")
                         print("===============================================================")
                         self.ingreso()
            else:
                if recargar == 2:
                    exit()
d = datos()
d.registro()
d.ingreso()


