from classDocente import Docente
from classInvestigador import Investigador
from classDocenteInvestigador import DocenteInvestigador
from classPApoyo import PersonalApoyo
from classObjectEncoder import ObjectEncoder
import time
import copy
import os
import gc

class Menu:
    __switcher=None
    def __init__(self):
        self.__switcher = { 1:self.opcion1,
                            2:self.opcion2,
                            3:self.opcion3,
                            4:self.opcion4,
                            5:self.opcion5,
                            6:self.opcion6,
                            7:self.opcion7,
                            8:self.opcion8,
                            9:self.salir
                         }
    def getSwitcher(self):
        return self.__switcher
    def opcion(self,op,li):
        gc.collect()
        func= self.__switcher.get(op, lambda: print("Opción no válida"))
        func(li)

    def salir(self,li):
        jsonF=ObjectEncoder()
        d=li.toJSON()
        jsonF.guardarJSONArchivo(d,'personal.json')
        print('Salida del programa')

    def opcion1(self,li):
        os.system('cls')
        band=False
        print('~~~~~INSERTAR AGENTE~~~~~')
        agente=input('AGENTE QUE DESEA AGREGAR(DOCENTE/INVESTIGADOR/PERSONAL DE APOYO/DOCENTE INVESTIGADOR):')
        while not band:
            if agente.upper()=='DOCENTE':
                os.system('cls')
                print('~~~~~INSERTAR DOCENTE~~~~~')
                cuil=input('CUIL: ')
                apellido=input('APELLIDO: ')
                nombre=input('NOMBRE: ')
                sueldoB=input('SUELDO BASICO: ')
                antiguedad=int(input('ANTIGUEDAD(AÑOS): '))
                carrera=input('CARRERA DONDE DICTA CLASES: ')
                cargo=input('CARGO:')
                catedra=input('CATEDRA:')
                unAgente=Docente(cuil, apellido, nombre, sueldoB, antiguedad, carrera, cargo, catedra)
                band=True
            elif agente.upper()=='INVESTIGADOR':
                os.system('cls')
                print('~~~~~INSERTAR INVESTIGADOR~~~~~')
                cuil=input('CUIL: ')
                apellido=input('APELLIDO: ')
                nombre=input('NOMBRE: ')
                sueldoB=input('SUELDO BASICO: ')
                antiguedad=int(input('ANTIGUEDAD(AÑOS): '))
                area=input('AREA DE INVESTIGACION: ')
                tipo=input('TIPO DE INVESTIGACION: ')
                unAgente=Investigador(cuil, apellido, nombre, sueldoB, antiguedad,'','', area, tipo)
                band=True
            elif agente.upper()=='PERSONAL DE APOYO':
                os.system('cls')
                print('~~~~~INSERTAR PERSONAL DE APOYO~~~~~')
                cuil=input('CUIL: ')
                apellido=input('APELLIDO: ')
                nombre=input('NOMBRE: ')
                sueldoB=input('SUELDO BASICO: ')
                antiguedad=int(input('ANTIGUEDAD(AÑOS): '))
                categoria=int(input('CATEGORIA: '))
                unAgente=PersonalApoyo(cuil, apellido, nombre, sueldoB, antiguedad,'','','','','', categoria)
                band=True
            elif agente.upper()=='DOCENTE INVESTIGADOR':
                os.system('cls')
                print('~~~~~INSERTAR DOCENTE INVESTIGADOR~~~~~')
                cuil=input('CUIL: ')
                apellido=input('APELLIDO: ')
                nombre=input('NOMBRE: ')
                sueldoB=input('SUELDO BASICO: ')
                antiguedad=int(input('ANTIGUEDAD(AÑOS): '))
                categProg=input('CATEGORIA EN EL PROGRAMA: ')
                importe=int(input('IMPORTE EXTRA: '))
                unAgente=DocenteInvestigador(cuil, apellido, nombre, sueldoB, antiguedad, carrera, cargo, catedra, area, tipo, categProg, importe)
            else:
                os.system('cls')
                print('~~~~~INSERTAR AGENTE~~~~~')
                print('AGENTE INCORRECTO-REINTENTE')
                agente=input('AGENTE QUE DESEA AGREGAR(DOCENTE/INVESTIGADOR/PERSONAL DE APOYO/DOCENTE INVESTIGADOR):')
        os.system('cls')
        posicion=int(input('\nPOSICION QUE DESEA AGREGAR:'))
        li.insertarElemento(unAgente,posicion)
        print('~~<AGENTE AÑADIDO EN LA POSICION {} DE LA LISTA>~~'.format(posicion))
        input()
        os.system('cls')
    
    def opcion2(self,li):
        os.system('cls')
        band=False
        print('~~~~~INSERTAR AGENTE~~~~~')
        agente=input('AGENTE QUE DESEA AGREGAR(DOCENTE/INVESTIGADOR/PERSONAL DE APOYO/DOCENTE INVESTIGADOR):')
        while not band:
            if agente.upper()=='DOCENTE':
                os.system('cls')
                print('~~~~~INSERTAR DOCENTE~~~~~')
                cuil=input('CUIL: ')
                apellido=input('APELLIDO: ')
                nombre=input('NOMBRE: ')
                sueldoB=input('SUELDO BASICO: ')
                antiguedad=int(input('ANTIGUEDAD(AÑOS): '))
                carrera=input('CARRERA DONDE DICTA CLASES: ')
                cargo=input('CARGO:')
                catedra=input('CATEDRA:')
                unAgente=Docente(cuil, apellido, nombre, sueldoB, antiguedad, carrera, cargo, catedra)
                band=True
            elif agente.upper()=='INVESTIGADOR':
                os.system('cls')
                print('~~~~~INSERTAR INVESTIGADOR~~~~~')
                cuil=input('CUIL: ')
                apellido=input('APELLIDO: ')
                nombre=input('NOMBRE: ')
                sueldoB=input('SUELDO BASICO: ')
                antiguedad=int(input('ANTIGUEDAD(AÑOS): '))
                area=input('AREA DE INVESTIGACION: ')
                tipo=input('TIPO DE INVESTIGACION: ')
                unAgente=Investigador(cuil, apellido, nombre, sueldoB, antiguedad,'','', area, tipo)
                band=True
            elif agente.upper()=='PERSONAL DE APOYO':
                os.system('cls')
                print('~~~~~INSERTAR PERSONAL DE APOYO~~~~~')
                cuil=input('CUIL: ')
                apellido=input('APELLIDO: ')
                nombre=input('NOMBRE: ')
                sueldoB=input('SUELDO BASICO: ')
                antiguedad=int(input('ANTIGUEDAD(AÑOS): '))
                categoria=int(input('CATEGORIA: '))
                unAgente=PersonalApoyo(cuil, apellido, nombre, sueldoB, antiguedad,'','','','','', categoria)
                band=True
            elif agente.upper()=='DOCENTE INVESTIGADOR':
                os.system('cls')
                print('~~~~~INSERTAR DOCENTE INVESTIGADOR~~~~~')
                cuil=input('CUIL: ')
                apellido=input('APELLIDO: ')
                nombre=input('NOMBRE: ')
                sueldoB=input('SUELDO BASICO: ')
                antiguedad=int(input('ANTIGUEDAD(AÑOS): '))
                carrera=input('CARRERA DONDE DICTA CLASES: ')
                cargo=input('CARGO:')
                catedra=input('CATEDRA:')
                categProg=input('CATEGORIA EN EL PROGRAMA: ')
                area=input('AREA DE INVESTIGACION: ')
                tipo=input('TIPO DE INVESTIGACION: ')
                importe=int(input('IMPORTE EXTRA: '))
                unAgente=DocenteInvestigador(cuil, apellido, nombre, sueldoB, antiguedad, carrera, cargo, catedra, area, tipo, categProg, importe)
                band=True
            else:
                os.system('cls')
                print('~~~~~INSERTAR AGENTE~~~~~')
                print('AGENTE INCORRECTO-REINTENTE')
                agente=input('AGENTE QUE DESEA AGREGAR(DOCENTE/INVESTIGADOR/PERSONAL DE APOYO/DOCENTE INVESTIGADOR):')
        li.agregarElemento(unAgente)
        print('~~<AGENTE AÑADIDO EN LA POSICION FINAL DE LA LISTA>~~')
        input()
        os.system('cls')
        
    def opcion3(self,li):
        os.system('cls')
        print('~~~~~TIPO DE OBJETO EN POSICION~~~~~')
        pos=int(input('INGRESE POSICION:'))
        li.tipoPosicion(pos)
        input()
        os.system('cls')
        
    def opcion4(self,li):
        os.system('cls')
        carrera=input('INGRESE CARRERA: ')
        os.system('cls')
        print('-----------------DOCENTES INVESTIGADORES DE {}-----------------'.format(carrera.upper()))
        li2=copy.deepcopy(li)
        li2.listadoCarrera(carrera)
        del li2
        input()
        os.system('cls')
    
    def opcion5(self,li):
        os.system('cls')
        print('-----------CANT. DOC. INVESTIGADORES E INVESTIGADORES-----------')
        area=input('INGRESE AREA DE INVESTIGACION: ')
        li.contador(area)
        input()
        os.system('cls')
        
    def opcion6(self,li):
        os.system('cls')
        li2=copy.deepcopy(li)
        print('~~~~~~~~~----LISTADO SUELDOS----~~~~~~~~~')
        li2.listadoSueldos()
        del li2
        input()
        os.system('cls')
    
    def opcion7(self,li):
        os.system('cls')
        print('~~~~~~~~~LISTADO CATEGORIA~~~~~~~~~')
        cat=input('INGRESE CATEGORIA(I, II, III, IV o V): ')
        os.system('cls')
        print('~~~~~~~~~LISTADO CATEGORIA {}~~~~~~~~~'.format(cat))
        li.listarCategoria(cat)
        input()
        os.system('cls')
    
    def opcion8(self,li):
        jsonF=ObjectEncoder()
        os.system('cls')
        print('~~~~~CREAR ARCHIVO JSON~~~')
        print('     <Creando archivo>')
        time.sleep(1)
        os.system('cls')
        print('~~~~~CREAR ARCHIVO JSON~~~')
        print('    <<Creando archivo>>')
        time.sleep(1)
        os.system('cls')
        print('~~~~~CREAR ARCHIVO JSON~~~')
        print('   <<<Creando archivo>>>')
        time.sleep(1)
        os.system('cls')
        print('~~~~~CREAR ARCHIVO JSON~~~')
        print('  <<<<Creando archivo>>>>')
        time.sleep(1)
        d=li.toJSON()
        jsonF.guardarJSONArchivo(d,'personal.json')
        os.system('cls')
        print('     ~~~~~ARCHIVO CREADO~~~~')
        input()
        os.system('cls')