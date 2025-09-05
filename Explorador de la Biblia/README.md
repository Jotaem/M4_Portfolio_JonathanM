# Explorador de la Biblia (Versión Avanzada con POO) 📖

Este es un programa en Python desarrollado para explorar los libros de la Biblia de una manera enriquecida e interactiva. Esta versión ha sido completamente **refactorizada utilizando Programación Orientada a Objetos (POO)** para ofrecer una estructura más robusta y nuevas funcionalidades. Ahora, además de listar y buscar libros, puedes explorar **perfiles detallados de los autores bíblicos**, ver **citas clave** de cada libro y **exportar esta información a archivos de texto**.

## Conceptos Avanzados Aplicados 🚀

* **Programación Orientada a Objetos:** El proyecto se modela con clases como `Libro`, `Autor` y `Biblioteca`, encapsulando datos y lógica para un código más limpio y escalable.
* **Composición de Objetos:** Un objeto `Libro` contiene un objeto `Autor`, demostrando una relación estructural clave en POO.
* **Gestión de Archivos:** Se ha implementado la capacidad de escribir archivos `.txt` para exportar perfiles completos de autores.
* **Modularidad:** El código está organizado en cuatro archivos (`datos.py`, `entidades.py`, `biblioteca.py`, `main.py`), cada uno con una responsabilidad clara.
* **Manejo de Excepciones:** Se utiliza `try-except` para un control seguro de las operaciones de escritura de archivos y las entradas del usuario.

## Nuevas Funcionalidades ✨

* **Perfiles de Autor:** Descubre una breve biografía, una cita famosa y la lista de obras de cada autor bíblico.
* **Citas Clave:** Al buscar un libro, ahora se muestra una cita representativa del mismo.
* **Exportación a TXT:** Guarda el perfil completo de tu autor favorito en un archivo `.txt` para consultarlo cuando quieras.

## Cómo Ejecutar ▶️

1.  Asegúrate de tener los cuatro archivos (`datos.py`, `entidades.py`, `biblioteca.py`, `main.py`) en la misma carpeta.
2.  Ejecuta el archivo principal desde la terminal:
    ```bash
    python main.py
    ```