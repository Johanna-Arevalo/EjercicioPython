Inventario = {
    'manzana' : 50,
    'naranjas' : 30,
    'peras' : 20
}

## Función mostrar inventario##
def mostrar_inventario(Inventario) :
    print("Inventario actual:")
    for producto, cantidad in Inventario.items():
        print(f"{producto}: {cantidad}")
        print()
        
## Función actualizar inventario##
def actualizar_inventario(Inventario, producto, cantidad):
    if producto in Inventario:
        Inventario[producto] = cantidad
        print(f"stok de '{producto}' actualizar a {cantidad}")
    else:
        print(f"Error: El producto '{producto}' no existe en el inventario.")
        
              
        