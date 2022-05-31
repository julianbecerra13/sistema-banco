import datetime
# BASE DE DATOS DE USUARIOS
BD = []
# FIN DE BASE DE DATOS DE USUARIOS


# FUNCIONES
def registrar():
    nombre = input("ingrese nombres: ")
    apellido = input("ingrese apellidos: ")
    cedula = input("ingrese numero de identificacion: ")
    edad = int(input("ingrese su edad: "))

    while edad >= 99:
        print("ingrese una edad valida")
        edad = int(input("ingrese su edad: "))

    fecha = datetime.datetime.now()
    saldo = int(input("ingrese su saldo inicial: "))
    prestamos = 0

    if saldo >= 50000:
        print("usted ha sido aprobado")

    else:
        print("ingrese un saldo mayor o igual a 50.000")
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
    for cuenta in BD:
        if cuenta[2] == cedula:
            deposito = int(input("ingrese el monto a depositar: "))
            if deposito <= cuenta[6]:
                cuenta[6] -= deposito
            else:
                cuenta[5] += deposito - cuenta[6]
                cuenta[6] = 0
            print("deposito exitoso")
            print("Saldo actual: ", cuenta[5])
            print("usted tiene un prestamo pendiente de: ", cuenta[6])


def retirar(cuenta):
    for i in BD:
        if i[2] == cuenta:
            saldo = int(input("ingrese el monto a retirar: "))

            if saldo > i[5]:
                print("saldo insuficiente")
            elif saldo == 50000:
                print("no puede retirar su saldo inicial")
            elif i[6] > 0:
                print("no puede retirar hasta que el prestamo sea pagado")
            else:
                i[5] -= saldo
                print("retiro exitoso")

            print("su Saldo actual es de: ", i[5])
            print("usted tiene un prestamo pendiente de: ", i[6])
            return True
    return False


def consultar(cedula):
    for cuenta in BD:
        if cuenta[2] == cedula:
            print("usuario: ", cuenta[0], cuenta[1])
            print(" su Saldo actual es de : ", cuenta[5])
            print(" su prestamo a deber es de : ", cuenta[6])

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
                print("prestamo aprobado")
            else:
                print("ya tienes un prestamo pendiente:", cuenta[6])


# FIN FUNCIONES

# PROGRAMA PRINCIPAL
# INTERFAZ PRINCIPAL
opcion = -100
while opcion != 0:
    print(
        '''
                    |===============================================================|
                    |=                      BANCO IMPERIAL                         =|
                    |===============================================================|
                    |===============================================================|
                    |=                       1 CREAR CUENTA                        =|
                    |=                       2 INGRESAR                            =|
                    |===============================================================|
                    |=============             0 salir                   ===========|
                    |===============================================================|
        ''')
    opcion = int(input("opcion: "))

 # FIN DE INTERFAZ PRINCIPAL

    if opcion == 1:
        registrar()

    elif opcion == 2:
        cuenta = input("ingrese numero de cedula: ")
# INTERFAZ DE INGRESO
        if ingresar(cuenta):
            op = -100
            while op != 0:

                print('''
                    |===============================================================|
                    |=                      BANCO IMPERIAL                         =|
                    |===============================================================|
                    |===============================================================|
                    |=                    ESCOJA SU MOVIMIENTO                     =|
                    |=                       1 DEPOSITAR                           =|
                    |=                       2 RETIRAR                             =|
                    |=                       3 PRESTAMO                            =|
                    |=                    4 CONSULTAR SALDO                        =|
                    |===============================================================|
                    |=============           0 regresar                =============|
                    |===============================================================|
                    ''')
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
# FIN DE INTERFAZ DE INGRESO

    else:
        print("opcion invalida")

print(BD)
# FIN PROGRAMA PRINCIPAL
