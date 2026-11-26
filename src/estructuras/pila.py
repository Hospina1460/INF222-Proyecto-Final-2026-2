class Pila:
    def __init__(self):
        self._items = []

    def push(self, dato):
        self._items.append(dato)

    def pop(self):
        if self.is_empty():
            return None
        return self._items.pop()

    def peek(self):
        if self.is_empty():
            return None
        return self._items[-1]

    def is_empty(self):
        return len(self._items) == 0

    def tamanio(self):
        return len(self._items)