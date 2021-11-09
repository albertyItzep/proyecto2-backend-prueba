# aca vamos a tener todos los datos en movimiento
from datetime import date
from os import terminal_size
from flask.json import jsonify
from Usuario import Usuario
from Publicacion import Publicacion
import json
import re
import random
class Gestor():
    def __init__(self) -> None:
        self.__Publicaciones = []
        self.__Usuarios=[]
        self.__Usuarios.append(Usuario('Fernando Cardona','m','admin@ipc1.com','admin','admin@ipc1'))      
        self.__Usuarios.append(Usuario('Albertt Itzep','m','alberttitzep123@gmail.com','angor123','sistemas123@'))
        self.__Publicaciones.append(Publicacion('Imagen','https://cdn.pixabay.com/photo/2021/10/19/12/30/elephant-6723452_960_720.jpg','Cultura','jose','12/12/2020'))
        self.__Publicaciones.append(Publicacion('Imagen','https://cdn.pixabay.com/photo/2021/09/22/00/28/kitten-6645241_960_720.jpg','Deportes','jose123','08/09/2021'))
        self.__Publicaciones.append(Publicacion('Imagen','https://cdn.pixabay.com/photo/2021/07/20/18/19/bald-eagle-6481346_960_720.jpg','Niños','pedrito123','12/06/2021'))
        self.__Publicaciones.append(Publicacion('Video','https://youtu.be/JpoEFiAJdxo','Cultura','pedrito123','23/09/2021'))
        self.__Publicaciones.append(Publicacion('Video','https://www.youtube.com/watch?v=rsTLyukvxGU','Internacional','pedrito123','22/07/2021'))
        self.__Publicaciones.append(Publicacion('Video','https://www.youtube.com/watch?v=rsTLyukvxGU','Actualidad','jose123','13/07/2021'))
    def validarUsuario(self,usuario):
        for x in self.__Usuarios:
            if x.retornarUsuario()==usuario:
                return "No agregar"
        return "Agregar"

    def iniciarSesion(self,usuario,contrasena):
        if len(usuario)>0 and len(contrasena)>0:
            if usuario != "admin":    
                for x in self.__Usuarios:
                    if(x.retornarUsuario()==usuario):
                        if (x.retornarContrasena()==contrasena):
                            print(json.dumps(x.__dict__))
                            return {"data":"true"}
                        else:
                            return {"data":"contrasena incorrecta"}               
                return {"data":"false"}
            elif usuario == "admin":
                if contrasena == "admin@ipc1":
                    return {"data":"admin"} 
                else:
                    return {"data":"contrasena incorrecta"}
    def retornarUsuarioIngresado(self,usuario):
        for x in self.__Usuarios:
            if(x.retornarUsuario()== usuario):
                return json.dumps(x.__dict__)
    #proceso de agregar actualizar y eliminar
    def agregarUsuario(self, usuario):
        self.__Usuarios.append(usuario)
    
    def agregarPublicaciones(self,publicacion):
        self.__Publicaciones.append(publicacion)
    def recorrerUsuarios(self):
        for x in self.__Usuarios:
            print(x.__dict__)
    
    def retornarUsuarios(self):
        arrJson=[]
        for x in self.__Usuarios:
            arrJson.append((x.__dict__))
        return json.dumps(arrJson)

    def borrarUsuarios(self,usuarioE):
        arrJson=[]
        contador=0
        for x in self.__Usuarios:
            if x.retornarUsuario() == usuarioE:
                print(x.retornarUsuario())
                self.__Usuarios.remove(x)
                break
        for x in self.__Usuarios:
            arrJson.append((x.__dict__))
        return json.dumps(arrJson)

    def editarUsuario(self,nombre,genero,correo,usuario,contrana,dato):
        for x in self.__Usuarios:
            if x.retornarUsuario()==dato:
                self.__Usuarios[self.__Usuarios.index(x)]=Usuario(nombre,genero,correo,usuario,contrana)
                return "actualizado"
    def editarPublicacion(self,type,url,category,user,date,id):
        self.__Publicaciones[id] = Publicacion(type,url,category,user,date)
        return "actualizado"

    def Obtenerusuarioos(self):
        return json.dumps([ob.__dict__ for ob in self.__Usuarios])
    def ObtenerPublicaciones(self):
        return json.dumps([ob.__dict__ for ob in self.__Publicaciones])
    def borrarPublicacion(self,id,usuario):
        self.__Publicaciones.pop(id)
        for x in self.__Usuarios:
            if x.retornarUsuario()==usuario:
                x.desasignarLargo()
                print(x.retornarlargo())
                break

    #usuario con mas publicaciones
    def MasPublicaciones(self):
        self.__Usuarios=sorted(self.__Usuarios,reverse=True)
        return json.dumps([ob.__dict__ for ob in self.__Usuarios])
    #publicacion con mas likes
    def MasLikes(self):
        self.__Publicaciones=sorted(self.__Publicaciones,reverse=True)
        return json.dumps([ob.__dict__ for ob in self.__Publicaciones])
    def agregarLike(self,id):
        self.__Publicaciones[id].asignarlike1()
        valor = (self.__Publicaciones[id])
        return valor.__dict__
    def quitarLike(self,id):
        self.__Publicaciones[id].quitarLike()
        valor = (self.__Publicaciones[id])
        return valor.__dict__
    # agregar a un usuario una publicacion
    def agregarPublicacion(self,publicacion):
        for x in self.__Usuarios:
            if x.retornarUsuario()==publicacion.retornarUser():
                x.AsignarLargo()
                print(x.retornarlargo())
                self.__Publicaciones.append(publicacion)
                return "agregado"
        return "no agregado" 

    def retornargrafUs(self,usuario):
        publicacionesUsuario=[]
        for x in self.__Publicaciones:
            if x.retornarUser()== usuario:
                publicacionesUsuario.append(x)
        return json.dumps([ob.__dict__ for ob in publicacionesUsuario])