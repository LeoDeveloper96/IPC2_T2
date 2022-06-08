from estructuras.nodo import Nodo


class ListaCircularDE:

    def __init__(self):
        self.primero = None
        self.ultimo = None

    def append(self, dato):
        nuevo = Nodo(dato)
        if self.primero is None:
            self.primero = nuevo
            self.ultimo = nuevo
        else:
            nuevo = Nodo(dato)
            actual = self.primero
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nuevo
            self.ultimo = nuevo
            nuevo.anterior = actual
            nuevo.siguiente = None

    def getDato(self, dato):
        tmp = self.primero
        while True:
            if tmp.dato == dato:
                return tmp
            tmp = tmp.siguiente
            if tmp == self.primero:
                return None