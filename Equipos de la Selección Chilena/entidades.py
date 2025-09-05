# entidades.py

class Jugador:
    """Representa a un jugador con su nombre y posición."""
    def __init__(self, nombre, posicion):
        self.nombre = nombre
        self.posicion = posicion

    def __str__(self):
        """Formato para imprimir un jugador."""
        return f"- {self.nombre} ({self.posicion})"

class Eliminatoria:
    """Representa una campaña eliminatoria completa."""
    def __init__(self, mundial, anio, clasifico, puntos, equipo_titular_data):
        self.mundial = mundial
        self.anio = anio
        self.clasifico = clasifico
        self.puntos = puntos
        self.equipo_titular = [Jugador(j['nombre'], j['posicion']) for j in equipo_titular_data]

    def mostrar_equipo(self):
        """Imprime el equipo titular de esta eliminatoria."""
        print(f"\n⚽👥  Equipo Titular: {self.mundial}  👥⚽")
        for jugador in self.equipo_titular:
            print(jugador) 