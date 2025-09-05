# main.py

from historial_seleccion import Historial

def mostrar_menu_principal():
    """Imprime el menú principal de opciones en la consola."""
    print("\n🏆⚽  MENÚ - ELIMINATORIAS SELECCIÓN CHILENA  ⚽🏆"+"\n")
    print("1. 👟 Listar equipo titular por eliminatoria")
    print("2. 🏃‍♂️  Filtrar jugadores por posición")
    print("3. 🥇 Ver mundiales a los que Chile clasificó")
    print("4. 🥅 Ver puntuación en cada eliminatoria")
    print("5. 💾 Exportar equipo a un archivo de texto (.txt)")
    print("6. Salir")
    print("\n"+"🔴⚪🔵"*10)

def main():
    """Función principal que ejecuta el bucle del programa."""
    historial_chile = Historial()

    while True:
        mostrar_menu_principal()
        opcion_usuario = input("\n👉 Elige una opción: ")
        
        if opcion_usuario == '1':
            historial_chile.listar_por_eliminatoria()
        elif opcion_usuario == '2':
            historial_chile.listar_por_posicion()
        elif opcion_usuario == '3':
            historial_chile.mostrar_clasificaciones()
        elif opcion_usuario == '4':
            historial_chile.mostrar_puntuaciones()
        elif opcion_usuario == '5':
            historial_chile.exportar_equipo_a_txt()
        elif opcion_usuario == '6':
            print("\n🔴⚪🔵 ¡Gracias por gritar con nosotros C-H-III!!!! 🔴⚪🔵")
            break
        else:
            print("\n⚠️  Opción no reconocida. Por favor, intenta de nuevo.")

if __name__ == "__main__":
    main()