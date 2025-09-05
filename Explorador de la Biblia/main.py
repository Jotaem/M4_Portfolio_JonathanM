# main.py

from biblioteca import Biblioteca

def menu_principal():
    biblioteca = Biblioteca()
    while True:
        print("\n✧✧ 📖 Explorador de la Biblia (Avanzado) 📖 ✧✧")
        print("1. Mostrar todos los libros")
        print("2. Buscar un libro (y ver su cita clave)")
        print("3. Ver perfil de autor (biografía y obras)")
        print("4. Exportar perfil de autor a .txt")
        print("5. Salir")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == '1':
            biblioteca.mostrar_libros_por_testamento()
        elif opcion == '2':
            biblioteca.buscar_libro()
        elif opcion == '3':
            biblioteca.mostrar_perfil_autor()
        elif opcion == '4':
            biblioteca.exportar_perfil_autor()
        elif opcion == '5':
            print("Adiós! Hasta pronto!")
            break
        else:
            print("❌ Opción no válida intente de nuevo.")

if __name__ == "__main__":
    menu_principal()