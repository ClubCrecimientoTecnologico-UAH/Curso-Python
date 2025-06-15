"""
EJERCICIOS PRÁCTICOS - FUNCIONES, CONDICIONALES Y BUCLES 🐍

Instrucciones:
1. Completa cada ejercicio en el espacio designado
2. Ejecuta el archivo para verificar tus respuestas
3. Las soluciones se encuentran al final del archivo
"""

# ====================
# EJERCICIO 1: Funciones básicas
# ====================
# Crea una función llamada 'saludar' que:
# - Reciba un nombre como parámetro
# - Retorne el string "¡Hola, [nombre]!"
# - Si no se proporciona nombre, que use "Visitante"

def saludar(nombre="Visitante"):
    # Tu código aquí
    pass

# ====================
# EJERCICIO 2: Condicionales
# ====================
# Escribe una función 'clasificar_edad' que:
# - Reciba una edad (número entero)
# - Retorne:
#   * "Niño" si edad < 13
#   * "Adolescente" si 13 <= edad < 18
#   * "Adulto" si 18 <= edad < 65
#   * "Adulto mayor" si edad >= 65
# - Maneje edades negativas con "Edad inválida"

def clasificar_edad(edad):
    # Tu código aquí
    pass

# ====================
# EJERCICIO 3: Bucles while
# ====================
# Completa la función 'contar_vocales' que:
# - Reciba un string
# - Use un bucle while para contar las vocales (a,e,i,o,u)
# - Retorne el total de vocales encontradas
# - Considera mayúsculas y minúsculas

def contar_vocales(texto):
    # Tu código aquí
    pass

# ====================
# EJERCICIO 4: Bucles for
# ====================
# Crea una función 'tabla_multiplicar' que:
# - Reciba un número entero
# - Imprima su tabla de multiplicar del 1 al 10
# - Usa formato: "5 x 3 = 15"

def tabla_multiplicar(numero):
    # Tu código aquí
    pass

# ====================
# EJERCICIO 5: Funciones + Condicionales
# ====================
# Implementa una función 'calculadora' que:
# - Reciba dos números y un operador (+, -, *, /)
# - Retorne el resultado de la operación
# - Maneje división por cero
# - Valide operadores inválidos

def calculadora(num1, num2, operador):
    # Tu código aquí
    pass

# ====================
# EJERCICIO 6: Proyecto integrador
# ====================
# Crea un sistema de login que:
# 1. Pida usuario y contraseña (predefinidos)
# 2. Dé 3 intentos máximo
# 3. Use funciones para:
#    - Validar credenciales
#    - Mostrar mensajes de error/éxito
#    - Controlar intentos restantes

def sistema_login():
    # Credenciales válidas
    USUARIO = "admin"
    CONTRASEÑA = "python123"
    
    # Tu implementación aquí
    pass

# =========================================
# ZONA DE PRUEBAS - NO MODIFICAR
# =========================================
def main():
    print("\n=== Pruebas Ejercicio 1 ===")
    print(saludar("Ana"))  # ¡Hola, Ana!
    print(saludar())       # ¡Hola, Visitante!
    
    print("\n=== Pruebas Ejercicio 2 ===")
    print(clasificar_edad(10))  # Niño
    print(clasificar_edad(70))  # Adulto mayor
    print(clasificar_edad(-5))  # Edad inválida
    
    print("\n=== Pruebas Ejercicio 3 ===")
    print(contar_vocales("Hello World"))  # 3
    print(contar_vocales("PYTHON"))      # 1
    
    print("\n=== Pruebas Ejercicio 4 ===")
    tabla_multiplicar(7)  # Debe imprimir tabla del 7
    
    print("\n=== Pruebas Ejercicio 5 ===")
    print(calculadora(5, 3, "+"))   # 8
    print(calculadora(10, 0, "/"))  # "Error: División por cero"
    
    print("\n=== Pruebas Ejercicio 6 ===")
    sistema_login()  # Probar con credenciales correctas/incorrectas

main()