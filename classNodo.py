from classPersonal import Personal

class Nodo:
     __agente=None
     __siguiente=None
     def __init__(self, agente=None):
        self.__agente=agente
        self.__siguiente=None
     def setSiguiente(self, siguiente):
        self.__siguiente=siguiente
     def getSiguiente(self):
        return self.__siguiente
     def getDato(self):
        return self.__agente
     def setDato(self,agente):
        self.__agente=agente