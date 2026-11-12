# Checkpoint 1 del Proyecto Final
INF 222 Estructura de Datos · Semestre 2026-2
Entrega: Semana 10

## Estado del proyecto

| Campo | Información |
|-------|-------------|
| Equipo | Team TaskFlow |
| Tema | TaskFlow — Gestor de Tareas con Deshacer/Rehacer |
| Commit de entrega | [actualizar checkpoint 1 con los roles del equipo definitivo] |

---

## Estructura de datos implementada

**Estructura 1:** Lista Enlazada Simple
**Archivo:** `src/estructuras/lista_enlazada.py`

**Métodos implementados y estado:**

| Método | Estado | Notas |
|--------|--------|-------|
| `insertar_inicio()` |  Completo | Inserta una nueva tarea en O(1) |
| `insertar_final()` |  Completo | Agrega tareas al final en O(n) |
| `eliminar()` |  Completo | Maneja casos borde (cabeza, medio, no existe) |
| `buscar()` |  Completo | Búsqueda secuencial en O(n) |

**Complejidad de las operaciones principales:**

| Operación | Complejidad | Justificación |
|-----------|-------------|---------------|
| `insertar_inicio` | O(1) | Solo se reasigna el puntero de la cabeza. |
| `buscar` | O(n) | En el peor caso, recorre todos los nodos de la lista. |

**¿Cómo está integrada en el sistema?**
La Lista Enlazada es el núcleo del sistema. El flujo de uso planeado es el siguiente:
1. Cuando el usuario selecciona "Registrar tarea" en el menú, el sistema crea un objeto Tarea y lo inserta usando `insertar_final()`.
2. Si el usuario pide ver sus tareas, el sistema usa `buscar()` o el recorrido interno para mostrarlas en pantalla.
3. Cuando el usuario marca una tarea como completada, el sistema usa `eliminar()` para sacarla del registro de pendientes.

---

## ¿Qué falta para el Checkpoint 2?

- [ ] Terminar la integración de la Pila en el `main.py` (Maria y Adriana).
- [ ] Crear la interfaz de menú por consola completa (Edward).
- [ ] Implementar el Árbol BST para categorías (Julieth).
- [ ] Escribir los casos de prueba en `src/tests/test_estructuras.py` que validen las operaciones de la lista y la pila.

---

## Problemas encontrados y cómo los resolvieron

**Problema:** Al inicio, al implementar la función `eliminar()`, el programa lanzaba un error si intentábamos borrar la primera tarea de la lista, ya que perdíamos la referencia al resto de los nodos y la lista "desaparecía".
**Solución:** Agregamos una validación para el caso borde de la cabeza. Si el dato a eliminar estaba en `self._cabeza`, simplemente reasignamos la cabeza al siguiente nodo (`self._cabeza = self._cabeza.siguiente`). Esto desconecta el primer nodo sin romper la cadena.

---

## Decisiones de diseño tomadas hasta ahora

Decidimos implementar nuestras propias estructuras de datos (Nodo y ListaEnlazada) en lugar de usar las listas nativas de Python (`[]`). Aunque las listas de Python son más fáciles, implementar la Lista Enlazada nos permite cumplir con el objetivo de la materia y, a nivel de sistema, nos prepara para el manejo del historial de Undo/Redo con la Pila de forma más eficiente en cuanto a memoria.

---

## Declaración de uso de IA

| Campo | Detalle |
|-------|---------|
| ¿Usaron IA? | Sí |
| Herramienta(s) | DeepSeek |
| Para qué se usó | Apoyo para estructurar el código de la lista enlazada y revisar la lógica del manejo de casos borde (eliminación de la cabeza). |
| Qué hizo el equipo por su cuenta | Definimos la arquitectura del sistema, creamos los repositorios y redactamos la propuesta. Edward implementó la lógica base de la lista, Maria y Adriana revisaron la integración, y Julieth estructuró el plan del BST. |
| El equipo puede explicar todo el código | Sí |
