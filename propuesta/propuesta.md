# Propuesta de Proyecto Final
INF 222 Estructura de Datos · Semestre 2026-2
Entrega: Semana 7

---

## Datos del equipo

| Campo | Información |
|-------|-------------|
| Nombre del equipo | Team TaskFlow |
| Integrante 1 | Edward Hospina · 8-782-940 · edward.hospina@up.ac.pa |
| Integrante 2 | Julieth Huerta · 8-1050-2149 · julieth-s.huerta-h@up.ac.pa |
| Integrante 3 | Maria Gonzalez · 9-761-1980 · maria.gonzalez44@up.ac.pa |

---

## Tema elegido

☒ **1** · ☐ 2 · ☐ 3 · ☐ 4 · ☐ 5 · ☐ Propuesta propia

**Nombre del sistema:** "TaskFlow — Gestor de Tareas con Deshacer/Rehacer"

---

## Descripción del problema

En la vida universitaria y profesional, es común manejar múltiples tareas al mismo tiempo y cometer errores al organizarlas (como borrar una tarea importante por accidente). TaskFlow es un sistema de gestión de tareas que permite crear pendientes, categorizarlos y, sobre todo, ofrece la funcionalidad de "Deshacer" (Undo) y "Rehacer" (Redo). Es relevante porque optimiza la organización personal y brinda una red de seguridad al usuario, garantizando que ninguna acción sea irreversible, usando la estructura de datos adecuada para el historial.

---

## Estructuras de datos a usar y justificación

| Estructura | Propósito en el sistema | ¿Por qué esta y no otra? |
|------------|------------------------|--------------------------|
| **Pila (Stack)** | Mantener el historial de acciones para Deshacer/Rehacer. | El principio LIFO es perfecto para esto: la última acción realizada es la primera que se debe deshacer. |
| **Lista Enlazada Simple** | Almacenar la lista de tareas pendientes. | Permite insertar nuevas tareas al inicio o al final en O(1), y eliminar tareas completadas fácilmente re-enlazando los nodos. |
| **Árbol (BST)** | Organizar las tareas por categorías (ej. Universidad, Personal, Trabajo). | Un Árbol Binario de Búsqueda permite buscar, insertar y agrupar tareas por categoría de manera muy eficiente en O(log n). |

---

## Alcance funcional (qué hará el sistema)

- ☐ **Funcionalidad 1:** Registrar nuevas tareas (título, descripción y categoría) usando la lista enlazada.
- ☐ **Funcionalidad 2:** Listar todas las tareas pendientes y marcarlas como completadas.
- ☐ **Funcionalidad 3:** Organizar y mostrar tareas por categorías usando el Árbol.
- ☐ **Funcionalidad 4:** Implementar "Deshacer" (Undo) usando la Pila (ej. si se borra una tarea por error, se recupera).
- ☐ **Funcionalidad 5:** Implementar "Rehacer" (Redo) para revertir un "Deshacer".
- ☐ **Funcionalidad 6:** Interfaz de usuario por consola (menú interactivo con opciones).

---

## Distribución de roles

| Integrante | Área de responsabilidad principal |
|------------|-----------------------------------|
| Edward Hospina | Implementación de la Pila (Undo/Redo) y la Lista Enlazada de tareas. |
| Julieth Huerta | Implementación del Árbol de categorías (BST) y búsqueda por categoría. |
| Maria Gonzalez | Interfaz de usuario (menú por consola), integración de módulos y pruebas. |

**Nota:** todos deben poder explicar todo el código. Los roles no implican que otros no participen en esa área.

---

## Cronograma tentativo

| Semana | Meta del equipo |
|--------|-----------------|
| 3-6 | Definir clases base de las estructuras de datos (Nodos, Pila, Lista, Árbol). |
| 7 | Entrega de esta propuesta. |
| 7-9 | Implementación de la Lista Enlazada (tareas) y la Pila (Undo/Redo). |
| 10 | Checkpoint 1: Registro de tareas y Undo/Redo funcionando en consola. |
| 10-13 | Integración del Árbol de categorías y lógica completa del sistema. |
| 14 | Checkpoint 2: Sistema completo con UI por consola y casos borde probados. |
| 15 | Entrega final y sustentación. |

---

## Declaración de integridad académica

Todos los integrantes firmantes declaran que:

1. El trabajo es original y de nuestra autoría.
2. El uso de IA generativa, si ocurre, será declarado explícitamente en cada entrega.
3. Comprendemos la política de integridad académica del curso.

**Firmas (nombres digitados equivalen a firma en la entrega virtual):**

- Edward Hospina
- Julieth Huerta
- Maria Gonzalez