from classPersonal import Personal
import os
class Docente(Personal):
    __carrera=''
    __cargo=''
    __catedra=''
    
    def __init__(self, cuil, apellido, nombre, sueldoB, antiguedad, carrera, cargo, catedra,area='', tipo='', categoria=0):
        super().__init__(cuil, apellido, nombre, sueldoB, antiguedad, cargo,catedra,area,tipo,categoria,carrera)
        self.__carrera=carrera
        self.__cargo=cargo
        self.__catedra=catedra
        
    def __str__(self):
        return('{}\nCARRERA:{}\tCARGO:{}\tCATEDRA'.format(super().__str__(),self.__carrera ,self.__cargo,self.__catedra))
    
    def mostrarDatos(self):
        super().mostrarDatos()
        print('Carrera:{}\nCargo:{}\nCatedra:{}\n'.format(self.__carrera,self.__cargo,self.__catedra))
    
    def getCarrera(self):
        return self.__carrera
    
    def getCargo(self):
        return self.__cargo
    
    def getCatedra(self):
        return self.__catedra
    
    def getObtSueldo(self):
        retorna=0.0
        if self.__cargo.upper()=='SIMPLE':
            retorna= self.getSueldoB()*0.1
        elif self.__cargo.upper()=='SEMIEXCLUSIVO':
            retorna= self.getSueldoB()*0.2
        elif self.__cargo.upper()=='EXCLUSIVO':
            retorna= self.getSueldoB()*0.3
        return float(super().getObtSueldo()+retorna)
    
    def toJSON(self):   
        d = dict(
            __class__=self.__class__.__name__,
            __atributos__=dict(cuil=self.getCuil(),
                               apellido=self.getApellido(),
                               nombre=self.getNombre(),
                               sueldoB=self.getSueldoB(),
                               antiguedad=int(self.getAntiguedad()),
                               carrera=self.getCarrera(),
                               cargo=self.getCargo(),
                               catedra=self.getCatedra()
                ))
        return d