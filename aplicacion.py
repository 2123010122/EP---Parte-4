import time
import sys
#ABRE EL LOGIN.TXT Y LEE EL USUARIO
login = open ("usuarios.txt","rt")
login_user = login.read()

#ABRE EL CLAVE.TXT Y LEE LA CLAVE
clave = open ("claves.txt","rt")
clave_user = clave.read()

#VALIDA QUE EL USUARO Y EL LOGIN SEAN CORRECTOS
def login():
    confirmacion=0
    while confirmacion <=2:
        
        login=input("Ingrese usuario: ")
        clave=input("Ingrese clave: ")
        
        if login == login_user and clave == clave_user:
            print("\nUsuario y Clave correcto")
            menu()
        else:
            confirmacion+=1
            print("Usuario y/o clave incorrectos.\n Intente nuevamente.\n")
    print("Se equivoco mas de tres veces") 
    time.sleep(3)
    
def menu():
    print("\nDatos Producto: \n1. Listar\n2. Agregar \n3. Salir")
    opcion = input("Opcion: ")
    if opcion == "1":
        print("listar")
        #listar_personas()
    elif opcion == "2":
        print("agregar")
        #agregar_personas()
    elif opcion == "3":
        print("salir")
        print("salir")
       #salir()
    else:
        print("\nOpcion no valida, ingrese nuevamente una opcion\n")
        menu()
login()