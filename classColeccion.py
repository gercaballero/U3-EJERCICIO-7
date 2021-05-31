from classNodo import Nodo
from zope.interface import Interface
from zope.interface import implementer
from InterfaceLista import ILista
from classPersonal import Personal
from classDocente import Docente
from classInvestigador import Investigador
from classPApoyo import PersonalApoyo
from classDocenteInvestigador import DocenteInvestigador
import os
@implementer(ILista)
class Lista:
    __comienzo=None
    __actual=None
    __indice=0
    __tope=0

    def __init__(self):
        self.__comienzo=None
        self.__actual=None
    def __iter__(self):
        return self

    def __next__(self):
        if self.__indice==self.__tope:
            self.__actual=self.__comienzo
            self.__indice=0
            raise StopIteration
        else:
            self.__indice+=1
            dato = self.__actual.getDato()
            self.__actual=self.__actual.getSiguiente()
            return dato
    def listar(self): #Metodo para listar completamente
        os.system('cls')
        print('-----------------------------------------------------')
        aux=self.__comienzo
        if aux != None:
            while aux!=None:
                aux.getDato().mostrarDatos()
                print('-----------------------------------------------------')
                aux=aux.getSiguiente()
        else:
            print('LISTA VACIA')

    def insertarElemento(self,elemento,posicion): #Metodo para insertar un elemento en una posicion deseada
        nodo=Nodo(elemento)
        aux=self.__comienzo
        if posicion>=0 and (self.__tope==posicion==0 or posicion<self.__tope):
            #PREGUNTA SI LA POSICION DESEADA ESTA ENTRE 0 Y EL TOPE
            if aux==None or posicion==0:
                #SI LA POSICION ES EL PRIMER LUGAR O LA LISTA ESTABA VACIA
                nodo.setSiguiente(self.__comienzo)
                self.__comienzo=nodo
                self.__actual=self.__comienzo
                self.__tope+=1      #AUMENTA EL TOPE POR QUE SE AGREGO UN ELEMENTO
            else:
                while self.__indice!=posicion:  #ITERA HASTA ENCONTRAR LA POSICION
                    ant=aux
                    aux=aux.getSiguiente()
                    self.__indice+=1
                ant.setSiguiente(nodo)
                nodo.setSiguiente(aux)
                self.__indice=0
                self.__tope+=1
                print('EL ELEMENTO SE INSERTO EN LA POSICION ',posicion)
        else:
            print('NO EXISTE LA POSICION {} EN LA LISTA ENLAZADA:'.format(posicion))
        
    def agregarElemento(self,elemento): #METODO PARA INSERTAR UN ELEMENTO AL FINAL DE LA LISTA
        nodo=Nodo(elemento)
        aux=self.__comienzo
        if aux==None:
            nodo.setSiguiente(self.__comienzo)
            self.__comienzo=nodo
            self.__actual=self.__comienzo
            self.__tope+=1
        else:
            ant=aux
            aux=aux.getSiguiente()
            while aux!=None:
                ant=aux
                aux=aux.getSiguiente()
            ant.setSiguiente(nodo)
            nodo.setSiguiente(aux)
            self.__tope+=1
    
    def tipoPosicion(self,posicion):    #SABER EL TIPO DE AGENTE EN CIERTA POSICION
        aux=self.__comienzo
        if posicion>=0 and (self.__tope==posicion==0 or posicion<self.__tope):
            if aux!=None:
                while self.__indice!=posicion:
                    aux=aux.getSiguiente()
                    self.__indice+=1
                if isinstance(aux.getDato(), DocenteInvestigador):  #PRIMERO QUE TODO VERIFICA SI ES DOCENTEINVESTIGADOR
                    #YA QUE SI PRIMERO VERIFICA DOCENTE O INVESTIGADOR NOS DARIA TIPO INCORRECTO
                    print('TIPO DE OBJETO ES DOCENTEINVESTIGADOR')
                elif isinstance(aux.getDato(), Docente):
                    print('TIPO DE OBJETO ES DOCENTE')
                elif isinstance(aux.getDato(), Investigador):
                    print('TIPO DE OBJETO ES INVESTIGADOR')
                elif isinstance(aux.getDato(), PersonalApoyo):
                    print('TIPO DE OBJETO ES PERSONALAPOYO')
            else:
                print('LISTA VACIA')
        else:
            print('NO EXISTE LA POSICION {} EN LA LISTA ENLAZADA:'.format(posicion))
        self.__indice=0
    
    def ordenarNombre(self):
        k=None
        cota=None
        p=self.__comienzo
        aux=None
        while (k != self.__comienzo):
            k=self.__comienzo                 #VERIFICA QUE LA K NO SEA EL COMIENZO DE LA LISTA
            p=self.__comienzo
            while (p.getSiguiente() != cota): #VERIFICA QUE EL SIGUIENTE NO SEA NONE
                if (p.getDato().getNombre().upper() > p.getSiguiente().getDato().getNombre().upper()):
                    aux = p.getSiguiente().getDato();       #GUARDA EL DATO DEL MENOR EN AUX
                    p.getSiguiente().setDato(p.getDato())   #COLOCA EL DATO DEL MAYOR DONDE ESTABA EL MENOR
                    p.setDato(aux)                          #COLOCA EL DATO DEL MENOR DONDE ESTABA EL MAYOR
                    k = p                                   #GUARDA EL ULTIMO INTERCAMBIO
                p = p.getSiguiente()
            cota = k.getSiguiente()                         #LIMITA LA LISTA PARA NO COMPARAR HASTA EL FINAL
            
    def ordenarApellido(self):
        k=None
        cota=None
        p=self.__comienzo
        aux=None
        while (k != self.__comienzo):
            k=self.__comienzo
            ka=self.__comienzo.getDato().getCuil()
            p=self.__comienzo
            while (p.getSiguiente() != cota):
                if (p.getDato().getApellido().upper() > p.getSiguiente().getDato().getApellido().upper()):
                    aux = p.getSiguiente().getDato();
                    p.getSiguiente().setDato(p.getDato())
                    p.setDato(aux)
                    k = p
                p = p.getSiguiente()
            cota = k.getSiguiente()

    def listadoCarrera(self,carrera):
        self.ordenarNombre()
        print('-----------------------------------------------------')
        aux=self.__comienzo
        encontrado = False
        if aux==None:
            print('LISTA VACIA')
        else:
            while aux!=None:
                if isinstance(aux.getDato(), DocenteInvestigador) and aux.getDato().getCarrera().upper()==carrera.upper():
                    aux.getDato().mostrarDatos()
                    print('-----------------------------------------------------')
                aux=aux.getSiguiente()
        
    def contador(self,area):
        di=0
        i=0
        print('---------------------------------------------------------------')
        for agente in self:
            if isinstance(agente, DocenteInvestigador) and isinstance(agente, Investigador):
                if agente.getArea().upper()==area.upper():
                    di+=1
            elif isinstance(agente, Investigador):
                if agente.getArea().upper()==area.upper():
                    i+=1
        print('CANTIDAD DE DOCENTES INVESTIGADORES DEL AREA {} ES: {}'.format(area.upper(),di))
        print('CANTIDAD DE INVESTIGADORES DEL AREA {} ES: {}'.format(area.upper(),i))
        print('---------------------------------------------------------------')
        
    def listadoSueldos(self):
        self.ordenarApellido()
        print('---------------------------------')
        ag=''
        for agente in self:
            if isinstance(agente, DocenteInvestigador): #BUSCA QUE TIPO DE AGENTE ES Y GUARDA EL TIPO EN UNA VARIABLE AG
                ag='Docente Investigador'
            elif isinstance(agente, Docente):
                ag='Docente'
            elif isinstance(agente, Investigador):
                ag='Investigador'
            elif isinstance(agente, PersonalApoyo):
                ag='Personal De Apoyo'
            print('NOMBRE:{}\nAPELLIDO:{}\nAGENTE:{}\nSUELDO:{}'
                  .format(agente.getNombre(),agente.getApellido(),ag,agente.getObtSueldo()))
            print('---------------------------------')
    
    def listarCategoria(self,categoria):
        print('---------------------------------')
        for agente in self:
            if isinstance(agente, DocenteInvestigador) and agente.getCategProg().upper()==categoria.upper():
                print('NOMBRE:{}\nAPELLIDO:{}\nIMP. EXTRA:{}'
                  .format(agente.getNombre(),agente.getApellido(),agente.getImpExtra()))
                print('---------------------------------')
   
    def toJSON(self):
        d = dict(
            __class__=self.__class__.__name__,
            agentes=[agente.toJSON() for agente in self]
                )
        return d
    
    def buscarPosicion(self,posicion): #RETORNA EL AGENTE DE CIERTA POSICION (UTILIZADO EN TESTING)
        aux=self.__comienzo
        if posicion>=0 and (self.__tope==posicion==0 or posicion<self.__tope):
            if aux!=None:
                while self.__indice!=posicion:
                    aux=aux.getSiguiente()
                    self.__indice+=1
            else:
                print('LISTA VACIA')
        else:
            print('NO EXISTE LA POSICION {} EN LA LISTA ENLAZADA:'.format(posicion))
        self.__indice=0
        if aux!=None:
            return aux.getDato()