# explorador_biblia.py
from datos_biblia import libros_biblia_completo

# funciones para manipular y explorar los datos de la Biblia
def mostrar_libros():
    """Muestra los libros de la Biblia organizados por testamento."""
    print("\n✧✧ 📜 Libros de la Biblia 📜 ✧✧")
    
    # Uso de listas por comprensión para filtrar libros por testamento
    antiguo_testamento = [libro["nombre"] for libro in libros_biblia_completo if libro["testamento"] == "Antiguo"]
    nuevo_testamento = [libro["nombre"] for libro in libros_biblia_completo if libro["testamento"] == "Nuevo"]
    
    print("\n📝 Antiguo Testamento:")
    for libro in antiguo_testamento:
        print(f"  - {libro}")
    
    print("\n📝 Nuevo Testamento:")
    for libro in nuevo_testamento:
        print(f"  - {libro}")

def buscar_libro():
    """Busca un libro en la lista de datos y verifica si existe."""
    print("\n✧✧ 🔎 Buscar un Libro 🔎 ✧✧")
    busqueda = input("Ingrese el nombre del libro a buscar: ").strip().title()
    encontrado = False # Variable booleana para el estado de la búsqueda
    
    # Bucle for para recorrer cada diccionario en la lista
    for libro in libros_biblia_completo:
        if libro["nombre"] == busqueda:
            encontrado = True
            break
    
    # Sentencia condicional para mostrar el resultado
    if encontrado:
        print(f"✅ ¡El libro '{busqueda}' se encuentra en la Biblia!")
    else:
        print(f"❌ El libro '{busqueda}' no se encontró.")

def contar_libros():
    """Cuenta y muestra el total de libros en la Biblia."""
    # La variable total_libros es un entero
    total_libros = len(libros_biblia_completo) 
    print(f"\n🔢 La Biblia contiene un total de {total_libros} libros.")

def listar_por_autor():
    """Agrupa y lista los libros por su autor bíblico."""
    print("\n✧✧ ✍️ Libros por Autor Bíblico ✍️ ✧✧")
    autores = {}
    
    # Bucle for para iterar sobre la lista y un diccionario para agrupar
    for libro in libros_biblia_completo:
        autor = libro["autor"]
        if autor not in autores:
            autores[autor] = []
        autores[autor].append(libro["nombre"])
    
    # Bucle for para imprimir los resultados
    for autor, libros in autores.items():
        print(f"\n📖 {autor}:")
        for libro in libros:
            print(f"  - {libro}")

def listar_por_tipo_literatura():
    """Agrupa y lista los libros por tipo de literatura."""
    print("\n✧✧ 📚 Libros por Tipo de Literatura 📚 ✧✧")
    tipos_literatura = {}
    
    for libro in libros_biblia_completo:
        tipo = libro["tipo"]
        if tipo not in tipos_literatura:
            tipos_literatura[tipo] = []
        tipos_literatura[tipo].append(libro["nombre"])
    
    for tipo, libros in tipos_literatura.items():
        print(f"\n📚 {tipo}:")
        for libro in libros:
            print(f"  - {libro}")

def listar_en_orden_cronologico():
    """Lista los libros de la Biblia en orden cronológico."""
    print("\n✧✧ 🕒 Libros en Orden Cronológico 🕒 ✧✧")
    # La lista ya está ordenada por la clave 'orden', solo necesitamos iterar
    for libro in libros_biblia_completo:
        print(f"({libro['orden']}) {libro['nombre']} - ({libro['testamento']} Testamento)")

def menu_principal():
    """Maneja el menú principal y las opciones del usuario."""
    while True: # Bucle while para mantener el programa en ejecución
        print("\n✧✧ 📖 Explorador de la Biblia 📖 ✧✧")
        print("1. Mostrar todos los libros (por testamento)")
        print("2. Buscar un libro")
        print("3. Contar todos los libros")
        print("4. Listar por autor bíblico")
        print("5. Listar por tipo de literatura")
        print("6. Listar en orden cronológico")
        print("7. Salir")
        
        opcion = input("Seleccione una opción: ")
        
        # Sentencias if/elif/else para el control del flujo del menú
        if opcion == '1':
            mostrar_libros()
        elif opcion == '2':
            buscar_libro()
        elif opcion == '3':
            contar_libros()
        elif opcion == '4':
            listar_por_autor()
        elif opcion == '5':
            listar_por_tipo_literatura()
        elif opcion == '6':
            listar_en_orden_cronologico()
        elif opcion == '7':
            print("👋 ¡Hasta luego!")
            break
        else:
            print("❌ Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    menu_principal()