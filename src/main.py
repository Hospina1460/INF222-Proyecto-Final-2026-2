import sys
import os

# Esto permite importar desde la carpeta src/estructuras
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from estructuras.lista_enlazada import ListaEnlazada
from estructuras.pila import Pila
from estructuras.arbol_bst import ArbolCategorias

class TaskFlow:
    def __init__(self):
        self.tareas = ListaEnlazada()
        self.historial_undo = Pila()
        self.historial_redo = Pila()
        self.arbol = ArbolCategorias() # <-- NUEVO: El Árbol BST

    def agregar_tarea(self, titulo, categoria):
        self.tareas.insertar_final(titulo)
        self.arbol.insertar(categoria, titulo) # <-- NUEVO: Se guarda en el árbol
        self.historial_undo.push(("ADD", titulo, categoria)) # Guardamos también la categoría
        self.historial_redo = Pila()
        print(f"✅ Tarea '{titulo}' agregada en la categoría '{categoria}'.")

    def eliminar_tarea(self, titulo, categoria):
        if self.tareas.eliminar(titulo):
            self.arbol.eliminar_tarea(categoria, titulo) # <-- NUEVO: Se elimina del árbol
            self.historial_undo.push(("DEL", titulo, categoria))
            self.historial_redo = Pila()
            print(f"🗑️ Tarea '{titulo}' eliminada.")
        else:
            print(f"❌ No se encontró la tarea '{titulo}'.")

    def deshacer(self):
        accion = self.historial_undo.pop()
        if accion is None:
            print("⚠️ No hay acciones para deshacer.")
            return

        tipo, titulo, categoria = accion
        if tipo == "ADD":
            self.tareas.eliminar(titulo)
            self.arbol.eliminar_tarea(categoria, titulo)
            self.historial_redo.push(("ADD", titulo, categoria))
            print(f"↩️ Deshecho: Se quitó '{titulo}'.")
        elif tipo == "DEL":
            self.tareas.insertar_final(titulo)
            self.arbol.insertar(categoria, titulo)
            self.historial_redo.push(("DEL", titulo, categoria))
            print(f"↩️ Deshecho: Se recuperó '{titulo}'.")

    def rehacer(self):
        accion = self.historial_redo.pop()
        if accion is None:
            print("⚠️ No hay acciones para rehacer.")
            return

        tipo, titulo, categoria = accion
        if tipo == "ADD":
            self.tareas.insertar_final(titulo)
            self.arbol.insertar(categoria, titulo)
            self.historial_undo.push(("ADD", titulo, categoria))
            print(f"↪️ Rehecho: Se volvió a agregar '{titulo}'.")
        elif tipo == "DEL":
            self.tareas.eliminar(titulo)
            self.arbol.eliminar_tarea(categoria, titulo)
            self.historial_undo.push(("DEL", titulo, categoria))
            print(f"↪️ Rehecho: Se volvió a eliminar '{titulo}'.")

    def mostrar_tareas(self):
        tareas = self.tareas.mostrar_todas()
        if not tareas:
            print("\n📭 No hay tareas pendientes.")
        else:
            print("\n📋 TAREAS PENDIENTES:")
            for i, t in enumerate(tareas, 1):
                print(f"  {i}. {t}")
        print(f"Total: {self.tareas.tamanio()} tareas.")

    def mostrar_por_categorias(self):
        """NUEVO: Muestra las tareas agrupadas usando el Árbol BST."""
        if self.arbol.raiz is None:
            print("\n📭 El árbol de categorías está vacío.")
            return
        
        print("\n🌳 TAREAS POR CATEGORÍA (Recorrido Inorden):")
        categorias = self.arbol.mostrar_en_orden()
        for cat, tareas in categorias:
            if tareas: # Solo mostrar si tiene tareas
                print(f"  📁 {cat}:")
                for t in tareas:
                    print(f"      - {t}")

def menu():
    app = TaskFlow()
    
    while True:
        print("\n" + "=" * 40)
        print("     TASKFLOW - Gestor de Tareas")
        print("=" * 40)
        print("1. Agregar tarea")
        print("2. Mostrar tareas (general)")
        print("3. Eliminar tarea")
        print("4. Deshacer (Undo)")
        print("5. Rehacer (Redo)")
        print("6. Ver tareas por Categoría (BST)")
        print("7. Salir")
        print("=" * 40)
        
        opcion = input("Elige una opción (1-7): ")
        
        if opcion == "1":
            titulo = input("Escribe el nombre de la tarea: ")
            categoria = input("Escribe la categoría (ej. Universidad, Personal, Trabajo): ")
            app.agregar_tarea(titulo, categoria)
        elif opcion == "2":
            app.mostrar_tareas()
            input("\nPresiona Enter para volver al menú...")
        elif opcion == "3":
            tareas = app.tareas.mostrar_todas()
            if not tareas:
                print("\n📭 No hay tareas para eliminar.")
            else:
                app.mostrar_tareas()
                try:
                    num = int(input("Escribe el NÚMERO de la tarea a eliminar: "))
                    posicion = num - 1 
                    
                    titulo = app.tareas.obtener_por_indice(posicion)
                    
                    if titulo is not None:
                        # Como ahora hay categorías, le pedimos que confirme en cuál estaba
                        categoria = input("Escribe la categoría de esa tarea (para borrarla del árbol): ")
                        app.eliminar_tarea(titulo, categoria)
                    else:
                        print("❌ Número fuera de rango.")
                except ValueError:
                    print("❌ Error: Debes escribir un número, no letras.")
            input("\nPresiona Enter para volver al menú...")
        elif opcion == "4":
            app.deshacer()
            input("\nPresiona Enter para volver al menú...")
        elif opcion == "5":
            app.rehacer()
            input("\nPresiona Enter para volver al menú...")
        elif opcion == "6":
            app.mostrar_por_categorias()
            input("\nPresiona Enter para volver al menú...")
        elif opcion == "7":
            print("¡Hasta luego! 👋")
            break
        else:
            print("❌ Opción inválida. Intenta de nuevo.")

if __name__ == "__main__":
    menu()