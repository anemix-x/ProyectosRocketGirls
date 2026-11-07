gastos = [] #comenzar lista vacia
conteo_registros = 0

def registrar_gasto(descripcion, monto): #definir como se van a solicitar los gastos
    if monto <= 0:
        raise ValueError("El monto del gasto debe ser mayor que cero.") #establecer que el monto debe ser mayor a 0
    return (descripcion, monto)

def listado_gastos(gastos, simbolo_moneda="¢"): #definir una funcion permanente de moneda y los gastos
    if not gastos:
        return "No hay gastos registrados." #mensaje en caso de que no se hayan registrado aun gastos
    listado = "Listado de gastos:\n"
    for i, (descripcion, monto) in enumerate(gastos, start=1): #enumerar los gastos que si hayan comenzando en 1
        listado += f"{i}. {descripcion}: {simbolo_moneda}{monto:.2f}\n" #mostrar el listado de gastos con su descripcion y monto con decimales
    return listado

def resumen_gastos(gastos): #definir el resume de gastos
    if not gastos:
        return "No hay gastos registrados." #mensaje en caso de que no se hayan registrado gastos
    total = sum(monto for _, monto in gastos) #suma de los gastos
    promedio = total / len(gastos) #promedio de los gastos
    mayor_gasto = max(gastos, key=lambda x: x[1]) #identificar el mayor gasto
    descripcion_mayor, monto_mayor = mayor_gasto
    return f"Total de gastos: ¢{total:.2f}\nPromedio por gasto: ¢{promedio:.2f}\nMayor gasto: {descripcion_mayor}= ¢{monto_mayor:.2f}" #mensaje que muestra el total, promedio y mayor gasto con descripcion y monto

def exit_program(): #definir que ocurre al salir del programa
     print(f"Cantidad de registros exitosos realizados: {conteo_registros}") #agregar el conteo de registros realizados
     print("Saliendo del programa. Bye!") #mensaje de despedida
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
    if opcion == "1":
        descripcion = input("Ingrese la descripción del gasto: ")
        try:
            monto = float(input("Ingrese el monto del gasto: ¢")) #solicitar un numero que puede tener decimales
            gasto = registrar_gasto(descripcion, monto) #registar el gasto con la descripcion y el monto
            gastos.append(gasto) #agregar el gasto a la lista
            conteo_registros += 1 #sumar 1 al conteo de registros
            print("Gasto registrado.")
        except ValueError as e:
            print(f"Error: {e}") #mensaje de error en caso de que el monto sea menor o igual a 0
        if monto <= 0:
                    raise ValueError("El monto del gasto debe ser mayor que cero.")
    elif opcion == "2":
        print(listado_gastos(gastos)) #mostrar el listado de gastos
    elif opcion == "3":
        print(resumen_gastos(gastos)) #mostrar el resumen de gastos
    elif opcion == "4":
       exit_program() #salir del programa      