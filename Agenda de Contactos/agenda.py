# agenda.py

import csv
from contacto import Contacto
import os

# Obtenemos la ruta absoluta de la carpeta donde está este script y creamos la ruta completa al archivo CSV
# Esto asegura que siempre use la ruta correcta, sin importar desde dónde se ejecute el script
DIRECTORIO_ACTUAL = os.path.dirname(os.path.abspath(__file__))
RUTA_ARCHIVO_CSV = os.path.join(DIRECTORIO_ACTUAL, 'agenda.csv')

class Agenda:
    """Gestiona una lista de contactos y su persistencia en un archivo CSV."""
    # 4. Modificamos el constructor para que use siempre la ruta correcta
    def __init__(self):
        self.contactos = []
        self.nombre_archivo = RUTA_ARCHIVO_CSV # ¡Ya no es solo 'agenda.csv'!
        self.cargar_contactos()

    def agregar_contacto(self, contacto):
        self.contactos.append(contacto)
        self.guardar_contactos()
        print(f"✅ Contacto '{contacto.nombre}' agregado exitosamente.")

    def mostrar_contactos(self):
        print("\n✔️ Lista de todos los contactos ✔️")
        if not self.contactos:
            print("La agenda está vacía.")
            return
        for contacto in self.contactos:
            print(contacto)

    def buscar_contacto(self, nombre):
        for contacto in self.contactos:
            if contacto.nombre.lower() == nombre.lower():
                print("\n📒 Información del Contacto 📒")
                print(contacto)
                return
        print("❌ El contacto no se encontró en la agenda.")

    def eliminar_contacto(self, nombre):
        contacto_a_eliminar = None
        for contacto in self.contactos:
            if contacto.nombre.lower() == nombre.lower():
                contacto_a_eliminar = contacto
                break
        
        if contacto_a_eliminar:
            self.contactos.remove(contacto_a_eliminar)
            self.guardar_contactos()
            print(f"🗑️ Contacto '{nombre}' eliminado exitosamente.")
        else:
            print("❌ El contacto no se encontró en la agenda.")

    def guardar_contactos(self):
        """Guarda la lista de contactos en el archivo CSV."""
        try:
            with open(self.nombre_archivo, 'w', newline='', encoding='utf-8') as archivo:
                writer = csv.writer(archivo)
                writer.writerow(['nombre', 'telefono', 'correo'])
                for contacto in self.contactos:
                    writer.writerow([contacto.nombre, contacto.telefono, contacto.correo])
        except IOError as e:
            print(f"🚨 Error al guardar el archivo: {e}")

    def cargar_contactos(self):
        """Carga los contactos desde el archivo CSV al iniciar."""
        try:
            with open(self.nombre_archivo, 'r', newline='', encoding='utf-8') as archivo:
                reader = csv.reader(archivo)
                next(reader) 
                for fila in reader:
                    self.contactos.append(Contacto(fila[0], fila[1], fila[2]))
        except FileNotFoundError:
            return