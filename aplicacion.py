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
    
def listar_productos():
    print("\n Listar productos\n")
    with open('nombre.txt') as f:
        nombres = [line.rstrip('\n') for line in f]
        
    with open('codigo.txt') as f:
        codigos = [line.rstrip('\n') for line in f] 
            
    with open('precio.txt') as f:
        precios = [line.rstrip('\n') for line in f]
    
    productos = list(zip(nombres, codigos, precios))

    
    print(f"{'ID':<10}{'NOMBRE':<15}{'CODIGO':<20}{'PRECIO':<10}")
    print("-" * 50)
    
    for idx, p in enumerate(productos, start=1):
        print(f"{idx:<10}{p[0]:<15}{p[1]:<20}{p[2]:<10}")
    menu()

def agregar_productos():
    
    print("\n Agregar producto\n")
    nombre = input("Ingrese nombre: ")
    archivo1 = open("nombre.txt","at")
    archivo1.write("\n"+ nombre)
    archivo1.close()
    
    apellido = input("Ingrese codigo: ")
    archivo2 = open("codigo.txt","at")
    archivo2.write("\n"+ apellido)
    archivo2.close()
    
    dni = input("Ingrese precio: ")
    archivo3 = open("precio.txt","at")
    archivo3.write("\n"+ dni)
    archivo3.close()
    
    print("\nProducto agregado correctamente\n")
    menu()

def salir():
    sys.exit()
    
def menu():
    print("\nDatos Producto: \n1. Listar\n2. Agregar \n3. Salir")
    opcion = input("Opcion: ")
    if opcion == "1":
        listar_productos()
    elif opcion == "2":
        print("agregar")
        agregar_productos()
    elif opcion == "3":
        salir()
    else:
        print("\nOpcion no valida, ingrese nuevamente una opcion\n")
        menu()
login()