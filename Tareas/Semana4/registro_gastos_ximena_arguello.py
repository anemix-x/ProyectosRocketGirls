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
