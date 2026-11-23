class NodoBST:
    def __init__(self, categoria):
        self.categoria = categoria
        self.tareas = []  # Lista de tareas dentro de esta categoría
        self.izquierdo = None
        self.derecho = None

class ArbolCategorias:
    def __init__(self):
        self.raiz = None

    def insertar(self, categoria, tarea):
        """Inserta una tarea en la categoría correspondiente (o crea la categoría)."""
        if self.raiz is None:
            self.raiz = NodoBST(categoria)
            self.raiz.tareas.append(tarea)
            return
        
        actual = self.raiz
        while True:
            if categoria == actual.categoria:
                actual.tareas.append(tarea)
                break
            elif categoria < actual.categoria:
                if actual.izquierdo is None:
                    actual.izquierdo = NodoBST(categoria)
                    actual.izquierdo.tareas.append(tarea)
                    break
                actual = actual.izquierdo
            else:
                if actual.derecho is None:
                    actual.derecho = NodoBST(categoria)
                    actual.derecho.tareas.append(tarea)
                    break
                actual = actual.derecho

    def eliminar_tarea(self, categoria, tarea):
        """Elimina una tarea específica de una categoría."""
        nodo = self.buscar_categoria(categoria)
        if nodo and tarea in nodo.tareas:
            nodo.tareas.remove(tarea)
            return True
        return False

    def buscar_categoria(self, categoria):
        """Busca el nodo de una categoría específica."""
        actual = self.raiz
        while actual is not None:
            if categoria == actual.categoria:
                return actual
            elif categoria < actual.categoria:
                actual = actual.izquierdo
            else:
                actual = actual.derecho
        return None

    def mostrar_en_orden(self):
        """Recorre el árbol inorden (izquierda -> raíz -> derecha) para mostrar todo ordenado alfabéticamente."""
        resultado = []
        self._inorden(self.raiz, resultado)
        return resultado

    def _inorden(self, nodo, resultado):
        if nodo is not None:
            self._inorden(nodo.izquierdo, resultado)
            resultado.append((nodo.categoria, nodo.tareas))
            self._inorden(nodo.derecho, resultado)