# biblioteca.py

from datos import datos_autores, datos_libros
from entidades import Autor, Libro

class Biblioteca:
    def __init__(self):
        self.autores = {}
        self.libros = []
        self._cargar_datos()

    def _cargar_datos(self):
        for nombre, data in datos_autores.items():
            self.autores[nombre] = Autor(nombre, data["biografia"], data["cita_famosa"])
        for data_libro in datos_libros:
            nombre_autor = data_libro["autor"]
            if nombre_autor in self.autores:
                autor_obj = self.autores[nombre_autor]
                libro_obj = Libro(
                    data_libro["nombre"], data_libro["testamento"], data_libro["tipo"],
                    data_libro["orden"], data_libro["cita_clave"], autor_obj
                )
                self.libros.append(libro_obj)
                autor_obj.libros.append(libro_obj)

    def mostrar_libros_por_testamento(self):
        print("\n✧✧ 📜 Libros de la Biblia 📜 ✧✧")
        antiguo = sorted([l.nombre for l in self.libros if l.testamento == "Antiguo"])
        nuevo = sorted([l.nombre for l in self.libros if l.testamento == "Nuevo"])
        print("\n📝 Antiguo Testamento:")
        for nombre in antiguo: print(f"  - {nombre}")
        print("\n📝 Nuevo Testamento:")
        for nombre in nuevo: print(f"  - {nombre}")
    
    def buscar_libro(self):
        print("\n✧✧ 🔎 Buscar un Libro 🔎 ✧✧")
        busqueda = input("Ingrese el nombre del libro: ").strip().title()
        libro_encontrado = next((l for l in self.libros if l.nombre == busqueda), None)
        if libro_encontrado:
            print(f"\n✅ ¡El libro '{busqueda}' se encuentra en la Biblia!")
            print(f"   - Autor: {libro_encontrado.autor.nombre}")
            print(f"   - Cita Clave: \"{libro_encontrado.cita_clave}\"")
        else:
            print(f"❌ El libro '{busqueda}' no se encontró.")

    def mostrar_perfil_autor(self):
        print("\n✧✧ ✍️ Ver Perfil de Autor ✍️ ✧✧")
        nombre_autor = input("Ingrese el nombre del autor: ").strip().title()
        if nombre_autor in self.autores:
            autor = self.autores[nombre_autor]
            print(f"\n--- Perfil de {autor.nombre} ---")
            print(f"Biografía: {autor.biografia}")
            if autor.cita_famosa:
                print(f"Cita Famosa: \"{autor.cita_famosa}\"")
            print("\nLibros escritos:")
            for libro in autor.libros:
                print(f"  - {libro.nombre}: \"{libro.cita_clave}\"")
            print("-" * (20 + len(autor.nombre)))
        else:
            print("❌ Autor no encontrado.")
            
    def exportar_perfil_autor(self):
        print("\n✧✧ 💾 Exportar Perfil de Autor 💾 ✧✧")
        nombre_autor = input("Ingrese el nombre del autor a exportar: ").strip().title()
        if nombre_autor in self.autores:
            autor = self.autores[nombre_autor]
            nombre_archivo = f"perfil_{autor.nombre.lower()}.txt"
            try:
                with open(nombre_archivo, 'w', encoding='utf-8') as f:
                    f.write(f"--- Perfil de {autor.nombre} ---\n")
                    f.write(f"Biografía: {autor.biografia}\n")
                    if autor.cita_famosa:
                        f.write(f"Cita Famosa: \"{autor.cita_famosa}\"\n")
                    f.write("\nLibros escritos:\n")
                    for libro in autor.libros:
                        f.write(f"  - {libro.nombre}: \"{libro.cita_clave}\"\n")
                print(f"\n✅ Perfil exportado exitosamente a '{nombre_archivo}'")
            except IOError as e:
                print(f"🚨 Error al escribir el archivo: {e}")
        else:
            print("❌ Autor no encontrado.")