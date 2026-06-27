# Punto de entrada del programa

from modelos.producto import Producto
from modelos.cliente import Cliente
from servicios.restaurante import Restaurante

# Crear instancia del restaurante
restaurante = Restaurante()

# Crear Productos
producto1 = Producto("Fritada", 4.99, 10, True)
producto2 = Producto("Coca cola", 3.25, 2, True)

# Crear clientes
cliente1 = Cliente("ELisabeht Mora", 30, "eli@gmail.com", True)
cliente2 = Cliente("Juan Lopez", 22, "juan@gmail.com", True)

# Agregar productos al restaurante 
restaurante.agregar_producto(producto1)
restaurante.agregar_producto(producto2)

# Agregar clientes al restaurante 
restaurante.agregar_cliente(cliente1)
restaurante.agregar_cliente(cliente2)

# Mostrar información registrada
restaurante.mostrar_producto()
restaurante.mostrar_clientes()