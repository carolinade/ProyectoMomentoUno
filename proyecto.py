usuarios = []
prestamos = []


def registrar_usuario(nombre, numero_tarjeta):
    usuario = {"nombre": nombre, "numero_tarjeta": numero_tarjeta}
    usuarios.append(usuario)


def tomar_bicicleta(usuario, origen, destino):
    prestamo = {"usuario": usuario, "origen": origen, "destino": destino}
    prestamos.append(prestamo)


def listar_usuarios():
    print("*-------------------*") 
    print("Usuarios:")
    for usuario in usuarios:
        print(f"Nombre: {usuario['nombre']}, Número de Tarjeta: {usuario['numero_tarjeta']}")


def listar_prestamos():
    print("*--------------------*") 
    print("Préstamos:")
    for prestamo in prestamos:
        print(f"Usuario: {prestamo['usuario']}, Origen: {prestamo['origen']}, Destino: {prestamo['destino']}")


while True:
    print("*--------------------*")     
    print("Menu:")
    print("1. Registrar Usuario")
    print("2. Tomar Bicicleta en Préstamo")
    print("3. Consultar Usuarios")
    print("4. Consultar Préstamos")
    print("5. Salir")
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        nombre = input("Ingrese el nombre de usuario: ")
        numero_tarjeta = input("Ingrese el número de tarjeta: ")
        registrar_usuario(nombre, numero_tarjeta)
    elif opcion == "2":
        numero_tarjeta = input("Ingrese el número de tarjeta: ")
        origen = input("Ingrese el origen del préstamo: ")
        destino = input("Ingrese el destino del préstamo: ")
        tomar_bicicleta(numero_tarjeta, origen, destino)
    elif opcion == "3":
        listar_usuarios()
    elif opcion == "4":
        listar_prestamos()
    elif opcion == "5":
        break
    else:
        print("Opción no válida. Intente de nuevo.")