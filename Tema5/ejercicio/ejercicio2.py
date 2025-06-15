"""
EJERCICIO INTEGRADOR: SISTEMA DE CAJA REGISTRADORA 🛒

Combina funciones, condicionales y bucles para crear un sistema simple de caja registradora.
¡Cuidado! Hay un bucle infinito que debes identificar y corregir.

Instrucciones:
1. Analiza el código y encuentra el bucle infinito
2. Corrige el error manteniendo la funcionalidad
3. Completa las funciones marcadas como TODO
4. El programa debe:
   - Mostrar un menú de opciones
   - Permitir agregar productos
   - Calcular el total
   - Salir correctamente
"""

# Lista global para almacenar los productos
productos = []

def mostrar_menu():
    """Muestra el menú principal"""
    print("\n" + "=" * 40)
    print(" CAJA REGISTRADORA ".center(40, "~"))
    print("1. Agregar producto")
    print("2. Ver productos")
    print("3. Calcular total")
    print("4. Salir")
    print("=" * 40 + "\n")

def agregar_producto():
    """Agrega un producto a la lista"""
    # TODO: Pedir nombre y precio del producto
    # TODO: Validar que el precio sea número positivo
    # TODO: Agregar a la lista como diccionario {'nombre': nombre, 'precio': precio}
    pass

def ver_productos():
    """Muestra todos los productos agregados"""
    # TODO: Mostrar "No hay productos" si la lista está vacía
    # TODO: Mostrar lista numerada de productos con formato
    pass

def calcular_total():
    """Calcula el total a pagar"""
    # TODO: Sumar todos los precios
    # TODO: Mostrar total con IVA (16%)
    pass

def main():
    """Función principal del programa"""
    while True:  # ¡Este bucle es infinito! ¿Cómo podemos arreglarlo?
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            agregar_producto()
        elif opcion == "2":
            ver_productos()
        elif opcion == "3":
            calcular_total()
        elif opcion == "4":
            print("¡Gracias por usar el sistema!")
            # TODO: Agregar código para salir del bucle
        else:
            print("Opción inválida. Intente nuevamente.")


print("¡Bienvenido al sistema de caja registradora!")
main()