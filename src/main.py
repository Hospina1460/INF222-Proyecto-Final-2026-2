from estructuras.lista_enlazada import ListaEnlazada

def main():
    print("--- Prueba de integración TaskFlow ---")
    mis_tareas = ListaEnlazada()
    
    # Insertamos tareas de prueba
    mis_tareas.insertar_final("Hacer el Checkpoint 1")
    mis_tareas.insertar_final("Estudiar para el Parcial 2")
    mis_tareas.insertar_inicio("Comprar café")
    
    print(f"Tienes {mis_tareas.tamanio()} tareas pendientes:")
    print(mis_tareas.mostrar_todas())
    
    print("\nCompletando 'Comprar café'...")
    mis_tareas.eliminar("Comprar café")
    
    print("Tareas restantes:")
    print(mis_tareas.mostrar_todas())

if __name__ == "__main__":
    main()