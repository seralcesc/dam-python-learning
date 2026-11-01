# 04 · Bucles while y validación

[Índice del tema](../README.md) · [Anterior](03_condicionales.md) · [Siguiente: for](05_for.md)

**Ejercicios relacionados:** 16–20. Contraseña, suma hasta cero, cuenta atrás, menú y Collatz.

## 1. Cuándo elegir while

Utiliza `while` cuando la repetición depende de una condición: hasta que la entrada sea válida, hasta elegir salir o mientras queden intentos.

```python
pendientes = 3

while pendientes > 0:
    print(f"Quedan {pendientes}")
    pendientes -= 1

print("Terminado")
```

Salida: Quedan 3, Quedan 2, Quedan 1 y Terminado, en líneas distintas.

La condición se comprueba **antes de cada vuelta**. Si es falsa al principio, el cuerpo no se ejecuta.

En Python no existe una sentencia `do-while`. Para pedir un dato al menos una vez puedes leerlo antes del bucle o usar `while True` con una salida explícita.

## 2. Las tres piezas de un bucle

| Pieza | En el ejemplo | Si falta… |
|---|---|---|
| Inicialización | pendientes = 3 | Puedes usar una variable no definida |
| Condición | pendientes > 0 | No defines cuándo debe continuar |
| Actualización | pendientes -= 1 | Puede repetirse indefinidamente |

La actualización también puede ser leer un nuevo dato. Lo necesario es que algo permita que la condición llegue a ser falsa o que se ejecute un `break`.

## 3. Repetir una entrada hasta que sea válida

```python
cantidad = int(input("Cantidad positiva: "))

while cantidad <= 0:
    print("Debe ser mayor que cero.")
    cantidad = int(input("Cantidad positiva: "))

print(f"Cantidad aceptada: {cantidad}")
```

El primer dato permite evaluar la condición. Dentro del bucle se vuelve a leer: sin esa lectura, una entrada inválida produciría un bucle infinito.

Esto valida el **rango de un entero**. Si escribes letras, `int()` produce `ValueError`; gestionar ese error requiere `try/except`, que se estudiará aparte.

## 4. while True y break

```python
while True:
    respuesta = input("Escribe fin para terminar: ").strip().lower()
    if respuesta == "fin":
        break
    print(f"Has escrito: {respuesta}")

print("Fuera del bucle")
```

`True` mantiene abierta la repetición. `break` termina el bucle más cercano y continúa con la instrucción posterior a él.

No confundas `break` con `continue`: este último salta el resto de la vuelta y vuelve a comprobar la condición. Puede ser útil, pero si omites con él una actualización necesaria, puedes crear una repetición infinita.

## 5. Centinela: un valor indica el final

Un centinela es una entrada especial que marca el fin de los datos.

```python
total = 0

while True:
    importe = int(input("Importe (-1 para terminar): "))
    if importe == -1:
        break
    total += importe

print(f"Total: {total}")
```

El centinela -1 no se procesa como importe: primero compruebas si hay que salir y después acumulas. El 0 del ejercicio 17 cumple esa misma función.

## 6. Combinar condiciones de continuación

Si repites **mientras no haya acierto y queden intentos**, necesitas `and`:

```python
intentos = 0
acierto = False
clave_correcta = "LUNA"  # Dato ficticio para practicar

while not acierto and intentos < 3:
    clave = input("Clave: ")
    intentos += 1
    acierto = clave == clave_correcta

if acierto:
    print("Acceso permitido")
else:
    print("Sin intentos")
```

Cada lectura consume un intento. La condición se deja de cumplir si aciertas **o** si llegas al límite.

Con `or`, acertar no bastaría para terminar mientras el contador aún fuera menor que 3. Escribe primero la frase "continuar mientras…" para elegir el operador.

## 7. Un menú de consola

```python
opcion = ""

while opcion != "0":
    print("1. Consultar")
    print("0. Salir")
    opcion = input("Opción: ").strip()

    if opcion == "1":
        print("Consulta realizada")
    elif opcion != "0":
        print("Opción no válida")
```

La lectura debe repetirse dentro del bucle. Mantener la opción como texto permite rechazar entradas como "hola" sin intentar convertirlas a entero.

## 8. Guía de los ejercicios, en orden

| Ejercicio | Qué controlar |
|---|---|
| 16 · Contraseña | Dos motivos de salida: acierto o agotamiento de tres intentos. Evitar un cuarto intento. |
| 17 · Suma | Inicializar el total a cero y comprobar el centinela antes de procesarlo. |
| 18 · Cuenta atrás | Validar el inicio y disminuir una unidad en cada vuelta; decidir si 0 debe mostrarse. |
| 19 · Menú | Mostrar opciones, leer y ejecutar dentro de la repetición. La opción de salir debe coincidir con el enunciado. |
| 20 · Collatz | Admitir solo un entero positivo, distinguir par/impar y actualizar el número en ambas ramas. Usar // en el paso de división para conservar enteros. |

Para Collatz, si introduces 1 no hace falta transformar el número. Si introduces 0 sin validación, dividirlo por 2 lo deja en 0 y no alcanzará 1. El enunciado presupone la llegada a 1 para los valores de práctica; no existe una demostración general de la conjetura para todos los enteros positivos.

## 9. Seguir el programa con una tabla

Para la cuenta atrás de tres pasos:

| Comprobación | pendientes | ¿pendientes > 0? | Acción |
|---|---|---|---|
| 1 | 3 | True | Mostrar 3 y guardar 2 |
| 2 | 2 | True | Mostrar 2 y guardar 1 |
| 3 | 1 | True | Mostrar 1 y guardar 0 |
| 4 | 0 | False | Salir |

Si no entiendes por qué repite, anota los valores antes y después de cada vuelta.

## Consulta rápida

**Repetir según una condición:** while · **Actualizar:** += o -= · **Salir inmediatamente:** break · **Fin de datos:** centinela · **Antes de probar:** identificar qué cambia en cada vuelta.

Referencia: [Introducción: primeros pasos y while](https://docs.python.org/es/3/tutorial/introduction.html#first-steps-towards-programming).
