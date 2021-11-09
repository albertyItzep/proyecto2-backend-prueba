
from _typeshed import Self


class Publicacion():
    def __init__(self,Type,Url,Category,User,date) -> None:
        self.__User=User
        self.__Type=Type
        self.__Url=Url
        self.__Date=date
        self.__Category=Category
        self.Like=0

    def retornarType(self):
        return self.__Type
    def retornarUrl(self):
        return self.__Url
    def retornarDate(self):
        return self.__Date
    def retornarCategory(self):
        return self.__Category
    def retornarLike(self):
        return self.Like
    def retornarUser(self):
        return self.__User

    def asignarType(self,typeP):
        self.__Type=typeP
    def asignarUrl(self,url):
        self.__Url=url
    def asignarDate(self,date):
        self.__Date=date
    def asignarCategory(self,category):
        self.__Category=category
    def asignarLike(self,like):
        self.Like+=like
    def asignarlike1(self):
        self.Like+=1
    def asignarUser(self,user):
        self.__User=user
    def quitarLike(self):
        self.Like= self.Like-1
    def __gt__(self,publicacion):
        return self.Like>publicacion.Like

