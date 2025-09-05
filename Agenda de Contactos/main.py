# main.py

from agenda import Agenda
from contacto import Contacto

def mostrar_menu():
    print("\n📒 Agenda de Contactos 📒")
    print("1. Agregar contacto")
    print("2. Buscar contacto")
    print("3. Eliminar contacto")
    print("4. Mostrar todos los contactos")
    print("5. Salir")

def main():
    mi_agenda = Agenda()

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            print("\n📑 Agregar un nuevo contacto 📑")
            nombre = input("✧ Ingrese el nombre del contacto: ")
            telefono = input("✧ Ingrese el número de teléfono: ")
            correo = input("✧ Ingrese el correo electrónico: ")
            nuevo_contacto = Contacto(nombre, telefono, correo)
            mi_agenda.agregar_contacto(nuevo_contacto)
        elif opcion == '2':
            print("\n📑 Buscar un contacto 📑")
            nombre = input("✧ Ingrese el nombre del contacto a buscar: ")
            mi_agenda.buscar_contacto(nombre)
        elif opcion == '3':
            print("\n✖️ Eliminar un contacto ✖️")
            nombre = input("✧ Ingrese el nombre del contacto a eliminar: ")
            mi_agenda.eliminar_contacto(nombre)
        elif opcion == '4':
            mi_agenda.mostrar_contactos()
        elif opcion == '5':
            print("👋 ¡Hasta luego!")
            break
        else:
            print("❌ Opción no válida. Por favor, intente de nuevo.")

if __name__ == "__main__":
    main()