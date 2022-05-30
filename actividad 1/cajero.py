import datetime
# BASE DE DATOS DE USUARIOS
BD = []
# FIN DE BASE DE DATOS DE USUARIOS
salir = False


# FUNCIONES
def registrar():
    nombre = input("ingrese su nombre: ")
    apellido = input("ingrese su apellido: ")
    cedula = float(input("ingrese su cedula: "))
    edad = input("ingrese su edad: ")
    fecha = datetime.datetime.now()
    saldo = float(input("ingrese su saldo: "))

    if saldo > 1000:
        print("usted ha sido aprobado")

    else:
        print("ingrese un saldo mayor a 1000")
        saldo = float(input("ingrese su saldo: "))

    cuenta = (nombre, apellido, cedula, edad, fecha, saldo)
    BD.append(cuenta)
    print(BD)


def ingresar(cuenta):
    for i in BD:
        if i[2] == cuenta:
            print("Bienvenido", i[0], i[1])
            return True
    return False


def depositar(cuenta):
    for i in BD:
        if i[2] == cuenta:
            saldo = float(input("ingrese el monto a depositar: "))
            i[5] += saldo
            print("Saldo actual: ", i[5])
            if i[5] < i[6]:
                saldo -= i[6]
                print("usted tiene un prestamo pendiente de: ", i[6])
                print("Saldo actual: ", i[5])
            return True
    return False


def retirar(cuenta):
    for i in BD:
        if i[2] == cuenta:
            saldo = float(input("ingrese el monto a retirar: "))
            i[5] -= saldo
            print("Saldo actual: ", i[5])
            return True
    return False


def consultar(cuenta):
    for i in BD:
        if i[2] == cuenta:
            print("Bienvenido", i[0], i[1])
            print("Saldo actual: ", i[5])
            return True
    return False


def prestamo(cuenta):
    for i in BD:
        if i[2] == cuenta:
            print("Bienvenido", i[0], i[1])
            print("Saldo actual: ", i[5])
            prestamo = float(input("ingresa valor a prestar: ",))
            DB.append(prestamo)
            return True
    return False


# FIN FUNCIONES


# PROGRAMA PRINCIPAL

# INTERFAZ PRINCIPAL

print("===============================================================")
print("=                      BANCO IMPERIAL                         =")
print("===============================================================")
print("===============================================================")
print("=                       C CREAR CUENTA                        =")
print("=                       I INGRESAR                            =")
print("=============             . salir                   ===========")
print("===============================================================")
op = input("opcion: ")

# FIN DE INTERFAZ PRINCIPAL
if op == "c":
    registrar()

    print("===============================================================")
    print("=                      BANCO IMPERIAL                         =")
    print("===============================================================")
    print("===============================================================")
    print("=                       C CREAR CUENTA                        =")
    print("=                       I INGRESAR                            =")
    print("===============================================================")
    print("=============             . salir                   ===========")
    print("===============================================================")
op = input("opcion: ")

if op == "i":
    cuenta = input("ingrese su numero de cuenta: ")
    
    ingresar(cuenta)

    print("===============================================================")
    print("=                      BANCO IMPERIAL                         =")
    print("===============================================================")
    print("===============================================================")
    print("=                    ESCOJA SU MOVIMIENTO                     =")
    print("=                       D DEPOSITAR                           =")
    print("=                       R RETIRAR                             =")
    print("=                       P PRESTAMO                            =")
    print("=                       S CONSULTAR                           =")
    print("===============================================================")
    print("=============            . salir                  =============")
    print("===============================================================")
    op = input("opcion: ")
    if op == "d":
        cuenta = input("ingrese su numero de cuenta: ")

        depositar(cuenta)
    if op == "r":
        cuenta = input("ingrese su numero de cuenta: ")
        retirar(cuenta)
    if op == "p":
        cuenta = input("ingrese su numero de cuenta: ")
        prestamo(cuenta)
    if op == "s":
        cuenta = input("ingrese su numero de cuenta: ")
        consultar(cuenta)

if op == ".":
    salir = True

print(BD)
# FIN PROGRAMA PRINCIPAL
