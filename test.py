import unittest
from classDocenteInvestigador import DocenteInvestigador
from classDocente import Docente
from classInvestigador import Investigador
from classPApoyo import PersonalApoyo
from classColeccion import Lista
from classPersonal import Personal
class testLista(unittest.TestCase):
    def setUp(self):
        self.lista=Lista()
        agente0=PersonalApoyo('1', 'Perez', 'Juan', 20000, 6,'','','','','',5)
        agente1=PersonalApoyo('1', 'Adaro', 'Diego', 30000, 3,'','','','','',15)
        agente2=PersonalApoyo('1', 'Caballero', 'German', 15000, 2,'','','','','',21)
        self.lista.agregarElemento(agente0)
        self.lista.agregarElemento(agente1)
        self.lista.agregarElemento(agente2)
        agente4=Docente('1', 'Messi', 'Lionel', 50000, 5, 'LCC', 'Profesor', 'POO')
        self.lista.insertarElemento(agente4, 0)
    def test_insertar(self):
        '''TEST METODO INSERTAR EN POSICION'''                 
        self.assertEqual(self.lista.buscarPosicion(0).getApellido(),'Messi')
    def test_agregar(self):
        '''TEST METODO AGREGAR AL FINAL DE LA LISTA'''
        self.assertEqual(self.lista.buscarPosicion(1).getNombre(),'Juan')
    def test_ordenarApellido(self):
        '''TEST METODO ORDENAR LA LISTA POR APELLIDOS'''
        self.lista.ordenarApellido()
        self.assertEqual(self.lista.buscarPosicion(1).getApellido(),'Caballero')
    def test_ordenarNombre(self):
        '''TEST METODO ORDENAR LISTA POR NOMBRES'''
        self.lista.ordenarNombre()
        self.assertEqual(self.lista.buscarPosicion(2).getNombre(),'Juan')
    def test_sueldo(self):
        '''TEST METODO OBTENER SUELDO'''
        self.assertEqual(self.lista.buscarPosicion(1).getObtSueldo(),23200)