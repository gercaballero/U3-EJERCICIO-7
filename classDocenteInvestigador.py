from classDocente import Docente
from classInvestigador import Investigador
import os
class DocenteInvestigador(Docente, Investigador):
    __categoriaProg=''
    __importeExtra=0
    
    def __init__(self,cuil, apellido, nombre, sueldoB, antiguedad, carrera, cargo, catedra,area, tipo,categProg,importe,categoria='CATEGORIA'):
        super().__init__(cuil, apellido, nombre, sueldoB, antiguedad, carrera, cargo, catedra, area, tipo, categoria)
        self.__categoriaProg=categProg
        self.__importeExtra=importe
        
    def mostrarDatos(self):
        super().mostrarDatos()
        print('Categoria Programa:{}\nImporte Extra:{}'.format(self.__categoriaProg,self.__importeExtra))
    
    def getObtSueldo(self):
        return float(Docente.getObtSueldo(self)+self.__importeExtra)
    
    def getCategProg(self):
        return self.__categoriaProg
    
    def getImpExtra(self):
        return float(self.__importeExtra)
    
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
                               catedra=self.getCatedra(),
                               area=self.getArea(),
                               tipo=self.getTipo(),
                               categProg=self.__categoriaProg,
                               importe=self.__importeExtra  
                ))
        return d
    
    