# main.py

# Diccionario global para almacenar los contactos
agenda = {}

def agregar_contacto():
    """Función para agregar un nuevo contacto a la agenda."""
    print("\n📑 Agregar un nuevo contacto 📑")
    nombre = input("✧ Ingrese el nombre del contacto: ")
    telefono = input("✧ Ingrese el número de teléfono: ")
    correo = input("✧ Ingrese el correo electrónico: ")
    
    # Se utiliza un diccionario como valor para almacenar los detalles del contacto
    agenda[nombre] = {"telefono": telefono, "correo": correo}
    print(f"✅ Contacto '{nombre}' agregado exitosamente.")

def buscar_contacto():
    """Función para buscar y mostrar los datos de un contacto."""
    print("\n📑 Buscar un contacto 📑")
    nombre = input("✧ Ingrese el nombre del contacto a buscar: ")
    
    # Se utiliza una sentencia condicional (if/else) para verificar si el contacto existe
    if nombre in agenda:
        contacto = agenda[nombre]
        print("\n📒 Información del Contacto 📒")
        print(f"🔸Nombre: {nombre}")
        print(f"🔸Teléfono: {contacto['telefono']}")
        print(f"🔸Correo: {contacto['correo']}")
    else:
        print("❌ El contacto no se encontró en la agenda.")

def eliminar_contacto():
    """Función para eliminar un contacto de la agenda."""
    print("\n✖️ Eliminar un contacto ✖️")
    nombre = input("✧ Ingrese el nombre del contacto a eliminar: ")
    
    if nombre in agenda:
        del agenda[nombre]
        print(f"🗑️ Contacto '{nombre}' eliminado exitosamente.")
    else:
        print("❌ El contacto no se encontró en la agenda.")

def mostrar_contactos():
    """Función para mostrar todos los contactos en la agenda."""
    print("\n✔️ Lista de todos los contactos ✔️")
    # Se utiliza un bucle for para iterar sobre las claves del diccionario
    if not agenda:
        print("La agenda está vacía.")
        return
        
    for nombre, datos in agenda.items():
        print(f"✧ {nombre}:")
        print(f"✧  Teléfono: {datos['telefono']}")
        print(f"✧  Correo: {datos['correo']}\n")

def menu_principal():
    """Muestra el menú principal y gestiona las opciones del usuario."""
    while True:  # Bucle infinito para mantener el programa en ejecución
        print("\n📒 Agenda de Contactos 📒")
        print("1. Agregar contacto")
        print("2. Buscar contacto")
        print("3. Eliminar contacto")
        print("4. Mostrar todos los contactos")
        print("5. Salir")
        
        opcion = input("Seleccione una opción: ")
        
        # Sentencias condicionales (if/elif/else) para el control de flujo
        if opcion == '1':
            agregar_contacto()
        elif opcion == '2':
            buscar_contacto()
        elif opcion == '3':
            eliminar_contacto()
        elif opcion == '4':
            mostrar_contactos()
        elif opcion == '5':
            print("👋 ¡Hasta luego!")
            break
        else:
            print("❌ Opción no válida. Por favor, intente de nuevo.")

if __name__ == "__main__":
    menu_principal()