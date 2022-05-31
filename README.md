# sistema-banco
Simula las diferentes transacciones que se llevan en un cajero de un banco; desde un programa diseñado
por python, que incorpora:
-sentencias de asignación
-sentencias de condicional
-sentencia control iterativo
-variables de control
-funciones y arreglos
Transacciones u operaciones posibles son (en todas tomar la fecha del evento):
1.Registrar los datos del usuario:
-cédula, nombre, apellidos, edad, fecha de apertura
2.La apertura de cada cuenta debe contar con un saldo inicial.
3.Se permite realizar consignaciones (depósitos, retiros, consultas de saldo, prestamos).
4.Permite el préstamo de máximo 4 veces el saldo en la cuenta, siempre y cuando no tenga saldos pendientes.
5.Los saldos: por préstamos y por capital asignado.
6.Debe permitir registrar y consultar todas las operaciones efectuadas por el usuario.
7.Al salir de la ejecución del programa debe salir todo el reporte de la cuenta.
8.Mientras exista una deuda no puede retirar capital ni sacar nuevos préstamos.
9.En caso de que el abono sea superior a la deuda, el saldo se adiciona al capital.
10. En caso de retiro no se puede retirar el valor mínimo de apertura (50.000).
