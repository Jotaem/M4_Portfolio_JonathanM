# Agenda de Contactos en Consola
Este proyecto es una versión mejorada de una agenda de contactos de consola, reescrita en Python utilizando Programación Orientada a Objetos.
La aplicación ahora guarda los datos de forma persistente en un archivo CSV, asegurando que la información no se pierda al cerrar el programa. Además, su código está estructurado de manera modular y es robusto frente a errores comunes de archivos.

## Conceptos Avanzados Aplicados 🚀
- Este proyecto demuestra los siguientes conceptos clave de Python:
- Programación Orientada a Objetos.
- Persistencia de Datos.
- Modularidad.
- Manejo de Rutas de Archivo.
- Manejo de Excepciones.

## Estructura del Código
El proyecto está dividido en los siguientes archivos:
- contacto.py: Define la clase Contacto, que actúa como plantilla para cada contacto, almacenando sus atributos (nombre, teléfono y correo).
- agenda.py: Contiene la clase Agenda, que es el cerebro del programa. Administra la lista de contactos y maneja toda la lógica para agregar, buscar, eliminar y, lo más importante, guardar y cargar los datos del archivo CSV.
- main.py: Es el punto de entrada de la aplicación. Muestra el menú interactivo al usuario y se comunica con el objeto Agenda para ejecutar las acciones.

## Requisitos del Proyecto
- Uso de variables, operadores y estructuras de datos (diccionarios).
- Implementación de sentencias condicionales (`if`, `elif`, `else`).
- Uso de bucles (`while`, `for`).
- Modularización del código con funciones.

## Cómo Ejecutar
1. Asegúrate de tener Python instalado.
2. Ejecuta el archivo desde la terminal:
   `python main.py`