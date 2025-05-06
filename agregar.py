def agregar_producto(inventario, producto, cantidad):
    if producto in inventario:
        inventario[producto] += cantidad
    else:
        inventario[producto] = cantidad
    print(f"Producto {producto} agregado con cantidad {cantidad}")