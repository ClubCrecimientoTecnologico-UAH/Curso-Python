<div style="text-align: center;">

[◄ Tema anterior: Errores en Python](../Tema4/) 

</div>

---

# FUNCIONES, CONDICIONALES Y BUCLES 🐍
1. [FUNCIONES](#funciones)
  - 1.1 [ANATOMÍA DE UNA FUNCIÓN](#anatomía-de-una-función)
  - 1.2 [DECLARACIÓN Y LLAMADO](#declaración-y-llamado)
  - 1.3 [FUNCIONES CON PARÁMETROS](#funciones-con-parámetros)
  - 1.4 [FUNCIONES QUE RETORNAN VALORES](#funciones-que-retornan-valores)
  - 1.5 [FUNCIONES SIN RETORNO](#funciones-sin-retorno)
  - 1.6 [ÁMBITO DE VARIABLES (SCOPE)](#ámbito-de-variables-scope)
  - 1.7 [LO QUE SUCEDE AL LLAMAR UNA FUNCIÓN](#lo-que-sucede-al-llamar-una-función)
  - 1.8 [FUNCIONES INTEGRADAS Y FUNCIONES DE LA COMUNIDAD](#funciones-integradas-y-funciones-de-la-comunidad)
2. [CONDICIONALES](#condicionales)
  - 2.1 [SINTAXIS BÁSICA](#sintaxis-básica)
  - 2.2 [TIPOS DE CONDICIONALES](#tipos-de-condicionales)
3. [BUCLES](#bucles)
  - 3.1 [BUCLE `WHILE`](#bucle-while)
  - 3.2 [BUCLE `FOR`](#bucle-for)
  - 3.3 [CCONTROL DE BUCLES](#ccontrol-de-bucles)
  - 3.4 [BUCLES ANIDADOS](#bucles-anidados)

---

# FUNCIONES
A lo largo de esta guía hemos mencionado repetidamente el término "función", pero ahora es momento de profundizar en este concepto fundamental de la programación. Las funciones son uno de los bloques de construcción más importantes en Python y en la programación en general.

En programación, una función es un bloque de código organizado y reutilizable que realiza una acción específica. Podemos imaginar una función como una máquina especializada que:
1. Recibe ciertos inputs (entradas)
2. Realiza operaciones con ellos
3. Produce un output (salida) o efecto

La característica principal de una función es que solo se ejecuta cuando es explícitamente llamada, no cuando es definida. Esto permite:
- Reutilizar código sin repetirlo
- Organizar mejor nuestros programas
- Dividir problemas complejos en partes más simples
- Facilitar el mantenimiento del código

## ANATOMÍA DE UNA FUNCIÓN
Una función en Python se compone de varios elementos esenciales:

```PYTHON
def nombre_funcion(parámetros):
    """Docstring (Comentario descriptivo)"""
    # Cuerpo de la función
    return valor
```

| Elemento | Ejemplo | Descripción | ¿Obligatorio? |
| -------- | ------- | ----------- | -------------- |
| `def` | def calcular | Marca el inicio de la función | Sí |
| `Nombre` | area_circulo | Identificador | Sí |
| `Parámetros` | (radio) | Variables de entrada | No (pueden ir vacíos) |
| `Cuerpo` | return 3.14*radio**2 | Lógica principal | Sí (puede estar vacío) |
| `return` | return resultado | Valor de salida | No (default=None) |

## DECLARACIÓN Y LLAMADO
Las funciones se declaran con la sintaxis `def nombreFuncion(parametro)` y es llamado con el mismo nombre y la misma cantidad de parámetros definidos.

```PYTHON
# Declaración de la función
def mostrar_bienvenida():
    print("¡Bienvenido al sistema!")
    print("Por favor ingrese sus credenciales")
    print("Versión 1.0")

# Llamado a la función
mostrar_bienvenida()
```

En este caso:
- La función `mostrar_bienvenida` no recibe parámetros
- No devuelve ningún valor (solo muestra mensajes)
- Se ejecuta cuando la llamamos con `mostrar_bienvenida()`

## FUNCIONES CON PARÁMETROS
Las funciones pueden recibir datos externos a través de parámetros:

```PYTHON
def calcular_area_rectangulo(base, altura):
    """Calcula el área de un rectángulo"""
    area = base * altura
    return area

# Llamamos la función con argumentos concretos
area1 = calcular_area_rectangulo(5, 3)
area2 = calcular_area_rectangulo(7.5, 4.2)
```

Aquí:
- `base` y `altura` son parámetros formales
- Los valores `5, 3` y `7.5, 4.2` son argumentos reales
- La función devuelve un resultado que podemos almacenar en variables

## FUNCIONES QUE RETORNAN VALORES
El `return` significa que la función retorna un valor tras ejecutarse, esto es importante para definir funciones que tienen como objetivo devolver un resultado.

```PYTHON
def convertir_a_dolares(monto, tasa_cambio):
    """Convierte un monto a dólares"""
    dolares = monto / tasa_cambio
    return round(dolares, 2)  # Redondea a 2 decimales

monto_dolares = convertir_a_dolares(100000, 3875.50)
print(f"Equivale a ${monto_dolares} USD")
```

Así mismo, una función puede tener multiples `return`, pero solo ejecutará uno, pues este representa el final de la función y no sigue ejecutando lo demás.

```PYTHON
def divideNumero(numero1, numero2):
    if numero2 == 0:
        return 0 # Si el segundo parametro es 0 termina la función antes retornando 0

    resultado = numero1 / numero2

    return resultado
```

Otras características importantes:
- Si no hay `return`, la función devuelve `None` automáticamente
- Podemos devolver múltiples valores usando tuplas: `return x, y, z`

## FUNCIONES SIN RETORNO
No todas las funciones necesitan devolver valores. Algunas realizan acciones sin producir un resultado directo:

```PYTHON
def mostrar_menu_principal():
    """Muestra el menú de opciones"""
    print("\n" + "="*50)
    print(" MENÚ PRINCIPAL ".center(50, "~"))
    print("1. Ingresar datos")
    print("2. Procesar información")
    print("3. Generar reporte")
    print("4. Salir")
    print("="*50 + "\n")

# Llamamos la función por sus efectos
mostrar_menu_principal()
```

Estas funciones: 
- Se usan por sus efectos secundarios (mostrar algo, guardar datos, etc.)
- Son útiles para organizar código aunque no devuelvan valores
- Pueden modificar variables globales (aunque esto no es recomendable)

## ÁMBITO DE VARIABLES (SCOPE)
Este concepto se refiere al *alcance* que tiene una variable. Es decir, las variables que son definidas dentro de una función **solo existe durante la ejecución de la función** y solo puede ser accedido durante este, de otro modo python marcará un error diciendo que la variable no fue definida. Es por esto que, las funciones retornan valores, para que no se pierdan al terminar esta misma.

Por otro lado, las variables que son *declarados fuera de las funciones* pueden ser accedidas en cualquier momento y dentro de cualquier función, es por ello que se les llama **variables globales**.

```PYTHON
def calcular_potencia(base, exponente):
    resultado = base ** exponente  # Variable local
    return resultado

numero = 5  # Variable global
potencia = calcular_potencia(numero, 3)
print(resultado)  # Error! resultado no existe fuera de la función
```

Es decir:
- Las variables dentro de una función son locales (solo existen allí)
- Las variables fuera de funciones son globales
- Podemos acceder a variables globales dentro de funciones, pero no modificarlas directamente
  
## LO QUE SUCEDE AL LLAMAR UNA FUNCIÓN
Cuando invocas una función, Python ejecuta un proceso riguroso detrás de escena. Imagina que es como un viaje espacial controlado por computadora:
1. **Fase de Preparación (Chequeos Previos)**
    - *Verificación de Existencia:* Python busca en su "directorio de funciones" (namespace actual).

    ```PYTHON
    # Ejemplo de error común
    funcion_inexistente()  # NameError: name 'funcion_inexistente' is not defined
    ```

    - *Validación de Argumentos:* Compara los parámetros definidos vs. los argumentos proporcionados.

    ```PYTHON
    def saludar(nombre, edad):
        print(f"Hola {nombre}, tienes {edad} años")
    
    saludar("Ana")  # TypeError: missing 1 required positional argument: 'edad'
    ```

2. **Fase de Ejecución (Salto al Código)**
    - *Python apila la llamada (call stack) y crea un nuevo marco de ejecución (frame).*
    - *Los argumentos se asignan a los parámetros como variables locales.*

    ```PYTHON
    # Ejemplo con seguimiento de variables
    def duplicar(numero):
        resultado = numero * 2  # 'numero' existe solo aquí
        return resultado
    
    x = 5
    y = duplicar(x)  # 1. x se copia a 'numero'
                     # 2. Se ejecuta la función
                     # 3. 'resultado' se devuelve y destruye
    ```

3. **Fase de Finalización (Retorno)**
    - El `return` actúa como un "botón de regreso":
      - Termina la función inmediatamente. 
      - Destruye todas las variables locales.
      - Transfiere el control al punto de llamada.
    -  Si no hay `return`, Python devuelve `None` automáticamente.


## FUNCIONES INTEGRADAS Y FUNCIONES DE LA COMUNIDAD
Las funciones no son solamente las que definimos en el código, estas también se encuentran en el propio Python. Por ejemplo, los ya utilizados `print()` e `input()` los cuales son funciones propias de Python las cuales llamamos para que se ejecuten, lo mismo con todas las `funciones integradas` que fueron mencionados en el [tema 3](../Tema3/).

Del mismo modo, la propia comunidad de Python se encarga de ofrecer funciones útiles para todo tipo de desarrollos para facilitar ciertos trabajos. Sin embargo, este punto se abarcará en detalle más adelante en esta guia.

---

# CONDICIONALES
Los condicionales son estructuras fundamentales que permiten a nuestros programas tomar decisiones. Imagínalos como bifurcaciones en el camino: según ciertas condiciones, el programa elegirá un recorrido u otro.

En programación, un condicional es un bloque de código que se ejecuta solo si se cumple una condición específica. Son el equivalente digital a:

> "SI [condición] ENTONCES [acción]
> SI NO, [acción alternativa]"

En Python, esto se traduce principalmente en tres estructuras:
1. `if` (si)
2. `elif` (si no, si)
3. `else` (si no)

## SINTAXIS BÁSICA
La estructura fundamental usa la palabra reservada `if` seguida de una condición y dos puntos (`:`):

```PYTHON
edad = 18

if edad >= 18:
    print("Eres mayor de edad")
```

## TIPOS DE CONDICIONALES

1. **Condicional Simple (`if`):** Ejecuta un bloque solo si se cumple la condición:
```PYTHON
saldo = 1000
retiro = 500

if retiro <= saldo:
    saldo -= retiro
    print(f"Retiro exitoso. Saldo restante: ${saldo}")
```

2. **Condicional Binario (`if-else`):** Añade una alternativa cuando la condición no se cumple:

```PYTHON
if edad >= 18:
    print("Puedes ingresar")
else:
    print("Acceso denegado")
```

3. **Condicional Múltiple (`if-elif-else`)**: Evalúa varias condiciones en secuencia:

```PYTHON
def evaluar_edad(edad):
    """Clasifica edad con returns tempranos"""
    if edad < 0:
        return "Edad inválida"
    if edad < 13:
        return "Niño"
    if edad < 18:
        return "Adolescente"
    return "Adulto"  # Default para >=18
```

4. **Condicionales anidadas:** Podemos colocar condicionales dentro de otros condicionales para crear lógicas complejas:

```PYTHON
if conexion_activa:
    if usuario_autenticado:
        print("Bienvenido al sistema")
    else:
        print("Por favor inicia sesión")
else:
    print("Error de conexión")
```

5. **Condicionales en una línea:** Python permite escribir condicionales simples en una sola línea:

```PYTHON
def getSaldo(saldo):
    # Forma tradicional
    if saldo > 0:
        return "Activo"
    else:
        return "Inactivo"

def getSaldo(saldo):
    # Equivalente en una línea
    return "Activo" if saldo > 0 else "Inactivo"
```

---

# BUCLES
Los bucles son estructuras de control que nos permiten repetir un bloque de código múltiples veces. Son fundamentales para automatizar tareas repetitivas y procesar colecciones de datos.

Python ofrece dos tipos principales de bucles:
1. `while`: Repite mientras se cumpla una condición
2. `for`: Itera sobre una secuencia (listas, strings, rangos, etc.)

## BUCLE `WHILE`
Estructura básica:
La estructura fundamental usa la palabra reservada `while` seguida de una condición y dos puntos (`:`):

```PYTHON
contador = 0
while contador < 5:
    print(f"Contador: {contador}")
    contador += 1  # Incremento esencial para evitar bucle infinito
```

Salida:

```
Contador: 0
Contador: 1
Contador: 2
Contador: 3
Contador: 4
```

Casos de uso comunes:
- Cuando no sabemos cuántas iteraciones necesitamos
- Validación de entrada de usuario
- Procesamiento hasta alcanzar una condición

## BUCLE `FOR`
La estructura fundamental usa la palabra reservada `for` seguida de un elemento a iterar y la secuencia de iteración seguido de (`:`):

```PYTHON
frutas = ["manzana", "banana", "naranja"]
for fruta in frutas:
    print(f"Me gusta la {fruta}")
```

Salida:

```
Me gusta la manzana
Me gusta la banana
Me gusta la naranja
```

**Función `range()`:** Genera secuencias numéricas para controlar las iteraciones:

```PYTHON
for i in range(3):  # 0, 1, 2
    print(f"Iteración {i}")
```

Salida:

```
Iteración 0
Iteración 1
Iteración 2
```

**Range avanzado:**

```PYTHON
for num in range(5, 10):    # 5 al 9
for num in range(0, 10, 2): # 0, 2, 4, 6, 8
```

##  CCONTROL DE BUCLES
Python ofrece palabras clave para modificar el flujo de los bucles:
1. `break:` Detiene completamente el bucle

```PYTHON
for num in range(10):
    if num == 5:
        break
    print(num)  # Solo imprime 0-4
```

2. `continue:` Salta a la siguiente iteración

```PYTHON
for num in range(10):
    if num % 2 == 0:
        continue
    print(num)  # Solo imprime impares
```

3. `else:` Se ejecuta cuando el bucle termina normalmente (sin break)

```PYTHON
for num in range(3):
    print(num)
else:
    print("Bucle completado")
```

## BUCLES ANIDADOS
Podemos colocar bucles dentro de otros bucles:

```PYTHON
for i in range(3):      # Filas
    for j in range(3):  # Columnas
        print(f"({i},{j})", end=" ")
    print()  # Nueva línea
```

Salida:

```
(0,0) (0,1) (0,2) 
(1,0) (1,1) (1,2) 
(2,0) (2,1) (2,2)
```

---

Antes de avanzar al siguiente tema, te recomendamos que te detengas a resolver los ejercicios de la carpeta [ejercicio](./ejercicio/).

---

<div style="text-align: center;">

[◄ Tema anterior: Errores en Python](../Tema4/) | [Siguiente tema: Programando en Python ►](../Tema5/)

</div>