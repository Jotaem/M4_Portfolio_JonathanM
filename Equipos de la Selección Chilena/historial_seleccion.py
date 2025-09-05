# hidtorial_seleccion.py

from datos_eliminatorias import datos_eliminatorias

def mostrar_menu_principal():
    """Imprime el menú principal de opciones en la consola."""
    print("\n🏆⚽  MENÚ - ELIMINATORIAS SELECCIÓN CHILENA  ⚽🏆"+"\n")
    print("1. 👟 Listar equipo titular por eliminatoria")
    print("2. 🏃‍♂️  Filtrar jugadores por posición")
    print("3. 🥇 Ver mundiales a los que Chile clasificó")
    print("4. 🥅 Ver puntuación en cada eliminatoria")
    print("5. Salir")
    print("\n"+"🔴⚪🔵"*10)

def listar_por_eliminatoria():
    """Muestra los equipos disponibles y lista el equipo titular de la eliminatoria seleccionada."""
    print("\n👉  Selecciona una eliminatoria para ver el equipo:")
    # Usamos un bucle 'for' con 'enumerate' para mostrar un índice amigable al usuario
    for i, eliminatoria in enumerate(datos_eliminatorias):
        print(f"{i + 1}. Eliminatoria para {eliminatoria['mundial']}")
    
    try:
        opcion_texto = input("\n👉  Ingresa el número de la eliminatoria: ")
        opcion_num = int(opcion_texto)

        if 1 <= opcion_num <= len(datos_eliminatorias):
            eliminatoria_elegida = datos_eliminatorias[opcion_num - 1]
            
            print(f"\n⚽👥  Equipo Titular: {eliminatoria_elegida['mundial']}  👥⚽")
            
            for jugador in eliminatoria_elegida['equipo_titular']:
                print(f"- {jugador['nombre']} ({jugador['posicion']})")
        else:
            print("\n⚠️  Error: Opción no válida. Por favor, elige un número de la lista.")
    except ValueError:
        print("\n⚠️  Error: Debes ingresar un número.")

def listar_por_posicion():
    """Permite al usuario elegir una posición y muestra todos los jugadores de esa posición."""
    print("\n👉 Selecciona la posición que deseas filtrar:")
    posiciones = ["Arquero", "Defensa", "Centrocampista", "Delantero"]
    for i, pos in enumerate(posiciones):
        print(f"{i + 1}. {pos}")
        
    try:
        opcion_num = int(input("\n👉 Ingresa el número de la posición: "))
        
        if 1 <= opcion_num <= len(posiciones):
            posicion_elegida = posiciones[opcion_num - 1]
            print(f"\n🧤👟 Jugadores en la posición de {posicion_elegida} 👟🧤")
            
            jugadores_encontrados = []
            
            for eliminatoria in datos_eliminatorias:
                for jugador in eliminatoria['equipo_titular']:
                    if jugador['posicion'] == posicion_elegida:
                        texto_jugador = f"{jugador['nombre']} (Eliminatoria {eliminatoria['eliminatoria']})"
                        if texto_jugador not in jugadores_encontrados:
                            jugadores_encontrados.append(texto_jugador)

            jugadores_encontrados.sort()
            for nombre in jugadores_encontrados:
                print(f"- {nombre}")

        else:
            print("\n⚠️  Error: Opción no válida.")
    except ValueError:
        print("\n⚠️  Error: Debes ingresar un número.")

def mostrar_clasificaciones():
    """Muestra un resumen de las eliminatorias a las que Chile clasificó."""
    print("\n📊🥇  Resumen de Clasificaciones a Mundiales 🥇📊")
    
    # Recorremos la lista de diccionarios
    for eliminatoria in datos_eliminatorias:
        clasificado = eliminatoria['clasifico']
        
        # condicional if/elif/else para manejar los tres casos
        if clasificado is True:
            print(f"- {eliminatoria['mundial']}: ¡Chile CLASIFICÓ! 👍")
        elif clasificado is False:
            print(f"- {eliminatoria['mundial']}: Chile NO CLASIFICÓ 👎")
        else:
            print(f"- {eliminatoria['mundial']}: {eliminatoria['clasifico']}")

def mostrar_puntuaciones():
    """Muestra los puntos obtenidos en cada eliminatoria."""
    print("\n⏱️🥅  Puntuación Final en Eliminatorias  🥅⏱️")
    
    for eliminatoria in datos_eliminatorias:
        mundial = eliminatoria['mundial']
        puntos = eliminatoria['puntos']
        
        print(f"- {mundial}: {puntos} puntos.")

def main():
    """Función principal que ejecuta el bucle del programa."""
    # bucle 'while' para que el menú se repita hasta que el usuario decida salir
    while True:
        mostrar_menu_principal()
        opcion_usuario = input("\n👉 Elige una opción: ")
        
        # if/elif/else para dirigir el flujo del programa según la opción
        if opcion_usuario == '1':
            listar_por_eliminatoria()
        elif opcion_usuario == '2':
            listar_por_posicion()
        elif opcion_usuario == '3':
            mostrar_clasificaciones()
        elif opcion_usuario == '4':
            mostrar_puntuaciones()
        elif opcion_usuario == '5':
            print("\n🔴⚪🔵 ¡Gracias por gritar con nosotros C-H-III!!!! 🔴⚪🔵")
            break
        else:
            print("\n⚠️  Opción no reconocida. Por favor, intenta de nuevo.")

if __name__ == "__main__":
    main()