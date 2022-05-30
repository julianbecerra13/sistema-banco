import datetime
# BASE DE DATOS DE USUARIOS
BD = []
# FIN DE BASE DE DATOS DE USUARIOS


# FUNCIONES
def registrar():
    nombre = input("ingrese su nombre: ")
    apellido = input("ingrese su apellido: ")
    cedula = input("ingrese su cedula: ")
    edad = input("ingrese su edad: ")
    fecha = datetime.datetime.now()
    saldo = int(input("ingrese su saldo: "))
    prestamos = 0

    if saldo > 1000:
        print("usted ha sido aprobado")

    else:
        print("ingrese un saldo mayor a 1000")
        saldo = int(input("ingrese su saldo: "))

    cuenta = [nombre, apellido, cedula, edad, fecha, saldo, prestamos]
    BD.append(cuenta)


def ingresar(cuenta):
    for i in BD:
        if i[2] == cuenta:
            print("Bienvenido", i[0], i[1])
            return True
    return False


def depositar(cuenta):
    for i in BD:
        if i[2] == cuenta:
            deposito = int(input("ingrese el monto a depositar: "))
            if deposito <= i[6]:
                i[6] -= deposito
            else:
                i[5] += deposito - i[6]
                i[6]= 0

            print("usted tiene un prestamo pendiente de: ", i[6])
            print("Saldo actual: ", i[5])


def retirar(cuenta):
    for i in BD:
        if i[2] == cuenta:
            saldo = int(input("ingrese el monto a retirar: "))
            
            if saldo > i[5]:
                print("saldo insuficiente")
            else:
                i[5] -= saldo
                print("retiro exitoso")

            print("Saldo actual: ", i[5])
            return True
    return False


def consultar(cedula):
    for cuenta in BD:
        if cuenta[2] == cedula:
            print("Bienvenido", cuenta[0], cuenta[1])
            print("Saldo actual: ", cuenta[5])
            print("prestamo a deber: ", cuenta[6])
            return True
    return False


def prestamo(cedula):
    for cuenta in BD:
        if cuenta[2] == cedula:
            print("Bienvenido", cuenta[0], cuenta[1])
            print("Su saldo actual es: ", cuenta[5])
            if cuenta[6] == 0:
                prestamo = int(input("ingrese valor a solicitar prestado: "))
                cuenta[6] = prestamo
            else:
                print("ya tienes un prestamo pendiente:", cuenta[6])


# FIN FUNCIONES

# PROGRAMA PRINCIPAL
# INTERFAZ PRINCIPAL
opcion = -100
while opcion != 0:
    print(
        '''
            ==============================================================
            =                      BANCO IMPERIAL                         =
            ===============================================================
            ===============================================================
            =                       1 CREAR CUENTA                        =
            =                       2 INGRESAR                            =
            =============             0 salir                   ===========
            ===============================================================
        ''')
    opcion = int(input("opcion: "))

    # FIN DE INTERFAZ PRINCIPAL

    if opcion == 1:
        registrar()

    elif opcion == 2:
        cuenta = input("ingrese numero de cedula: ")

        if ingresar(cuenta):
            op = -100
            while op != 0:
                print("===============================================================")
                print("=                      BANCO IMPERIAL                         =")
                print("===============================================================")
                print("===============================================================")
                print("=                    ESCOJA SU MOVIMIENTO                     =")
                print("=                       1 DEPOSITAR                           =")
                print("=                       2 RETIRAR                             =")
                print("=                       3 PRESTAMO                            =")
                print("=                    4 CONSULTAR SALDO                        =")
                print("===============================================================")
                print("=============           0 regresar                =============")
                print("===============================================================")
                op = int(input("opcion: "))
                if op == 1:

                    depositar(cuenta)
                elif op == 2:

                    retirar(cuenta)
                elif op == 3:

                    prestamo(cuenta)
                elif op == 4:

                    consultar(cuenta)
                else:
                    print("opcion invalida")
        else:
            print("cuenta no encontrada")
    else:
        print("opcion invalida")

print(BD)
# FIN PROGRAMA PRINCIPAL
