# contacto.py

class Contacto:
    """Representa un contacto con nombre, teléfono y correo."""
    def __init__(self, nombre, telefono, correo):
        self.nombre = nombre
        self.telefono = telefono
        self.correo = correo

    def __str__(self):
        """Devuelve una representación en string del contacto, con el estilo original."""
        return f"✧ {self.nombre}:\n✧  Teléfono: {self.telefono}\n✧  Correo: {self.correo}\n"