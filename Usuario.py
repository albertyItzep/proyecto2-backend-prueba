from logging import fatal
from pprint import pprint
import re


class Usuario():
    def __init__(self,nom,gen,corr,us,contras) -> None:
        self.__Nombre=nom
        self.__Genero=gen
        self.__Correo=corr
        self.__Usuario=us
        self.__Contrasena=contras
        self.largoP = 0
        


    def retornarNombre(self):
        return self.__Nombre
    def retornarGenero(self):
        return self.__Genero
    def retornarCorreo(self):
        return self.__Correo
    def retornarUsuario(self):
        return self.__Usuario
    def retornarContrasena(self):
        return self.__Contrasena
    def retornarlargo(self):
        return self.largoP
    def largoValores(self):
        a=False
        b=False
        c=False
        d=False
        e=False
        if len(self.__Nombre)>0:
            a=True
        else:
            a=False

        if len(self.__Genero)>0:
            b=True
        else:
            b=False

        if len(self.__Correo)>6:
            c=True
        else:
            c=False

        if len(self.__Usuario)>3:
            d=True
        else:
            d=False

        if len(self.__Contrasena)>=8:
            m= re.search(r"\d",self.__Contrasena)
            m1 = re.search(r"\W",self.__Contrasena)
            if m!=None and m1!=None:
                e=True
            else:
                e=False
        else:
            e=False
        
        if a==True and b==True and c==True and d==True and e==True:
            return True
        elif a==True and b==True and c==True and d==True and e==False:
            return "invalid password"
        else:
            return False

    def AsignarNombre(self,nombre):
        self.__Nombre=nombre
        print(self.__Nombre) 
    def AsignarGenero(self,genero):
        self.__Genero=genero
    def AsignarCorreo(self,correo):
        self.__Correo=correo
    def AsignarUsuario(self,usuario):
        self.__Usuario=usuario
    def AsignarContrasena(self,contrasena):
        self.__Contrasena=contrasena
    def AsignarLargo(self):
        self.largoP+=1
    def desasignarLargo(self):
        if self.largoP>0:
            self.largoP-=1
    def __gt__(self,usuario):
        return self.largoP>usuario.largoP
