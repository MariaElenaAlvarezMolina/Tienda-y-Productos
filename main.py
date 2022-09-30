from Tienda import Tienda
from Producto import Producto

lampara = Producto("Lámpara", 10000, "Hogar", 111)
atun = Producto("Atún", 590, "Comida", 222)
zapato = Producto("Zapatos", 30000, "Vestimenta", 333)
blusa = Producto("Blusa", 5000, "Vestimenta", 444)
tenedor = Producto("Tenedor", 300, "Cocina", 555)

shoppingcenter = Tienda()

#Agregar productos a la lista de productos
shoppingcenter.agregar_producto(lampara).agregar_producto(atun).agregar_producto(zapato).agregar_producto(blusa).agregar_producto(tenedor).imprime_lista()

#Eliminación del producto "Blusa" con id = 444
shoppingcenter.vender_producto(444).imprime_lista()

#Bonus
#Liquidación de productos de la categoría "Vestimenta"
zapato.print_info()
blusa.print_info()
# Hace la liquidación e imprime la info nueva
shoppingcenter.hacer_liquidacion("Vestimenta", 0.05)

#Bonus
#Aplicación de inflación
shoppingcenter.inflacion(0.03)