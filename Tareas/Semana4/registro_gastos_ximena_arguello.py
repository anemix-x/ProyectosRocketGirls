gastos = []
conteo_registros = 0

def registrar_gasto(descripcion, monto):
    if monto <= 0:
        raise ValueError("El monto del gasto debe ser mayor que cero.")
    return (descripcion, monto)

def listado_gastos(gastos, simbolo_moneda="¢"):
    if not gastos:
        return "No hay gastos registrados."
    listado = "Listado de gastos:\n"
    for i, (descripcion, monto) in enumerate(gastos, start=1):
        listado += f"{i}. {descripcion}: {simbolo_moneda}{monto:.2f}\n"
    return listado

def resumen_gastos(gastos):
    if not gastos:
        return "No hay gastos registrados."
    total = sum(monto for _, monto in gastos)
    promedio = total / len(gastos)
    mayor_gasto = max(gastos, key=lambda x: x[1])
    descripcion_mayor, monto_mayor = mayor_gasto
    return f"Total de gastos: ¢{total:.2f}\nPromedio por gasto: ¢{promedio:.2f}\nMayor gasto: {descripcion_mayor}= ¢{monto_mayor:.2f}"

def exit_program():
     print(f"Cantidad de registros exitosos realizados: {conteo_registros}")
     print("Saliendo del programa. Bye!")
     exit()

print("Bienvenido al programa de registro de gastos.")
def mostrar_opciones(): #definir el menu de opciones para el usuario
    print("++++++++++++++")
    print("1. Registrar un gasto")
    print("2. Ver listado de gastos")
    print("3. Ver resumen de gastos")
    print("4. Salir")

while True:
    mostrar_opciones()
    opcion = input("Seleccione una opcion: ") #mostrar el menu de opciones y solicitar que elija una
    #opciones ennumeradas 
    if opcion == "1":
        descripcion = input("Ingrese la descripción del gasto: ")
        try:
            monto = float(input("Ingrese el monto del gasto: ¢"))
            gasto = registrar_gasto(descripcion, monto)
            gastos.append(gasto)
            conteo_registros += 1
            print("Gasto registrado.")
        except ValueError as e:
            print(f"Error: {e}")
        if monto <= 0:
                    raise ValueError("El monto del gasto debe ser mayor que cero.")
    elif opcion == "2":
        print(listado_gastos(gastos))
    elif opcion == "3":
        print(resumen_gastos(gastos))
    elif opcion == "4":
       exit_program()       