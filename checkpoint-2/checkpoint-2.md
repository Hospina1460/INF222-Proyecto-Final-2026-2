# Checkpoint 2 — Proyecto Final INF 222
Estructura de Datos · Semestre 2026-2 · 20-25% del proyecto
Fecha límite: semana 13 (ver calendario en README.md)

## Datos del equipo
| Campo | Información |
| :--- | :--- |
| Nombre del equipo | Team TaskFlow |
| Integrantes | Edward Hospina, Julieth Huerta, Maria Gonzalez, Adriana Pineda |
| Repositorio GitHub | https://github.com/Hospina1460/INF222-Proyecto-Final-2026-2/tree/main |
| Tema elegido | TaskFlow — Gestor de Tareas con Deshacer/Rehacer |

## 1. Estado de implementación

**Estructuras de datos implementadas**
| Estructura | Módulo / archivo | Estado | Complejidad inserción | Complejidad búsqueda |
| :--- | :--- | :--- | :--- | :--- |
| Lista Enlazada Simple | `src/estructuras/lista_enlazada.py` | ✅ Completa | O(1) inicio / O(n) final | O(n) |
| Pila (Stack) | `src/estructuras/pila.py` | ✅ Completa | O(1) | O(n) |
| Árbol Binario de Búsqueda (BST) | `src/estructuras/arbol_bst.py` | ✅ Completa | O(log n) promedio | O(log n) promedio |

**Funcionalidades completadas**
- [x] Funcionalidad 1: Registrar nuevas tareas usando la Lista Enlazada.
- [x] Funcionalidad 2: Listar todas las tareas pendientes y marcarlas como completadas (eliminar de la lista).
- [x] Funcionalidad 3: Organizar y mostrar tareas por categorías usando el Árbol BST.
- [x] Funcionalidad 4: Implementar "Deshacer" (Undo) usando la Pila.
- [x] Funcionalidad 5: Implementar "Rehacer" (Redo) para revertir un "Deshacer".
- [x] Funcionalidad 6: Interfaz de usuario por consola (menú interactivo completo).

## 2. Análisis de complejidad actualizado

| Operación | Complejidad real | ¿Cambió respecto al CP1? | Motivo del cambio |
| :--- | :--- | :--- | :--- |
| Insertar tarea (Lista) | O(n) | No | Se inserta al final de la lista. |
| Eliminar tarea (Lista) | O(n) | No | Búsqueda secuencial para encontrar el nodo. |
| Push / Pop (Pila) | O(1) | No | Operaciones en el tope de la pila. |
| Insertar tarea en BST | O(log n) promedio | N/A (Nuevo) | El árbol divide el espacio a la mitad. |
| Buscar categoría (BST) | O(log n) promedio | N/A (Nuevo) | Se descarta la mitad del árbol en cada paso. |

## 3. Integración entre estructuras

El sistema TaskFlow integra las tres estructuras de la siguiente manera:

```text
       [ USUARIO ]
            │
            ▼
    [ MENÚ CONSOLA ] (main.py)
            │
   ┌────────┴─────────────────────────┐
   ▼                                  ▼
[ Agregar/Eliminar ]           [ Ver por Categorías ]
   │                                  │
   ▼                                  ▼
[ LISTA ENLAZADA ]               [ ÁRBOL BST ]
(Tareas en orden)               (Agrupa por categoría)
   │                                  │
   └──────────────┬───────────────────┘
                  ▼
             [ PILA (Stack) ]
          (Historial Undo/Redo)
```

## 4. Evidencia de código funcionando
Salida real de python src/main.py probando las funcionalidades principales:
```text
$ python src/main.py

========================================
     TASKFLOW - Gestor de Tareas
========================================
1. Agregar tarea
2. Mostrar tareas (general)
3. Eliminar tarea
4. Deshacer (Undo)
5. Rehacer (Redo)
6. Ver tareas por Categoría (BST)
7. Salir
========================================
Elige una opción (1-7): 1
Escribe el nombre de la tarea: Comprar café
Escribe la categoría (ej. Universidad, Personal, Trabajo): Personal
✅ Tarea 'Comprar café' agregada en la categoría 'Personal'.

Elige una opción (1-7): 1
Escribe el nombre de la tarea: Hacer el Checkpoint 2
Escribe la categoría (ej. Universidad, Personal, Trabajo): Universidad
✅ Tarea 'Hacer el Checkpoint 2' agregada en la categoría 'Universidad'.

Elige una opción (1-7): 1
Escribe el nombre de la tarea: Leer libro de datos
Escribe la categoría (ej. Universidad, Personal, Trabajo): Universidad
✅ Tarea 'Leer libro de datos' agregada en la categoría 'Universidad'.

Elige una opción (1-7): 6

🌳 TAREAS POR CATEGORÍA (Recorrido Inorden):
  📁 Personal:
      - Comprar café
  📁 Universidad:
      - Hacer el Checkpoint 2
      - Leer libro de datos

Elige una opción (1-7): 4
↩️ Deshecho: Se quitó 'Leer libro de datos'.

Elige una opción (1-7): 2

📋 TAREAS PENDIENTES:
  1. Comprar café
  2. Hacer el Checkpoint 2
Total: 2 tareas.
```
## 5. Pruebas unitarias

| Función probada | Casos de prueba | Resultado |
| :--- | :--- | :--- |
| Lista: `insertar_inicio`, `insertar_final` | Inserción en lista vacía y con datos | Pasaron 2/2 |
| Lista: `buscar` | Búsqueda existente e inexistente | Pasaron 2/2 |
| Lista: `eliminar` | Eliminar cabeza, dato medio e inexistente | Pasaron 3/3 |
| Pila: `push`, `pop`, `peek` | Operaciones básicas LIFO | Pasaron 3/3 |


## 6. Dificultades encontradas y cómo las resolvieron

| Dificultad | Cómo se resolvió |
| :--- | :--- |
| Al principio, el menú pedía escribir el nombre de la tarea para eliminarla. | Se agregó el método `obtener_por_indice` a la Lista Enlazada para poder eliminar por número (opción más amigable). |
| Sincronizar el Undo/Redo con el Árbol BST (si borro del árbol, debe volver al hacer Undo). | Se modificó la Pila para que guarde una tupla `(acción, tarea, categoría)` en lugar de solo la tarea. Así el sistema sabe exactamente en qué categoría devolverla. |
| El error al eliminar la primera tarea de la Lista (perdía la referencia). | Se agregó el caso borde reasignando la cabeza (`self.cabeza = self.cabeza.siguiente`). |

## 7. Tareas pendientes para la entrega final

| Tarea | Responsable | Fecha estimada |
| :--- | :--- | :--- |
| Escribir pruebas unitarias para el Árbol BST | Adriana | Semana 14 |
| Documentar el código con comentarios explicativos | Todo el equipo | Semana 14 |
| Grabar video de sustentación del sistema | Edward | Semana 15 |
| Preparar la presentación final | Todo el equipo | Semana 15 |

## 8. Declaración de uso de IA generativa

| Campo | Detalle |
| :--- | :--- |
| ¿Se usó IA? | Sí |
| Herramienta | DeepSeek (modelo de chat) |
| Para qué se usó | Apoyo para comprender la integración del BST con la Lista y la Pila, y para la estructuración del código base. |
| Todo el código fue revisado y comprendido por el equipo | Sí |

**Nota:** El equipo diseñó la arquitectura del sistema, implementó los métodos de las estructuras y adaptó las sugerencias generadas por la IA para cumplir con los requisitos de la materia. Todo el código ha sido probado y comprendido por los integrantes.

## 9. Enlace al commit de este checkpoint

Rama principal: `main`

Últimos 5 commits:
```text
0c69170 (HEAD -> main, origin/main, origin/HEAD) actualizar checkpoint 1 con los roles del equipo definitivo
6f0f5ae Merge branch 'main' of https://github.com/Hospina1460/INF222-Proyecto-Final-2026-2
dae727d semana 7: reorganización de la propuesta final
bfd7c30 semana 10: integrar lista enlanzadas en main.py para probar el sistema
a0ab8a9 semana - 10: checkpoint 1 - lista enlanzada en main.py
```