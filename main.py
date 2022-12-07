import requests
import os

my_url = "http://127.0.0.1:5000"
#app.py
#usuario
def app_sign_in(nombre,contrasena):
    r = requests.get(my_url+"/sign-in/"+nombre+"/"+contrasena)
    if r.ok:
        return r.json()
    else:
        return None

def app_mostar_peliculas():
    r = requests.get(my_url+"/peliculas")
    return r.json()

def app_buscar_pelicula(id):
    id = str(id)
    r = requests.get(my_url+"/peliculas/"+id)
    if r.ok:
        return r.json()
    else:
        return None

def app_agregar_pelicula(pelicula):
    requests.post(my_url+"/peliculas", json=pelicula)

def app_modificar_pelicula(id, pelicula):
    requests.put(my_url+"/peliculas/"+id, json=pelicula)
    
def app_eliminar_pelicula(id):
    requests.delete(my_url+"/peliculas/"+id)
#--------------------------------------------------------------------------------------------
#main.py
def menu():
    op = -1
    while op < 0 or op > 2:
        os.system("clear")
        print("----------Menu----------")
        print("ingresesu tipo de usuario")
        print("1. Ingresar usuario")
        print("2. Ingresar como invitado")
        print("0. Salir")
        op = input("ingrese su opcion: ")
        if op.isalpha():
            op = -1
        else:
            op = int(op)
    return op

def menu_usuario():
    op = -1
    while op < 0 or op > 2:
        print("\n1. agregar pelicula")
        print("2. buscar pelicula")
        print('0. volver')
        op = input("ingrese su opcion: ")
        if op.isalpha():
            op = -1
        else:
            op = int(op)
    return op

def menu_pelicula():
    op = -1
    while op < 0 or op > 3:
        print("\n1. ver mis comentarios de la pelicula")
        print("2. modificar pelicula")
        print("3. eliminar pelicula")
        print('0. volver')
        op = input("ingrese su opcion: ")
        if op.isalpha():
            op = -1
        else:
            op = int(op)
    return op

def menu_comentarios():
    op = -1
    while op < 0 or op > 2:
        print("1. modificar comentario")
        print("2. eliminar comentario")
        print("0. volver")
        op = input("ingrese su opcion: ")
        if op.isalpha():
            op = -1
        else:
            op = int(op)
    return op
    

def ingreso():
    #os.system("clear")
    print("USUARIO")
    print("sign in")
    nombre = input("Nombre: ")
    contrasena = input("Contrasena: ")
    usuario = app_sign_in(nombre, contrasena)
    
    if usuario == None:
        return None
    else:
        flag = 0
        return usuario

def mostar_peliculas():
    peliculas = app_mostar_peliculas()
    for pelicula in peliculas["peliculas"]:
        if pelicula == {}:
            continue
        else:
            print(pelicula["titulo"])
            print(pelicula["director"])
            print(pelicula["anno"])
            print(pelicula["duracion"], "\n")

def buscar_pelicula(nombre):
    peliculas = app_mostar_peliculas()
    for pelicula in peliculas["peliculas"]:
        if pelicula == {}:
            continue
        elif pelicula["titulo"].lower() == nombre.lower():
            return pelicula["id"]
    else:
        return None

def mostrar_pelicula(id):
    pelicula = app_buscar_pelicula(id)
    for i in pelicula.keys():
        if i == "id":
            continue
        else:
            print(i, ": ", pelicula[i] ,sep='')

def agregar_pelicula():
    pelicula = {}
    print("para agregar una pelicula se necesitan los siguientes datos:")
    pelicula["titulo"] = input("titulo: ")
    pelicula["anno"] = input("anno: ")
    pelicula["director"] = input("director: ")
    pelicula["duracion"] = input("duracion: ")
    pelicula["genero"] = input("genero: ").split(", ")
    pelicula["sinopsis"] = input("sinopsis: ")
    pelicula["poster"] = input("poster: ")
    app_agregar_pelicula(pelicula)

def modificar_pelicula(id):
    op = -1
    while op != 0:
        print("MODIFICAR PELICULA")
        print("1. titulo")
        print("2. anno")
        print("3. director")
        print("4. duracion")
        print("5. genero")
        print("6. sinopsis")
        print("7. poster")
        print("0. volver")
        op = input("ingrese numero del dato que quiere modificar: ")

    pelicula = app_buscar_pelicula(id)
    if op == 1:
        pelicula["titulo"] = input("titulo: ")
    elif op == 2:
        pelicula["anno"] = input("anno: ")
    elif op == 3:
        pelicula["director"] = input("director: ")
    elif op == 4:
        pelicula["duracion"] = input("duracion: ")
    elif op == 5:
        pelicula["genero"] = input("genero: ").split(", ")
    elif op == 6:
        pelicula["sinopsis"] = input("sinopsis: ")
    elif op == 7:
        pelicula["poster"] = input("poster: ")
    app_modificar_pelicula(id, pelicula)

def eliminar_pelicula(id):
    app_eliminar_pelicula(id)

#def mostar_comentarios(id_pelicula):



#--------------------------------------------------------------------------------------------
#main

op_usuario = menu()
while op_usuario != 0:
    if op_usuario == 1:
        usuario = ingreso()
        if usuario == None:
            print("error al ingresar un dato")
            print("1. Reingresar")
            print("0. volver")
            op_ingreso = int(input("su opcion: "))
            if op_ingreso == 1:
                usuario = ingreso()
            else:
                op_usuario = menu()
                continue
        #os.system("clear")
        mostar_peliculas()
        
        op_menu_usuario = menu_usuario()
        while op_menu_usuario != 0:
            if op_menu_usuario == 1:
                #os.system("clear")
                print("AGREGAR PELICULA")
                agregar_pelicula()
            elif op_menu_usuario == 2:
                #os.system("clear")
                print("BUSCAR PELICULA")
                nombre = input("Ingrese el nombre de la pelicula: ")
                id_pelicula = buscar_pelicula(nombre)
                if id_pelicula == None:
                    print("La pelicula no esta cargada")
                    op_menu_usuario = menu_usuario()
                    continue   
                
                mostrar_pelicula(id_pelicula)
                
                op_menu_pelicula = menu_pelicula()
                if op_menu_pelicula == 1:
                    #mostar_comentarios(id_pelicula)
                    op_comentario = -1
                    while op_comentario != 0 or op_comentario != 1:
                        print("1. buscar comentario")
                        print("0. volver")
                        op_comentario = input("ingrese su opcion: ")
                        if op_comentario.isalpha():
                            op_comentario = -1
                        else:
                            op_comentario = int(op_comentario)
                    if op_comentario == 0:
                        op_menu_pelicula = menu_pelicula()
                    else:
                        comentario = input("ingrese el id del comentario: ")
                        id_comentario = buscar_comentario(comentario)
                        if id_comentario == None:
                            print("El comentario no existe")
                        else:    
                            #mostrar_comentario(id_comentario)
                            op_menu_comentario = menu_comentarios()
                            #while op_menu_cometario?
                elif op_menu_pelicula == 2:
                    modificar_pelicula(id_pelicula)
                elif op_menu_pelicula == 3:
                    eliminar_pelicula(id_pelicula)
            
            else: # else de op_menu_usuario
                continue

        



    #con ingreso de usuario invitado
    elif op_usuario == 2:
        print("a")
