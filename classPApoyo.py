from classPersonal import Personal

class PersonalApoyo(Personal):
    __categoria=0
    
    def __init__(self, cuil, apellido, nombre, sueldoB, antiguedad, carrera="", cargo="", catedra="",area="", tipo="", categoria=0):
        super().__init__(cuil, apellido, nombre, sueldoB, antiguedad, cargo,catedra,area,tipo,categoria,carrera)
        self.__categoria=int(categoria)
    
    def mostrarDatos(self):
        super().mostrarDatos()
        print('Categoria:{}'.format(self.__categoria))
    
    def getCategoria(self):
        return int(self.__categoria)
    
    def getObtSueldo(self):
        retorna=0.0
        if self.__categoria>=1 and self.__categoria<=10:
            retorna= self.getSueldoB()*0.1
        elif self.__categoria>=11 and self.__categoria<=20:
            retorna= self.getSueldoB()*0.2
        elif self.__categoria>=21 and self.__categoria<=22:
            retorna= self.getSueldoB()*0.3
        return float(super().getObtSueldo()+ retorna)
   
    def toJSON(self):
        d = dict(
            __class__=self.__class__.__name__,
            __atributos__=dict(cuil=self.getCuil(),
                               apellido=self.getApellido(),
                               nombre=self.getNombre(),
                               sueldoB=self.getSueldoB(),
                               antiguedad=int(self.getAntiguedad()),
                               carrera="",
                               cargo="",
                               catedra="",
                               area="",
                               tipo="",
                               categoria=int(self.__categoria)
                ))
        return d