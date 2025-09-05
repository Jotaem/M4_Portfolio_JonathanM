# Portafolio Módulo 4: Proyectos Avanzados en Python 🐍

Este repositorio contiene la evolución de tres proyectos de consola desarrollados en Python, refactorizados para aplicar y demostrar conceptos de programación avanzada.
Cada programa ha sido reestructurado utilizando **Programación Orientada a Objetos (POO)**, se ha añadido **gestión de archivos** para la persistencia de datos y se ha mejorado la **modularidad** y el **manejo de errores**, llevando las aplicaciones a un nivel superior de calidad y diseño.

## Conceptos Avanzados Aplicados

Este portafolio demuestra el dominio de los siguientes conceptos clave:

* **Programación Orientada a Objetos (POO):** Uso de Clases, Objetos, Atributos, Métodos y Composición para un diseño de software escalable.
* **Persistencia de Datos:** Capacidad de leer y escribir en archivos externos (`.csv`, `.txt`) para que la información no se pierda.
* **Modularidad y Código Escalable:** Separación del código en distintos archivos (`entidades`, `lógica`, `main`), cada uno con una responsabilidad única.
* **Manejo de Excepciones:** Uso de `try-except` para un control robusto de errores, como entradas de usuario inválidas o problemas con archivos.

---
## Proyectos Incluidos

### 1. Agenda de Contactos (Avanzada) 📞
Una aplicación de agenda que ahora **guarda los datos de forma persistente en un archivo CSV**. El código está completamente reescrito con clases como `Contacto` y `Agenda`.

* **Ubicación:** Carpeta `Agenda de Contactos/`
* **Ejecutar con:** `python main.py`

### 2. Estadísticas de la Selección Chilena (Avanzada) ⚽
Un explorador de datos históricos de la selección, ahora modelado con clases como `Jugador` y `Eliminatoria`. Incluye una nueva función para **exportar alineaciones a archivos `.txt`**.

* **Ubicación:** Carpeta `Equipos de la Selección Chilena/`
* **Ejecutar con:** `python main.py`

### 3. Explorador de la Biblia (Avanzado) 📖
Una herramienta de exploración bíblica enriquecida con perfiles de autor, biografías y citas clave. El sistema está basado en clases como `Libro`, `Autor` y `Biblioteca`, y permite **exportar perfiles de autor a archivos `.txt`**.

* **Ubicación:** Carpeta `Explorador de la Biblia/`
* **Ejecutar con:** `python main.py`