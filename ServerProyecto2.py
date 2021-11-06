#hola a todos vamos a iniciar el proyecto 2 con python esta es la api para iniciar
import re
from flask import Flask, app ,jsonify
import json
from flask import request
from flask_cors import CORS
from Gestor import Gestor
from Usuario import Usuario
from Publicacion import Publicacion

# iniciando servidor
app = Flask(__name__)
# validaciones de cors
CORS(app)
# Almacenamiento general

administrador= Gestor()

@app.route('/')
def central():
    return "hello"

@app.route('/register',methods=['POST'])
def register():
    genero= request.json['genero']
    generom= genero.lower()
    datosUsuario= Usuario(request.json['nombre'],generom,request.json['correo'],request.json['usuario'],request.json['password']) 
    largo= datosUsuario.largoValores()
    if largo ==True:
        if administrador.validarUsuario(datosUsuario.retornarUsuario())=="Agregar":
            administrador.agregarUsuario(datosUsuario)
            return jsonify({"data":"true"})
        elif administrador.validarUsuario(datosUsuario.retornarUsuario())=="No agregar":
            return jsonify({"data":"false"})
    elif largo==False:
        return jsonify({"data":"todos los campos son necesario"})
    elif largo=="invalid password":
        return jsonify({"data":"invalid password"})
@app.route('/usuarioIngresado/<string:usuario>')
def usuarioIngresado(usuario):
    try:
        return administrador.retornarUsuarioIngresado(usuario)
    except Exception:
        return jsonify({"Json incorrecto"})
@app.route("/inicio/<usuario>/<string:password>",methods=['GET'])
def inicio(usuario=None,password=None):
        passwordE= password
        passwordE= passwordE.replace('~','#')
        print(passwordE)
        return jsonify(administrador.iniciarSesion(usuario,passwordE))

@app.route("/cargaUsuarios",methods=['POST'])
def cargaUsuarios():
    try:
        usuariosC= request.json["usuarios"]
        c =0
        for x in usuariosC:
            genero= x['gender']
            generom= genero.lower()
            nuevo = Usuario(x['name'],generom,x['email'],x['username'],x['password'])
            nuevo.largoP=c
            c+=1
            administrador.agregarUsuario(nuevo)
        administrador.recorrerUsuarios()
        return jsonify({"response":"true"})
    except Exception:
        return jsonify({"response":"Json incorrecto"})

@app.route("/cargaPublicaciones",methods=['POST'])
def cargarPublicaciones():
    try:
        publicacionesC = request.json['publicaciones']
        imagenes = publicacionesC['images']
        videos = publicacionesC['videos']
        for x in imagenes:
            nuevo = Publicacion("Imagen",x['url'],x['category'],x['author'],x['date'])
            administrador.agregarPublicaciones(nuevo)
        
        for x in videos:
            nuevo = Publicacion("Video",x['url'],x['category'],x['author'],x['date'])
            administrador.agregarPublicaciones(nuevo)
        return jsonify({"response":"true"})
    except Exception:
        return jsonify({"response":"false"})

@app.route('/obtenerUsuarios')
def obtenerUsuarios():
    hola=administrador.retornarUsuarios()
    return hola
@app.route('/borrarUsuario/<usuario>',methods=['DELETE'])
def borrarUsuario(usuario=None):
    print(usuario)
    datosR= administrador.borrarUsuarios(usuario)
    return datosR

@app.route('/editarUsuario',methods=['PUT'])
def editarUsuario():
    usuario = request.json['Usuario']
    #convertimos genero a minuscula
    genero= usuario['genero']
    generom= genero.lower()
    #creamos usuario
    usuarioAModificar= Usuario(usuario['nombre'],generom,usuario['correo'],usuario['usuario'],usuario['password'])
    llaveValor= usuario['datos']
    #validamos que los datos sean correctos
    largoCorrecto=usuarioAModificar.largoValores()
    if largoCorrecto == True:
        if administrador.editarUsuario(usuarioAModificar.retornarNombre(),usuarioAModificar.retornarGenero(),usuarioAModificar.retornarCorreo(),usuarioAModificar.retornarUsuario(),usuarioAModificar.retornarContrasena(),llaveValor) == "actualizado":
            return administrador.Obtenerusuarioos()
        else:
            return jsonify({"data":"Usuario a modificar Inexistente"})
    elif largoCorrecto== False:
        return jsonify({"data":"Datos requeridos"})
    elif largoCorrecto=="invalid password":
        return jsonify({"data":"Invalid Password"})

@app.route('/obtenerPublicaciones')
def obtenerPublicaciones():
    return administrador.ObtenerPublicaciones()
@app.route('/editarPublicacion',methods=['PUT'])
def editarpublicacion():
    publicacion = request.json['Publicacion']
    if administrador.editarPublicacion(publicacion['type'],publicacion['url'],publicacion['category'],publicacion['user'],publicacion['date'],publicacion['datekey'])=="actualizado":
        return administrador.ObtenerPublicaciones()
    else:
        return jsonify({"data":"inexistente"})
@app.route('/borrarPublicacion/<int:id>/<string:usuario>',methods=['DELETE'])
def borrarPublicacion(id,usuario):
    administrador.borrarPublicacion(id,usuario)
    return administrador.ObtenerPublicaciones()

#aca llamamos al vector ordenado de usuarios por mas publicaciones
@app.route('/verestadp')
def verP():
    return administrador.MasPublicaciones()

# datos para usuario diferente de admin
    # modificar usuario
@app.route('/usuarioM',methods=['PUT'])
def ModificarUsuario():
    usuario=request.json['usuario']
    print(usuario['keydate'])
    if usuario['keydate']==False:
        administrador.editarUsuario(usuario['nombre'],usuario['genero'],usuario['correo'],usuario['usuario'],usuario['password'],usuario['usuarioInicial'])
        return jsonify({"data":"true"})
    elif usuario['keydate']==True:
        print('bandera')
        if administrador.validarUsuario(usuario['usuario'])== "Agregar":
            print('bandera1 valorada')
            print(administrador.editarUsuario(usuario['nombre'],usuario['genero'],usuario['correo'],usuario['usuario'],usuario['password'],usuario['usuarioInicial']))
            return jsonify({"data":"true"})
        elif administrador.validarUsuario(usuario['usuario']) == "No agregar":
            return jsonify({"data":"false"})
    return jsonify({"data":"no se agrego"})

@app.route('/crearPublicacion',methods=['POST'])
def crearPublicacion():
    pAsignar = request.json['publicacion']
    nuevo = Publicacion(pAsignar['type'],pAsignar['url'],pAsignar['category'],pAsignar['author'],pAsignar['date'])
    if administrador.agregarPublicacion(nuevo)=="agregado":
        return jsonify({"data":"true"})
    else:
        return jsonify({"data":"false"})
#vamos a llamar al arreglo de publicaciones por mas likes
@app.route('/MasLikes')
def MasLikes():
    return administrador.MasLikes()

@app.route('/like/<int:id>')
def like(id):
    return jsonify({"data":administrador.agregarLike(id)})

@app.route('/graficsR/<string:user>')
def graficas(user):
    return administrador.retornargrafUs(user)
app.run(host="0.0.0.0", port=3000, debug=True)
