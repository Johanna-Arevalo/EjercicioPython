## Función actualizar inventario##
def actualizar_inventario(Inventario, producto, cantidad):
    if producto in Inventario:
        Inventario[producto] = cantidad
        print(f"stok de '{producto}' actualizar a {cantidad}")
    else:
        print(f"Error: El producto '{producto}' no existe en el inventario.")