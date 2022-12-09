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
    while op < 0 or op > 4:
        print("\n1. agregar pelicula")
        print("2. buscar pelicula")
        print("3. buscar por director")
        print("4. buscar por genero")
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
    op_usuario = menu()
    while op_usuario != 0:
        if op_usuario == 1:
            print("USUARIO")
            print("sign in")
            nombre = input("Nombre: ")
            contrasena = input("Contrasena: ")
            usuario = app_sign_in(nombre, contrasena)
            if usuario == None:
                print("error al ingresar un dato")
                print("1. Reingresar")
                print("2. entrar como invitado")
                print("0. salir")
                op_ingreso = int(input("su opcion: "))
                if op_ingreso == 1:
                    continue
                if op_ingreso == 2:
                    usuario = 0
                    return usuario
                else:
                    break
            else:
                return usuario
        elif op_usuario == 2:
            usuario = 0
            return usuario
    

def mostar_peliculas():
    os.system("clear")
    print("----------------------- LISTA DE PELICULAS ---------------------")
    peliculas = app_mostrar_peliculas()
    for pelicula in peliculas:
        print(pelicula["titulo"])
        print("director:", pelicula["director"])
        print("anno:", pelicula["anno"])
        print("duracion:", pelicula["duracion"], "\n")

def buscar_pelicula(nombre):
    peliculas = app_mostrar_peliculas()
    for pelicula in peliculas:
        if pelicula["titulo"].lower() == nombre.lower():
            return pelicula["id"]
    else:
        return None

def mostrar_pelicula(id):
    pelicula = app_buscar_pelicula(id)
    #print("\n------", pelicula["titulo"].upper(), "------")
    print()
    os.system('echo "------ \033[1m"'+pelicula["titulo"].upper()+'"\033[0m ------"')
    for i in pelicula.keys():
        if i == "id" or i == "titulo":
            continue
        else:
            print(i, ": ", pelicula[i] ,sep='')
    print("\nCOMENTARIOS")
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
    while op < 0 or op > 7:
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
        if op.isalpha() or op =='':
            op = -1
        else:
            op = int(op)

        pelicula = app_buscar_pelicula(id)
        if op == 0:
            break
        elif op == 1:
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
        else:
            continue    
        app_modificar_pelicula(str(id), pelicula)

def eliminar_pelicula(id):
    app_eliminar_pelicula(str(id))

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

def modificar_comentario(id_pelicula, id_usuario):
    print("MODIFICAR COMENTARIO")
    id_comentario = int(input("ingrese el nro de su comentario: "))
    comentario = buscar_comentario(id_comentario, id_pelicula)
    if comentario == None:
        print ("El comentario no existe")
    elif comentario["id_usuario"] != id_usuario:
        print ("El comentario no lo hiciste vos")
    else:
        comentario["comentario"] = input("ingrese la modificacion de su comentario: ")
        app_modificar_comentario(str(comentario["id"]), comentario)

def eliminar_comentario(id_pelicula, id_usuario):
    print("ELIMINAR COMENTARIO")
    id_comentario = int(input("ingrese el nro de su comentario: "))
    comentario = buscar_comentario(id_comentario, id_pelicula)
    if comentario == None:
        print("el comentario no existe")
    elif comentario["id_usuario"] != id_usuario:
        print ("El comentario no lo hiciste vos")
    else:
        app_eliminar_comentario(str(comentario["id"]))

def lista_directores():
    peliculas = app_mostrar_peliculas()
    directores = []
    for pelicula in peliculas:
        directores.append(pelicula["director"])
    return set(directores)
    
def buscar_por_director(nombre):
    peliculas = app_mostrar_peliculas()
    lista_peliculas = []
    for pelicula in peliculas:
        if pelicula["director"].lower() == nombre.lower():
            lista_peliculas.append(pelicula["id"])
    return lista_peliculas

def mostrar_por_director():
    os.system("clear")
    print("BUSCAR POR DIRECTOR")
    directores = lista_directores()
    print ("lista de los directores")
    for director in directores:
        print(director, end="  |  ")
    print()

    nombre = input("Nombre del director: ")
    lista_peliculas = buscar_por_director(nombre)
    if lista_peliculas == []:
        print("No hay peliculas de ese director")
        c = input("Presione enter para volver... ")
    else:
        for pelicula in lista_peliculas:
            mostrar_pelicula(pelicula)
        c = input("Presione enter para volver... ")

def lista_generos():
    peliculas = app_mostrar_peliculas()
    generos = []
    for pelicula in peliculas:
        for genero in pelicula["genero"]:
            generos.append(genero)
    return set(generos)

def buscar_por_genero(genero):
    peliculas = app_mostrar_peliculas()
    lista_peliculas = []
    for pelicula in peliculas:
        for i in pelicula["genero"]:
            if i.lower() == genero.lower():
                lista_peliculas.append(pelicula["id"])
    return lista_peliculas

def mostrar_por_genero():
    os.system("clear")
    print("BUSCAR POR GENERO")
    generos = lista_generos()
    print("lista de generos")
    for genero in generos:
        print(genero, end="  |  ")
    print()
    nombre = input("Nombre del genero: ")
    lista_de_generos = buscar_por_genero(nombre)
    if lista_de_generos == []:
        print("ese genero no esta")
        c = input("Presione enter para volver...")
    else:
        for pelicula in lista_de_generos:
            mostrar_pelicula(pelicula)
        c = input("Presione enter para volver... ")

def mostar_ult_diez_peliculas():
    peliculas = app_mostrar_peliculas()
    print("----------------------- LISTA DE PELICULAS ---------------------")
    for i in range(-10, 0):
        pelicula = peliculas[i]
        print(pelicula["titulo"])
        print("director:", pelicula["director"])
        print("anno:", pelicula["anno"])
        print("duracion:", pelicula["duracion"], "\n")


def salir():
    print("chao")
    os.system("sleep 1")
    os.system("clear")
    
#--------------------------------------------------------------------------------------------
#main
usuario = ingreso()

while True:
    if usuario == None:
        salir()
        break
    elif usuario != 0:
        mostar_peliculas()
        
        op_menu_usuario = menu_usuario()
        while op_menu_usuario != 0:
            if op_menu_usuario == 1:
                agregar_pelicula()
                break
            elif op_menu_usuario == 2:
                mostar_peliculas()
                print("BUSCAR PELICULA")
                nombre = input("Ingrese el nombre de la pelicula: ")
                id_pelicula = buscar_pelicula(nombre)
                if id_pelicula == None:
                    print("La pelicula no esta cargada")
                    os.system("sleep 1")
                    break   
                else:
                    os.system("clear")
                    mostrar_pelicula(id_pelicula)
                    op_menu_pelicula = menu_pelicula()
                    #while op_menu_pelicula?
                    if op_menu_pelicula == 1:
                        crear_comentario(usuario, id_pelicula)
                    elif op_menu_pelicula == 2:
                        mostrar_tus_comentarios(usuario["id"], id_pelicula)
                        op_menu_comentarios = menu_comentarios()
                        while op_menu_comentarios != 0:
                            if op_menu_comentarios == 1:
                                modificar_comentario(id_pelicula, usuario["id"])
                                break
                            elif op_menu_comentarios == 2:
                                eliminar_comentario(id_pelicula, usuario["id"])
                                break
                        else:
                            break
                    elif op_menu_pelicula == 3:
                        modificar_pelicula(id_pelicula)
                        break
                    elif op_menu_pelicula == 4:
                        eliminar_pelicula(id_pelicula)
                        break
            elif op_menu_usuario == 3:
                mostrar_por_director()
                break
                
            elif op_menu_usuario == 4:
                mostrar_por_genero()
                break
            else:
                print("salistes")
                os.system("sleep 3")
                break 
        else: # else de op_menu_usuario
            salir()
            break

    #con ingreso de usuario invitado
    elif usuario == 0:
        op_invitado = -1
        os.system("clear")
        while op_invitado < 0 or op_invitado > 3:
            mostar_ult_diez_peliculas()
            print("1. buscar pelicula")
            print("2. buscar por director")
            print("3. buscar por genero"            )
            print("0. salir")
            op_invitado = input("ingrese su opcion: ")
            if op_invitado.isalpha() or op_invitado == '':
                op_invitado = -1
            else:
                op_invitado = int(op_invitado)

            if op_invitado == 1:
                print("BUSCAR PELICULA")
                nombre = input("Ingrese el nombre de la pelicula: ")
                id_pelicula = buscar_pelicula(nombre)
                if id_pelicula == None:
                    print("La pelicula no esta cargada")
                    os.system("sleep 1")
                    break
                else:
                    mostrar_pelicula(id_pelicula)
                    c = input("\npresione enter para volver... ")
                    break
            elif op_invitado == 2:
                mostrar_por_director()
                break
            elif op_invitado == 3:
                mostrar_por_genero()
                break
        else:
            salir()
            break