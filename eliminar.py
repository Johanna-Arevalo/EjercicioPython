def eliminar_producto(inventario, producto):
    if producto in inventario:
        del inventario[producto]
        print(f"producto {producto} eliminado")
    else:
        print(f"Error: El producto {producto} no existe en el inventario")