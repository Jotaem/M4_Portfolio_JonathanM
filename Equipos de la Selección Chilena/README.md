# Proyecto: Estadísticas de la Selección Chilena (Versión con POO) ⚽
Este es un programa de consola que permite consultar información histórica sobre las últimas 10 participaciones de la selección chilena de fútbol en las eliminatorias para la Copa del Mundo.
Esta versión ha sido **refactorizada** para utilizar **Programación Orientada a Objetos (POO)**, haciendo el código más modular, escalable y fácil de mantener. Además, incluye una nueva funcionalidad para **exportar datos a archivos de texto**.

## Conceptos Avanzados Aplicados 🚀

* **Programación Orientada a Objetos:** El proyecto está estructurado en clases (`Jugador`, `Eliminatoria`, `Historial`) que modelan las entidades del mundo real y encapsulan la lógica de negocio.
* **Gestión de Archivos:** Se ha añadido la capacidad de escribir archivos `.txt` para exportar las alineaciones de los equipos, demostrando el manejo de archivos.
* **Modularidad:** El código está organizado en tres archivos (`entidades.py`, `historial.py`, `main.py`), cada uno con una responsabilidad específica.
* **Manejo de Excepciones:** Se utiliza `try-except` para un control robusto de las entradas del usuario y de posibles errores al escribir archivos.

## Estructura del Código 📂

* **`datos_eliminatorias.py`:** Contiene los datos brutos de las eliminatorias.
* **`entidades.py`:** Define las clases `Jugador` y `Eliminatoria`, que son los "moldes" para nuestros datos.
* **`historial.py`:** Contiene la clase `Historial`, que actúa como el motor del programa, cargando los datos y manejando toda la lógica.
* **`main.py`:** Es el punto de entrada que muestra el menú y se comunica con el objeto `Historial`.

## Cómo Ejecutar ▶️

1.  Asegúrate de tener todos los archivos en la misma carpeta.
2.  Ejecuta el archivo principal desde la terminal:
    ```bash
    python main.py
    ```
3.  Sigue las instrucciones del menú. Al usar la opción de exportar, se creará un archivo `.txt` en la misma carpeta.