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
        if usuario["nombre"] == nombre and usuario["contrasena"] == contrasena:
            return usuario
    else:
        return Response("Error al ingresar un dato", status=HTTPStatus.BAD_REQUEST)


#Peliculas
@app.route("/peliculas")
def mostrar_peliculas():
    lista_peliculas =[]
    for pelicula in peliculas["peliculas"]:
        dic_pelicula = {
            "id": pelicula["id"],
            "titulo": pelicula["titulo"], 
            "anno": pelicula["anno"],
            "director": pelicula["director"]
        }
        lista_peliculas.append(dic_pelicula)
    return lista_peliculas
#o puedo devovler las peliculas enteras y filtrar desde el programa, veo que onda despues


@app.route("/peliculas/<id>")
def info_pelicula(id):
    int_id = int(id)
    for pelicula in peliculas["peliculas"]:
        if pelicula["id"] == int_id:
            return pelicula
    else:
        return Response({}, status=HTTPStatus.BAD_REQUEST)


@app.route("/peliculas", methods=["POST"])
def cargar_pelicula():
    ult_id = len(peliculas["peliculas"]) + 1       
    
    datos_pelicula = request.get_json()
    for pelicula in peliculas["peliculas"]:
        if pelicula["titulo"].lower() == datos_pelicula["titulo"].lower():
            return Response("La pelicula ya existe", status=HTTPStatus.BAD_REQUEST)
    else:
        datos_pelicula["id"] = ult_id
        peliculas["peliculas"].append(datos_pelicula)
        with open ("json/peliculas.json", "w") as f:
            json.dump(peliculas, f, indent=4)
            f.close()
        return Response(datos_pelicula, status=HTTPStatus.OK)


@app.route("/peliculas/<id>", methods=["PUT"])
def modificar_pelicula(id):
    int_id = int(id)
    datos_pelicula = request.get_json()

    for pelicula in peliculas["peliculas"]:
        if pelicula == {}:                  #cuando se clearea un dict queda asi, vacio; Si esta asi pasa al siguiente
            continue
        elif pelicula["id"] == int_id:
            #En el for, la i itera sobre las peliculas, la k sobre los datos; a pelicula sub key le da el dato sub la misma key.
            for i, k in zip(pelicula.keys(), datos_pelicula.keys()):
                pelicula[i] = datos_pelicula[i]
            
            with open ("json/peliculas.json", "w") as f:
                json.dump(peliculas, f, indent=4)
                f.close()
            return Response("modificada con exito", status=HTTPStatus.OK)
    else:
        return Response("La pelicula no existe", status=HTTPStatus.BAD_REQUEST)


@app.route("/peliculas/<id>", methods=["DELETE"])
def eliminar_pelicula(id):
    int_id = int(id)
    for pelicula in peliculas["peliculas"]:
        if pelicula == {}:                  #cuando se clearea un dict queda asi, vacio; Si esta asi pasa al siguiente
            continue
        elif pelicula["id"] == int_id:
            pelicula.clear()
            with open ("json/peliculas.json", "w") as f:
                json.dump(peliculas, f, indent=4)
                f.close()
            return Response("La pelicula se borro con exito", status=HTTPStatus.OK)
    else:
        return Response("La pelicula no existe", status=HTTPStatus.BAD_REQUEST)

#comentarios
@app.route("/peliculas/<id_peli>/comentarios")
def mostrar_comentario_pelicula(id_peli):
    id_peli= int(id_peli)
    lista_comentarios = []
    for comentario in comentarios["comentarios"]:
        if comentario == {}:
            continue
        elif comentario["id_pelicula"] == id_peli:
            lista_comentarios.append(comentario)
    return lista_comentarios

@app.route("/<id_usuario>/peliculas/<id_pelicula>/comentarios", methods=["POST"])
def crear_comentario_pelicula(id_usuario, id_pelicula):
    id_pelicula = int(id_pelicula)
    id_comentario = len(comentarios["comentarios"]) + 1
    print(id_comentario)
    datos_comentario = request.get_json()
    for pelicula in peliculas["peliculas"]:
        if pelicula == {}:
            continue
        elif pelicula["id"] == id_pelicula:
            datos_comentario["id"] = id_comentario
            datos_comentario["id_usuario"] = int(id_usuario)
            datos_comentario["id_pelicula"] = id_pelicula
            comentarios["comentarios"].append(datos_comentario)
            with open ("json/comentarios.json", "w") as f:
                json.dump(comentarios, f, indent=4)
                f.close()
            return Response("Comentario hecho con exito", status=HTTPStatus.OK)
    else:
        return Response("Error al ingresar un dato", status=HTTPStatus.BAD_REQUEST)

@app.route("/<id_usuario>/comentario/<id_comentario>", methods=["PUT"])
def modificar_comentario(id_usuario, id_comentario):
    id_comentario = int(id_comentario)
    id_usuario = int(id_usuario)
    datos_comentario = request.get_json()

    for comentario in comentarios["comentarios"]:
        if comentario == {}:
            continue
        elif comentario["id"] == id_comentario and comentario["id_usuario"] == id_usuario:
            comentario["comentario"] = datos_comentario["comentario"]
            with open ("json/comentarios.json", "w") as f:
                json.dump(comentarios, f, indent=4)
                f.close()
            return Response("cambio hecho con exito", status=HTTPStatus.OK)
    else:
        return Response("Error al ingresar un dato", status=HTTPStatus.BAD_REQUEST)


@app.route("/<id_usuario>/comentario/<id_comentario>", methods=["DELETE"])
def eliminar_comentario(id_usuario , id_comentario):
    id_comentario = int(id_comentario)
    id_usuario = int(id_usuario)

    for comentario in comentarios["comentarios"]:
        if comentario == {}:
            continue
        elif comentario["id"] == id_comentario and comentario["id_usuario"] == id_usuario:
            comentario.clear()
            with open ("json/comentarios.json", "w") as f:
                json.dump(comentarios, f, indent=4)
                f.close()
            return Response("su comentario se ha borrado", status=HTTPStatus.OK)
    else:
        return Response("El comentario no existe o no tienes la autorizacion", status=HTTPStatus.BAD_REQUEST)