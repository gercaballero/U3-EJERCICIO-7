import os
class Personal:
    __cuil=''
    __apellido=''
    __nombre=''
    __sueldoB=0
    __antiguedad=0
    
    def __init__(self,cuil, apellido, nombre, sueldoB, antiguedad, catedra, area, tipo, categoria,carrera, cargo):
        self.__cuil=cuil
        self.__apellido=apellido
        self.__nombre=nombre
        self.__sueldoB=sueldoB
        self.__antiguedad=antiguedad
    
    def __str__(self):
        return('CUIL:{}\tAPELLIDO:{}\tNOMBRE:{}\tSUELDOB:{}\tANTIGUEDAD:{}'.
              format(self.__cuil,self.__apellido,self.__nombre,self.__sueldoB,self.__antiguedad))
    
    def mostrarDatos(self):
        print('CUIL:{}\nAPELLIDO:{}\nNOMBRE:{}\nSUELDOB:{}\nANTIGUEDAD:{}'.
              format(self.__cuil,self.__apellido,self.__nombre,self.__sueldoB,self.__antiguedad))
    
    def getObtSueldo(self):     #OBTENER SUELDO GENERAL POR ANTIGUEDAD
        return float(float(self.__sueldoB) + float(self.__sueldoB)* (float(self.__antiguedad)*0.01))
    
    def getCuil(self):
        return self.__cuil
    
    def getApellido(self):
        return self.__apellido
    
    def getNombre(self):
        return self.__nombre
    
    def getSueldoB(self):
        return int(self.__sueldoB)
    
    def getAntiguedad(self):
        return int(self.__antiguedad)