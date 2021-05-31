from classPersonal import Personal
import os
class Investigador(Personal):
    __area=''
    __tipo=''
    
    def __init__(self,cuil, apellido, nombre, sueldoB, antiguedad, cargo, catedra,area,tipo,categoria=0,carrera=''):
        super().__init__(cuil, apellido, nombre, sueldoB, antiguedad, cargo,catedra,area,tipo,categoria,carrera)
        self.__area=area
        self.__tipo=tipo
    
    def __str__(self):
        return('{}\nAREA:{}\tTIPO:{}'.format(super().__str__(),self.__area,self.__tipo))
    
    def mostrarDatos(self):
        super().mostrarDatos()
        print('Area:{}\tTipo:{}\n'.format(self.__area,self.__tipo))
    
    def getArea(self):
        return self.__area
    
    def getTipo(self):
        return self.__tipo
    
    def getObtSueldo(self):
        return float(super().getObtSueldo())
    
    def toJSON(self):
        d = dict(
            __class__=self.__class__.__name__,
            __atributos__=dict(cuil=self.getCuil(),
                               apellido=self.getApellido(),
                               nombre=self.getNombre(),
                               sueldoB=self.getSueldoB(),
                               antiguedad=int(self.getAntiguedad()),
                               cargo='',
                               catedra='',
                               area=self.getArea(),
                               tipo=self.getTipo(),
                ))
        return d