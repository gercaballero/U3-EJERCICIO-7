from classDocenteInvestigador import DocenteInvestigador
from classDocente import Docente
from classInvestigador import Investigador
from classPApoyo import PersonalApoyo
from classColeccion import Lista
from classPersonal import Personal
from classMenu import Menu
import os
from classObjectEncoder import ObjectEncoder
import unittest
from test import testLista

if __name__=='__main__':
    os.system('cls')
    o=input('\n----->> ¿DESEA REALIZAR TEST?(SI/NO): ')
    if o.upper() =='SI':
        unittest.main()                 #TEST CON UNITTESTING
    
    '''ARCHIVO CARGADO'''
    jsonF=ObjectEncoder()
    diccionario=jsonF.leerJSONArchivo('personal.json')  #LEO Y CARGO EL ARCHIVO JSON A LA LISTA
    vehiculos=jsonF.decodificarDiccionario(diccionario)
    lista=Lista()                                       #CREO UNA LISTA VACIA 
    lista=vehiculos                                     #ASIGNO LA LISTA DEL OBJECT ENCODER A LA LISTA NUEVA
    menu= Menu()
    salir= False
    os.system('cls')
    while not salir:
            os.system('cls')
            print("""-------------------Menu-------------------
1- INSERTAR AGENTE
2- AGREGAR AGENTE
3- TIPO POR POSICION
4- DOCENTE INVESTIGADORES SEGUN CARRERA
5- CONTADOR DOCENTE INVESTIGADOR E INVESGADORES
6- LISTAR POR APELLIDO
7- CATEG INVESTIGACION
8- GUARDAR EN ARCHIVO
9- SALIR""")
            op= input('\n INGRESE UNA OPCION: ')
            if op in ('1','2','3','4','5','6','7','8','9'):
                menu.opcion(int(op),lista)
                if op=='9':
                    salir=True
            else:
                os.system('cls')
                print ("---OPCION NO VALIDA---")
            os.system('cls')
