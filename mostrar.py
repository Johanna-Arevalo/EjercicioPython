## Función mostrar inventario##
def mostrar_inventario(Inventario) :
    print("Inventario actual:")
    for producto, cantidad in Inventario.items():
        print(f"{producto}: {cantidad}")
        print()