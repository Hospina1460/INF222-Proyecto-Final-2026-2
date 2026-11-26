class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

class ListaEnlazada:
    def __init__(self):
        self.cabeza = None
        self._tamanio = 0

    def insertar_inicio(self, dato):
        nuevo = Nodo(dato)
        nuevo.siguiente = self.cabeza
        self.cabeza = nuevo
        self._tamanio += 1

    def insertar_final(self, dato):
        nuevo = Nodo(dato)
        if self.cabeza is None:
            self.cabeza = nuevo
        else:
            actual = self.cabeza
            while actual.siguiente is not None:
                actual = actual.siguiente
            actual.siguiente = nuevo
        self._tamanio += 1

    # ESTE ES TU MÉTODO ELIMINAR (Está perfecto, no se tocó)
    def eliminar(self, dato):
        """Elimina la primera ocurrencia del dato."""
        actual = self.cabeza
        anterior = None
        
        while actual is not None:
            if actual.dato == dato:
                if anterior is None:
                    # Era la cabeza
                    self.cabeza = actual.siguiente
                else:
                    anterior.siguiente = actual.siguiente
                self._tamanio -= 1
                return True  # Eliminado con éxito
            anterior = actual
            actual = actual.siguiente
        return False  # No se encontró

    def buscar(self, dato):
        actual = self.cabeza
        while actual is not None:
            if actual.dato == dato:
                return True
            actual = actual.siguiente
        return False

    def mostrar_todas(self):
        tareas = []
        actual = self.cabeza
        while actual is not None:
            tareas.append(actual.dato)
            actual = actual.siguiente
        return tareas

    # NUEVO MÉTODO: Para buscar por posición (número) en el main
    def obtener_por_indice(self, indice):
        """Retorna el dato en la posición dada (0 = primera tarea)."""
        if indice < 0 or indice >= self._tamanio:
            return None
        
        actual = self.cabeza
        contador = 0
        while actual is not None:
            if contador == indice:
                return actual.dato
            actual = actual.siguiente
            contador += 1
        return None

    def tamanio(self):
        return self._tamanio