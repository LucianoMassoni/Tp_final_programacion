import requests
import os

url = "http://127.0.0.1:5000"
#usuario
def sign_in(nombre,contrasena):
    r = requests.get(url+"/sign-in/"+nombre+"/"+contrasena)
    if r.ok:
        return r.json()
    else:
        return None

def ingreso():
    flag = 1
    op = 1
    while flag != 0 and op != 0:
        #os.system("clear")
        print("USUARIO")
        print("sign in")
        nombre = input("Nombre: ")
        contrasena = input("Contrasena: ")
        usuario = sign_in(nombre, contrasena)
        
        if usuario == None:
            print("error al ingresar un dato")
            print("1. Reingresar")
            print("0. volver")
            op = int(input("su opcion: "))
            if op == 1:
                flag = 1
                op = 1
            else:
                return None
        else:
            flag = 0
            return usuario
#main
op_usuario = -1
while op_usuario != 0:
    os.system("clear")
    print("----------Menu----------")
    print("ingresesu tipo de usuario")
    print("1. Ingresar usuario")
    print("2. Ingresar como invitado")
    print("0. Salir")
    op_usuario = int(input("op: "))

    #con ingreso de usuario.
    if op_usuario == 1:
        usuario = ingreso()
        
