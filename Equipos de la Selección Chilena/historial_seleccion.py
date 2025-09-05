# historial_seleccion.py

from entidades import Eliminatoria, Jugador
from datos_eliminatorias import datos_eliminatorias

class Historial:
    """Gestiona la colección de eliminatorias y las operaciones sobre ellas."""
    def __init__(self):
        self.eliminatorias = []
        self._cargar_datos()

    def _cargar_datos(self):
        """Método privado para cargar y transformar los datos en objetos."""
        for datos in datos_eliminatorias:
            eliminatoria = Eliminatoria(
                datos['mundial'],
                datos['eliminatoria'],
                datos['clasifico'],
                datos['puntos'],
                datos['equipo_titular']
            )
            self.eliminatorias.append(eliminatoria)

    def listar_por_eliminatoria(self):
        """Muestra los equipos disponibles y el equipo titular seleccionado."""
        print("\n👉  Selecciona una eliminatoria para ver el equipo:")
        for i, elim in enumerate(self.eliminatorias):
            print(f"{i + 1}. Eliminatoria para {elim.mundial}")
        
        try:
            opcion_num = int(input("\n👉  Ingresa el número de la eliminatoria: "))
            if 1 <= opcion_num <= len(self.eliminatorias):
                self.eliminatorias[opcion_num - 1].mostrar_equipo()
            else:
                print("\n⚠️  Error: Opción no válida. Por favor, elige un número de la lista.")
        except ValueError:
            print("\n⚠️  Error: Debes ingresar un número.")

    def listar_por_posicion(self):
        """Filtra y muestra jugadores por posición a lo largo de la historia."""
        print("\n👉 Selecciona la posición que deseas filtrar:")
        posiciones = ["Arquero", "Defensa", "Centrocampista", "Delantero"]
        for i, pos in enumerate(posiciones):
            print(f"{i + 1}. {pos}")
            
        try:
            opcion_num = int(input("\n👉 Ingresa el número de la posición: "))
            if 1 <= opcion_num <= len(posiciones):
                posicion_elegida = posiciones[opcion_num - 1]
                print(f"\n🧤👟 Jugadores en la posición de {posicion_elegida} 👟🧤")
                
                jugadores_encontrados = set()
                for elim in self.eliminatorias:
                    for jugador in elim.equipo_titular:
                        if jugador.posicion == posicion_elegida:
                            texto_jugador = f"{jugador.nombre} (Eliminatoria {elim.anio})"
                            jugadores_encontrados.add(texto_jugador)
                
                for nombre in sorted(list(jugadores_encontrados)):
                    print(f"- {nombre}")
            else:
                print("\n⚠️  Error: Opción no válida.")
        except ValueError:
            print("\n⚠️  Error: Debes ingresar un número.")

    def mostrar_clasificaciones(self):
        """Muestra un resumen de las clasificaciones a mundiales."""
        print("\n📊🥇  Resumen de Clasificaciones a Mundiales 🥇📊")
        for elim in self.eliminatorias:
            if elim.clasifico is True:
                print(f"- {elim.mundial}: ¡Chile CLASIFICÓ! 👍")
            elif elim.clasifico is False:
                print(f"- {elim.mundial}: Chile NO CLASIFICÓ 👎")
            else:
                print(f"- {elim.mundial}: {elim.clasifico}")

    def mostrar_puntuaciones(self):
        """Muestra los puntos obtenidos en cada eliminatoria."""
        print("\n⏱️🥅  Puntuación Final en Eliminatorias  🥅⏱️")
        for elim in self.eliminatorias:
            print(f"- {elim.mundial}: {elim.puntos} puntos.")

    def exportar_equipo_a_txt(self):
        """Exporta la alineación de una eliminatoria a un archivo .txt."""
        print("\n👉  Selecciona una eliminatoria para exportar su equipo a un archivo .txt:")
        for i, elim in enumerate(self.eliminatorias):
            print(f"{i + 1}. {elim.mundial}")

        try:
            opcion_num = int(input("\n👉  Ingresa el número de la eliminatoria a exportar: "))
            if 1 <= opcion_num <= len(self.eliminatorias):
                eliminatoria_elegida = self.eliminatorias[opcion_num - 1]
                nombre_archivo = f"equipo_{eliminatoria_elegida.anio}.txt"
                
                with open(nombre_archivo, 'w', encoding='utf-8') as archivo:
                    archivo.write(f"Equipo Titular: {eliminatoria_elegida.mundial}\n")
                    archivo.write("="*30 + "\n")
                    for jugador in eliminatoria_elegida.equipo_titular:
                        archivo.write(f"{jugador.nombre} ({jugador.posicion})\n")
                
                print(f"\n✅ ¡Equipo exportado exitosamente al archivo '{nombre_archivo}'!")
            else:
                print("\n⚠️  Error: Opción no válida.")
        except ValueError:
            print("\n⚠️  Error: Debes ingresar un número.")
        except IOError as e:
            print(f"\n🚨 Error al escribir en el archivo: {e}")