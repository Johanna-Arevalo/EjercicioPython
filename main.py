from mostrar import mostrar_inventario
from actualizar import actualizar_inventario
from agregar import agregar_producto
from eliminar import eliminar_producto

# Inventario inicial
inventario = {
    'manzana': 50,
    'naranjas': 30,
    'peras': 20
}

mostrar_inventario(inventario)
actualizar_inventario(inventario, 'peras', 25)
agregar_producto(inventario, 'bananas', 40)
eliminar_producto(inventario, 'naranjas')
mostrar_inventario(inventario)


