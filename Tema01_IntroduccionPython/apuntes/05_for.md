# 05 · Bucles for y rangos

[Índice del tema](../README.md) · [Anterior](04_while.md) · [Siguiente: patrones](06_patrones_algoritmicos.md)

**Ejercicios relacionados:** 21–25. Tablas, pares, vocales, factorial y triángulos.

## 1. Qué hace for en Python

`for` toma sucesivamente los elementos de un objeto que se pueda recorrer, como una cadena, una lista o un rango.

```python
for letra in "sol":
    print(letra)
```

Muestra s, o y l en líneas distintas. La variable `letra` recibe el siguiente carácter automáticamente; no tienes que incrementar un índice.

## 2. range(inicio, fin, paso)

El inicio se incluye y el fin **se excluye**.

| Expresión | Valores recorridos |
|---|---|
| range(4) | 0, 1, 2, 3 |
| range(2, 6) | 2, 3, 4, 5 |
| range(2, 9, 2) | 2, 4, 6, 8 |
| range(4, -1, -1) | 4, 3, 2, 1, 0 |

El inicio por defecto es 0 y el paso por defecto es 1. El paso no puede ser 0.

```python
for numero in range(1, 4):
    print(f"Paso {numero}")
```

Salida: Paso 1, Paso 2 y Paso 3.

Para incluir un límite superior entero con paso positivo, suele utilizarse `limite + 1`. En una cuenta atrás, adapta también el final al sentido del recorrido.

`range(5, 1)` está vacío: con paso positivo no puedes avanzar desde 5 hasta un valor menor que 1.

## 3. Repetir una cantidad fija de veces

```python
for _ in range(3):
    print("Preparado")
```

`_` es una variable convencional para indicar que no necesitas el valor de cada vuelta.

Si necesitas mostrar la posición, utiliza un nombre como `numero_paso` y un rango que empiece en 1.

## 4. Recorrer caracteres y contar coincidencias

```python
texto = "casa"
contador = 0

for letra in texto:
    if letra == "a":
        contador += 1

print(contador)  # 2
```

El contador se inicializa **antes** del bucle. Si lo pusieras dentro, se reiniciaría en cada vuelta.

Para comparar sin distinguir mayúsculas, recorre `texto.lower()`. Para contar vocales puedes comprobar pertenencia con `in`. Decide según el enunciado si también incluirás á, é, í, ó, ú y ü: no aparecen automáticamente al escribir "aeiou".

Si necesitas posiciones:

```python
texto = "sol"
for i in range(len(texto)):
    print(i, texto[i])
```

No sumes 1 a `len(texto)`: el último índice válido ya es `len(texto) - 1`.

## 5. Acumular productos

En una suma, el valor neutro es 0. En un producto, es 1:

```python
producto = 1

for factor in range(2, 5):
    producto *= factor

print(producto)  # 24: 1 * 2 * 3 * 4
```

Si empiezas un producto en 0, todos los pasos seguirán dando 0.

Esto explica el caso 0! = 1: un bucle que no realiza multiplicaciones deja el acumulador en 1.

## 6. Patrones de texto

Repetir una cadena permite construir líneas de distinta longitud:

```python
for fila in range(1, 4):
    print("#" * fila)
```

Salida:

```text
#
##
###
```

Piensa en qué cambia de una fila a otra: el número de símbolos. Antes de usar bucles anidados, comprueba si la repetición de cadenas ya resuelve el patrón.

## 7. for o while

| Necesidad | Elección habitual |
|---|---|
| Procesar los caracteres de un texto | for |
| Leer exactamente cinco datos válidos | for con validación interna, o while con contador |
| Repetir hasta que el usuario salga | while |
| Recorrer los enteros de un intervalo | for con range |
| Transformar un valor hasta cumplir una condición | while |

Ambos pueden resolver muchos problemas; elige el que haga más visible la lógica.

## 8. Guía de los ejercicios, en orden

| Ejercicio | Cómo plantearlo | Caso de comprobación |
|---|---|---|
| 21 · Tabla | Fijar el número y recorrer los multiplicadores 1–10. | Deben aparecer diez líneas. |
| 22 · Pares | Recorrer el intervalo y filtrar con % 2. Después puedes practicar el recorrido de dos en dos. | Límites impares, iguales e invertidos. |
| 23 · Vocales | Recorrer el texto y aumentar un contador si el carácter está en las vocales admitidas. | Mayúsculas, texto vacío y tildes según el criterio elegido. |
| 24 · Factorial | Validar que n no sea negativo; iniciar el producto a 1. | 0! = 1 y 4! = 24. |
| 25 · Triángulo | Recorrer filas desde 1 hasta la altura y generar esa cantidad de símbolos. | Altura 1 y altura inválida. |

Si el límite inferior es mayor que el superior, decide si el programa lo rechaza, intercambia los límites o recorre hacia atrás. No supongas que `range` lo corrige.

## Errores frecuentes y consulta rápida

- No escribas `i++`: en Python se utiliza `i += 1`, aunque un for normal ya avanza automáticamente.
- Modificar `i` dentro del cuerpo no modifica el siguiente valor que entregará range().
- No reinicies el contador o acumulador dentro del bucle.
- Comprueba por separado la primera y la última vuelta.

**Contar vueltas:** range(n) · **Intervalo inclusivo creciente:** range(a, b + 1) · **Recorrer texto:** for caracter in texto · **Producto:** iniciar a 1.

Referencia: [for y range en la documentación oficial](https://docs.python.org/es/3/tutorial/controlflow.html#for-statements).
