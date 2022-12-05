from flask import Flask, jsonify, Response, request
from http import HTTPStatus
import json

app = Flask(__name__)

usuarios = json.load(open("json/usuarios.json"))
peliculas = json.load(open("json/peliculas.json"))
comentarios = json.load(open("json/comentarios.json"))



@app.route("/")
def home():
    return usuarios

#Usuarios
@app.route("/sign-in/<nombre>/<contrasena>", methods=["GET"])
def sign_in(nombre,contrasena):
    #le paso el nombre y la contrasena por url porque no se ve y se puede realizar un metodo GET
    #datos_usuario = request.get_json()
    bool_nick = False
    bool_contra = False

    for usuario in usuarios["usuarios"]:
        if usuario["nombre"] == nombre:
            bool_nick = True
            break
    
    for usuario in usuarios["usuarios"]:
        if usuario["contrasena"] == contrasena:
            bool_contra = True
            break

    if bool_nick and bool_contra:
        return usuario
    else:
        return Response("Error al ingresar un dato", status=HTTPStatus.BAD_REQUEST)


#Peliculas
@app.route("/peliculas")
def mostrar_peliculas():
    lista_peliculas =[]
    for pelicula in peliculas["peliculas"]:
        lista_peliculas.append(pelicula["titulo"], pelicula["anno"], pelicula["director"])
    return lista_peliculas