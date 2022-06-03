import datetime
# BASE DE DATOS DE USUARIOS
BD = []
# FIN DE BASE DE DATOS DE USUARIOS


# FUNCIONES
def registrar():
    operaciones = []
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
        print("|===============================================================|")
        print("                      USTED A SIDO REGISTRADO                   ")                           
        print("|===============================================================|")

    else:
        print("ingrese un saldo mayor o igual a 50.000")
        saldo = int(input("ingrese su saldo: "))

    cuenta = [nombre, apellido, cedula, edad,
              fecha, saldo, prestamos, operaciones]
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
                operacion = {
                    "fecha": datetime.datetime.now(),
                    "tipo": "deposito",
                    "monto": deposito
                }
                i[7].append(operacion)
            else:
                i[5] += deposito - i[6]
                i[6] = 0
                operacion = {
                    "fecha": datetime.datetime.now(),
                    "tipo": "deposito",
                    "monto": deposito
                }
                i[7].append(operacion)
            print("|===============================================================|")
            print("                      deposito exitoso                           ")
            print("|===============================================================|")
            print("Saldo actual: ", i[5])
            print("usted tiene un prestamo pendiente de: ", i[6])


def retirar(cuenta):
    for i in BD:
        if i[2] == cuenta:
            saldo = int(input("ingrese el monto a retirar: "))

            if saldo > i[5]:
                print("saldo insuficiente")
            elif saldo < 0:
                print("ingrese un valor positivo")
            elif saldo == 50000:
                print("no puede retirar su saldo inicial")
            elif i[6] > 0:
                print("no puede retirar hasta que el prestamo sea pagado")
            else:
                i[5] -= saldo
                print(
                    "|===============================================================|")
                print(
                    "                      retiro exitoso                             ")
                print(
                    "|===============================================================|")
                operacion = {
                    "fecha": datetime.datetime.now(),
                    "tipo": "retiro",
                    "monto": saldo
                }
                i[7].append(operacion)

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
            operacion = {
                "fecha": datetime.datetime.now(),
                "tipo": "consulta",
                "monto": 0
            }
            cuenta[7].append(operacion)
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
                operacion = {
                    "fecha": datetime.datetime.now(),
                    "tipo": "prestamo",
                    "monto": prestamo
                }
                cuenta[7].append(operacion)

            elif prestamo > cuenta[5]*4:
                print(
                    "usted no puede solicitar un prestamo 4 veces mayor a su saldo inicial")
            else:
                print("ya tienes un prestamo pendiente:", cuenta[6])


def imprimir_operacion():
    print("Operaciones realizadas: ")
    print("===============================================================")
    for operacion in BD:
        for i in operacion[7]:
            print("fecha: ", i["fecha"])
            print("tipo: ", i["tipo"])
            print("monto: ", i["monto"])
            print("/n")
    print("===============================================================")

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
                    1

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

print("|===============================================================|")
for i in BD:
    imprimir_operacion()
print("|===============================================================|")
# FIN PROGRAMA PRINCIPAL
