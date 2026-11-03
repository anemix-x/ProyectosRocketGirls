menu = { #diccionario con productos
    "Sushi": 7000,
    "Ramen": 6000,
    "Gyoza": 4500,
    "Tempura": 8000,
    "Yakitori": 4000,
    "Udon": 6000
}
saludo = input("Bienvenida al izakaya, ¿Cuál es tu nombre? ") #saludar al usuario y solicitar su nombre
print(f"Hola {saludo}, elija una opcion:") #solicitar que elija una opcion

pedido = [] #comenzar pedido vacio

def mostrar_menu(): #mostrar menu ennumerado, con sus precios en colones y decimales
    print("Este es nuestro menu:")
    for i, (producto, precio) in enumerate(menu.items(), 1):
        print(f"{i}. {producto} : ₡{precio:.2f}")
    
def agregar_pedido(): #agreagar uno de los productos al menu
    mostrar_menu() #mostrar el menu y soliciarlo por nombre
    nombre_producto = input("Ingrese el nombre del producto que desea agregar al pedido: ")
    producto_encontrado = None
    for producto_existente in menu.keys(): #asegurarse de que el producto se agregue sin importar si es mayuscula o minuscula
        if producto_existente.lower() == nombre_producto.lower():
            producto_encontrado = producto_existente
            break
    if producto_encontrado:
        cantidad_final = int(input(f"¿Cuántas unidades de {producto_encontrado} desea? ")) #solicitar la cantidad
        try:
            cantidad = int(cantidad_final) #si la cantidad es mayor a 0 agregarlo
            if cantidad > 0:
                precio_unitario = menu[producto_encontrado]
                precio_total_producto = precio_unitario * cantidad
                pedido.append({
                    "producto": producto_encontrado,
                    "cantidad": cantidad,
                    "precio_total": precio_total_producto
                })
                print(f"Se ha agregado {cantidad} {producto_encontrado} al pedido.") #mostrar el producto y la cantidad
            else:
                print("La cantidad debe ser un número entero mayor a 0.") #mensaje en caso de que sea un numero menor a 0
        except ValueError:
            print("Entrada inválida. Ingrese un numero.") #mensaje en caso de que no sea un numero
    else:
        print("Producto no encontrado en el menu.") #mensaje en caso de que escriba mal el producto o no exista

def mostrar_pedido(): #mostrar el pedido actual
    print("El pedido actual es:")
    if not pedido:
        print("No hay productos en el pedido.") #mensaje si el pedido esta vacio
        return 0
    
    total = 0
    for i, item in enumerate(pedido, 1): #mostrar el pedido con sus productos, cantidades y precios
        print(f"{item['producto']}: {item['cantidad']} = ₡{item['precio_total']}")
        total += item['precio_total']
    print(f"Tu subtotal es: ₡{total:.2f}") #mostrar el subtotal del pedido
    return total

def mostrar_opciones(): #definir el menu de opciones para el usuario
    print("++++++++++++++")
    print("1. Ver el menú con precios")
    print("2. Agregar un producto al pedido")
    print("3. Ver el pedido actual")
    print("4. Finalizar compra o salir")

while True:
    mostrar_opciones()
    opcion = input("Seleccione una opción: ") #mostrar el menu de opciones y solicitar que elija una
    #opciones ennumeradas 
    if opcion == "1":
        mostrar_menu()
    elif opcion == "2":
        agregar_pedido()
    elif opcion == "3":
        mostrar_pedido()
    elif opcion == "4":
        subtotal = mostrar_pedido()
        if subtotal > 0:
            while True:
                propina_input = input("¿Cual porcentaje de propina desea dejar(0 a 100)?: ") #solicitar una propina antes de terminar
                try:
                    porcentaje_propina = float(propina_input)
                    if 0 <= porcentaje_propina <= 100: #revisar que sea un numero valido
                        break
                    else:
                        print("Ingrese un porcentaje valido entre 0 y 100.") #mensaje si el numero no es valido
                except ValueError:
                    print("Entrada invalida. Ingrese un numero.") #mensaje si no es un numero
            monto_propina = subtotal * (porcentaje_propina / 100) #calcular la propina y el total final
            total_final = subtotal + monto_propina

            print("Factura detallada: ") #mostrar la factura con sus elementos
            print(f"Subtotal: ₡{subtotal:.2f}")
            print(f"Propina ({porcentaje_propina}%): ₡{monto_propina:.2f}")
            print(f"Total: ₡{total_final:.2f}")
        else:
            print("No realizo ninguna compra.") #mensaje si no se agregaron productos
        print("Gracias por su visita, vuelva pronto.") #mensaje de despedida
        break
    else:
        print("Opción inválida. Seleccione una opción del 1-4.") #mensaje en caso de no seleccionar una opcion valida del menu de opciones