from mostrar import mostrar_inventario
from actualizar import actualizar_inventario

# Inventario inicial 
inventario = {
    'manzana' : 50,
    'naranjas' : 30,
    'peras' : 20
}

mostrar_inventario(inventario)
actualizar_inventario(inventario, 'peras',25)
mostrar_inventario(inventario)



