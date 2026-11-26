# TaskFlow: Gestor de Tareas con Deshacer/Rehacer — Proyecto Final INF 222
Semestre 2026-2 · Equipo: Team TaskFlow

## Descripción del sistema
TaskFlow es un sistema de gestión de tareas por consola que permite a los usuarios crear pendientes, categorizarlos y, lo más importante, ofrece la funcionalidad de "Deshacer" (Undo) y "Rehacer" (Redo). 
El sistema resuelve el problema de la pérdida de información por errores humanos (como borrar una tarea accidentalmente), brindando una red de seguridad al usuario. Es útil para estudiantes y profesionales que necesitan organizar sus actividades diarias de forma segura y categorizada.

## Requisitos e instalación
```bash
# Python 3.12 o superior
python --version

# Clonar el repositorio
git clone https://github.com/Hospina1460/INF222-Proyecto-Final-2026-2.git
cd INF222-Proyecto-Final-2026-2

# No se requieren dependencias externas salvo Python estándar
```
## Cómo ejecutar el sistema
```bash
cd src
python main.py
```
El menú interactivo cuenta con las siguientes opciones:

• Opción 1: Agregar tarea (solicita título y categoría).

• Opción 2: Mostrar tareas (general).

• Opción 3: Eliminar tarea (por número de índice).

• Opción 4: Deshacer (Undo) la última acción.

• Opción 5: Rehacer (Redo) la última acción deshecha.

• Opción 6: Ver tareas por Categoría (usando el recorrido inorden del BST).

• Opción 7: Salir.

## Estructura de datos utilizada
| Estructura | Clase / Archivo | Uso en el sistema | Por qué esta estructura |
| :--- | :--- | :--- | :--- |
| Lista Enlazada Simple | `estructuras/lista_enlazada.py` | Almacenar la lista de tareas pendientes. | Permite insertar y eliminar tareas fácilmente mediante re-enlace de nodos. |
| Pila (Stack) | `estructuras/pila.py` | Mantener el historial de acciones para Undo/Redo. | El principio LIFO (Last In, First Out) es idóneo para revertir acciones en orden inverso. |
| Árbol Binario de Búsqueda (BST) | `estructuras/arbol_bst.py` | Organizar y agrupar las tareas por categorías. | Permite buscar e insertar categorías eficientemente en O(log n) y mostrarlas en orden alfabético. |

## Análisis de complejidad de ls operaciones principales
| Operación | Complejidad temporal | Complejidad espacial | Estructura involucrada |
| :--- | :--- | :--- | :--- |
| Insertar tarea | O(n) | O(1) | Lista Enlazada (inserción al final) |
| Buscar/Eliminar tarea | O(n) | O(1) | Lista Enlazada (búsqueda secuencial) |
| Push / Pop (Undo/Redo) | O(1) | O(1) | Pila (operaciones en el tope) |
| Insertar/Buscar categoría | O(log n) promedio | O(1) | Árbol BST |

## Cómo ejecutar las pruebas
```bash
# Desde la raíz del proyecto, usando el módulo unittest estándar
python -m unittest src/tests/test_estructuras.py
```
## Contribución de cada estudiante

| Integrante | Commits (aprox.) | Área de contribución principal |
| :--- | :--- | :--- |
| Edward Hospina | 15 commits | Integración en `main.py`, interfaz de menú, pruebas y documentación. |
| Julieth Huerta | 4 commits | Implementación de la lógica del Árbol BST y recorrido inorden. |
| Maria Gonzalez | 5 commits | Implementación de la Lista Enlazada y la Pila. |
| Adriana Pineda | 4 commits | Revisión de casos borde, apoyo en pruebas unitarias y diseño de casos de prueba. |

## Declaración de uso de IA generativa
| Campo | Detalle |
| :--- | :--- |
| Herramienta(s) usadas | DeepSeek (modelo de chat) |
| Partes donde se usó | Apoyo para comprender la integración de estructuras y estructuración del código base. |
| Partes desarrolladas sin IA | La lógica de los métodos de las estructuras, la integración en el menú, la corrección de errores y las pruebas unitarias. |
| El equipo comprende todo el código | Sí. Todo el código fue revisado, adaptado y probado por los integrantes. |

## Lecciones aprendidas
Lo más difícil fue sincronizar las tres estructuras de datos al mismo tiempo, por ejemplo, asegurarse de que al usar "Undo" en una tarea eliminada, esta se recuperara correctamente no solo en la Lista, sino también en el Árbol de categorías.

Si empezáramos de nuevo, dedicaríamos más tiempo al diseño de la arquitectura y a la escritura de pruebas unitarias desde el principio, para detectar errores de integración antes de tener todo el código conectado.
