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

def app_mostrar_peliculas():
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

def app_mostar_comentarios(id_pelicula):
    r = requests.get(my_url+"/peliculas/"+id_pelicula+"/comentarios")
    if r.ok:
        return r.json()
    else:
        return None

def app_crear_comentario(id_usuario, id_pelicula, comentario):
    requests.post(my_url+"/"+id_usuario+"/peliculas/"+id_pelicula+"/comentarios", json=comentario)

def app_modificar_comentario(id_comentario, comentario):
    requests.put(my_url+"/comentario/"+id_comentario, json=comentario)

def app_eliminar_comentario(id_comentario):
    requests.delete(my_url+"/comentario/"+id_comentario)

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
    while op < 0 or op > 4:
        print("\n1. agregar comentario")
        print("2. ver mis comentarios de la pelicula")
        print("3. modificar pelicula")
        print("4. eliminar pelicula")
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
        print("\n1. modificar comentario")
        print("2. eliminar comentario")
        print("0. volver")
        op = input("ingrese su opcion: ")
        if op.isalpha():
            op = -1
        else:
            op = int(op)
    return op
    

def ingreso():
    os.system("clear")
    print("USUARIO")
    print("sign in")
    nombre = input("Nombre: ")
    contrasena = input("Contrasena: ")
    usuario = app_sign_in(nombre, contrasena)
    
    if usuario == None:
        return None
    else:
        return usuario

def mostar_peliculas():
    peliculas = app_mostrar_peliculas()
    for pelicula in peliculas["peliculas"]:
        if pelicula == {}:
            continue
        else:
            print(pelicula["titulo"])
            print(pelicula["director"])
            print(pelicula["anno"])
            print(pelicula["duracion"], "\n")

def buscar_pelicula(nombre):
    peliculas = app_mostrar_peliculas()
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
    print("COMENTARIOS")
    comentarios = app_mostar_comentarios(str(id))
    for comentario in comentarios:
        print(comentario["nombre_usuario"],": ", comentario["comentario"], sep="")

def agregar_pelicula():
    print("AGREGAR PELICULA")
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

#comentarios--
def crear_comentario(usuario, id_pelicula):
    comentario = {}
    print("CREAR COMENTARIO")
    comentario["comentario"] = input("Ingrese su comentario: ")
    comentario["nombre_usuario"] = usuario["nombre"]
    app_crear_comentario(str(usuario["id"]), str(id_pelicula), comentario)

def buscar_tus_comentarios(id_usuario, id_pelicula):
    comentarios = app_mostar_comentarios(str(id_pelicula))
    lista_comentarios = []
    for comentario in comentarios:
        if comentario["id_usuario"] == id_usuario:
            lista_comentarios.append(comentario)
    return lista_comentarios


def mostrar_tus_comentarios(id_usuario, id_pelicula):
    comentarios = buscar_tus_comentarios(id_usuario, id_pelicula)
    for comentario in comentarios:
        print("nro.", comentario["id"],"|", comentario["nombre_usuario"],": ", comentario["comentario"], sep="")
        
def buscar_comentario(id, id_pelicula):
    comentarios = app_mostar_comentarios(str(id_pelicula))
    for comentario in comentarios:
        if comentario["id"] == id:
            return comentario
    else:
        return None

def modificar_comentario(id_pelicula):
    print("MODIFICAR COMENTARIO")
    id_comentario = int(input("ingrese el nro de su comentario: "))
    comentario = buscar_comentario(id_comentario, id_pelicula)
    print(comentario)
    if comentario == None:
        return "El comentario no existe"
    else:
        
        comentario["comentario"] = input("ingrese la modificacion de su comentario: ")
        app_modificar_comentario(str(comentario["id"]), comentario)

def eliminar_comentario(id_pelicula):
    print("ELIMINAR COMENTARIO")
    id_comentario = int(input("ingrese el nro de su comentario: "))
    comentario = buscar_comentario(id_comentario, id_pelicula)
    if comentario == None:
        print("el comentario no existe")
    else:
        app_eliminar_comentario(str(comentario["id"]))
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
                    crear_comentario(usuario, id_pelicula)
                elif op_menu_pelicula == 2:
                    mostrar_tus_comentarios(usuario["id"], id_pelicula)
                    op_menu_comentarios = menu_comentarios()
                    while op_menu_comentarios != 0:
                        if op_menu_comentarios == 1:
                            modificar_comentario(id_pelicula)
                            op_menu_comentarios = menu_comentarios()
                            continue
                        elif op_menu_comentarios == 2:
                            eliminar_comentario(id_pelicula)
                            op_menu_comentarios = menu_comentarios()
                            continue
                        else:
                            break

                elif op_menu_pelicula == 3:
                    modificar_pelicula(id_pelicula)
                elif op_menu_pelicula == 4:
                    eliminar_pelicula(id_pelicula)
            
            else: # else de op_menu_usuario
                continue

        



    #con ingreso de usuario invitado
    elif op_usuario == 2:
        print("a")
