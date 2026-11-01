# 06 · Patrones algorítmicos

[Índice del tema](../README.md) · [Anterior](05_for.md)

**Ejercicios relacionados:** 26–30. Notas, primos, ventas, extremos y números perfectos.

## 1. Reconocer qué necesitas recordar

Un patrón es una forma de resolver una necesidad que se repite en distintos ejercicios.

| Necesidad | Variable habitual | Valor inicial |
|---|---|---|
| ¿Cuántos cumplen una condición? | Contador | 0 |
| ¿Cuánto suman? | Acumulador | 0 |
| ¿Cuál es su producto? | Acumulador de producto | 1 |
| ¿Ha ocurrido algo? | Indicador o flag | False |
| ¿Todos cumplen una propiedad? | Indicador | True, hasta hallar una excepción |
| ¿Cuál es el mayor o menor? | Máximo o mínimo | Primer dato válido |

Antes de programar, escribe qué significa cada variable. Una variable llamada `total` resulta ambigua si no sabes si cuenta personas o suma importes.

## 2. Contador, acumulador e indicador juntos

```python
importes = [20, 75, 90, 15]
contador = 0
suma = 0
hay_importe_alto = False

for importe in importes:
    if importe > 50:
        contador += 1
        suma += importe
        hay_importe_alto = True

print(contador)        # 2
print(suma)            # 165
print(hay_importe_alto) # True
```

El contador suma 1 por coincidencia. El acumulador suma el dato. El indicador recuerda que hubo al menos una coincidencia y permanece verdadero.

No lo vuelvas a poner a False cuando un dato posterior no cumpla la condición: perderías la información anterior.

## 3. Media: elegir bien el denominador

```python
notas = [4, 8, 6]
suma_notas = 0
aprobados = 0

for nota in notas:
    suma_notas += nota
    if nota >= 5:
        aprobados += 1

media_grupo = suma_notas / len(notas)
print(aprobados)              # 2
print(f"{media_grupo:.2f}")    # 6.00
```

La media del grupo divide la suma de **todas las notas** entre el número de notas. Dividir entre los aprobados mezclaría dos grupos distintos.

Para calcular solo la media de los aprobados, necesitas sumar únicamente sus notas y dividir entre su cantidad, siempre que esta sea mayor que 0.

Si lees cinco notas con validación, una entrada fuera de rango no debe consumir una plaza de alumno: vuelve a pedirla antes de contabilizarla.

## 4. Primo: buscar una excepción

Un entero mayor que 1 es primo si no tiene divisores enteros distintos de 1 y de sí mismo.

Planteamiento:

1. Validar que el número sea mayor que 1.
2. Suponer que es primo.
3. Buscar un divisor entre 2 y el número anterior.
4. Si aparece, cambiar el indicador y terminar la búsqueda.

```python
numero = 9
es_primo = numero > 1

for divisor in range(2, numero):
    if numero % divisor == 0:
        es_primo = False
        break

print(es_primo)  # False
```

El caso 2 es importante: el rango está vacío y la suposición inicial permanece verdadera. 0, 1 y los negativos no son primos.

Una vez comprendida la búsqueda básica, puedes limitarla a divisores cuyo cuadrado no supere el número: los divisores aparecen por parejas. Esto reduce el trabajo, pero no cambia la idea del indicador.

## 5. Filtrar ventas y comprobar un objetivo

Distingue qué conjunto pide el enunciado:

- Cantidad de ventas destacadas.
- Suma de las ventas destacadas.
- Suma de todas las ventas, si el objetivo se refiere al total global.

Si "objetivo global" no aclara a qué suma se refiere, identifica el criterio antes de implementarlo. Compara la suma adecuada con el objetivo una vez terminado el recorrido.

No basta con calcular un resultado si el enunciado también pide mostrarlo: revisa que la salida incluya contador, importe y estado.

## 6. Máximo y mínimo: empezar con un dato real

No inicialices el máximo a 0: fallaría si todos los datos fueran negativos. El mínimo a 0 fallaría si todos fueran positivos.

```python
datos = [-8, -3, -12]
mayor = datos[0]
menor = datos[0]

for numero in datos:
    if numero > mayor:
        mayor = numero
    if numero < menor:
        menor = numero

print(mayor)  # -3
print(menor)  # -12
```

Cuando los datos vienen del teclado, valida que la cantidad sea al menos 1, lee el primer número y úsalo para inicializar ambos extremos. Después procesa los restantes.

Puedes calcular extremos sin guardar todos los datos en una lista.

## 7. Números perfectos: acumular divisores propios

Para un entero positivo, sus divisores propios positivos excluyen el propio número.

Para 8: los divisores propios son 1, 2 y 4. Suman 7, así que 8 no es perfecto.

Planteamiento:

1. Validar que el número sea positivo.
2. Inicializar la suma de divisores a 0.
3. Recorrer candidatos desde 1 hasta el número anterior.
4. Sumar los candidatos que dividan exactamente al número.
5. Comparar la suma final con el número.

El 1 no es perfecto: no tiene divisores propios positivos y su suma es 0. Rechaza 0 antes del cálculo para evitar concluir erróneamente que es perfecto porque una suma vacía también da 0.

## 8. Listas y herramientas que aparecen en tus soluciones

Una lista agrupa valores entre corchetes:

```python
numeros = [4, 7, 2]
numeros.append(9)
print(len(numeros))  # 4
print(sum(numeros))  # 22
print(max(numeros))  # 9
print(min(numeros))  # 2
```

`max([])` y `min([])` producen `ValueError`: necesitan al menos un elemento.

También puedes construir una lista filtrando otra:

```python
numeros = [4, 7, 2, 9]
seleccionados = [n for n in numeros if n > 5]
print(seleccionados)  # [7, 9]
```

Esta expresión se llama comprensión de listas. Equivale a:

```python
numeros = [4, 7, 2, 9]
seleccionados = []

for n in numeros:
    if n > 5:
        seleccionados.append(n)

print(seleccionados)  # [7, 9]
```

Primero practica el recorrido explícito. Si el objetivo del ejercicio es utilizar contadores y acumuladores, resolverlo únicamente con sum(), max() o una comprensión puede ocultar precisamente el patrón que debes practicar.

## 9. Guía de los ejercicios, en orden

| Ejercicio | Variables o patrón | Casos que probar |
|---|---|---|
| 26 · Evaluaciones | Cantidad de notas válidas, suma de todas las notas y contador de aprobados. | Todos suspenden; todos aprueban; una nota inválida. |
| 27 · Primos | Indicador y búsqueda de un divisor. | 1, 2, 9, 17 y un negativo. |
| 28 · Ventas | Filtrado, contador, acumulador e indicador del objetivo. | Ninguna destacada; total igual al objetivo; total superior. |
| 29 · Extremos | Inicializar con el primer dato y comparar el resto. | Un solo dato; todos negativos; valores repetidos; cantidad 0. |
| 30 · Perfectos | Acumular divisores propios y comparar al final. | 1, 6, 8, 28 y 0 como entrada inválida. |

## 10. Comprobación manual

Para contar y sumar los valores mayores que 50:

| Dato | ¿Supera 50? | Contador después | Suma después |
|---|---|---|---|
| 20 | No | 0 | 0 |
| 75 | Sí | 1 | 75 |
| 90 | Sí | 2 | 165 |
| 15 | No | 2 | 165 |

Si tu salida no coincide, identifica en qué fila se desvía el valor. Es más fácil corregir una actualización concreta que revisar todo el programa a la vez.

## Consulta rápida

**Contar:** contador += 1 · **Sumar datos:** total += dato · **Recordar un hallazgo:** flag = True · **Divisibilidad:** numero % divisor == 0 · **Media:** suma / cantidad · **Extremos:** inicializar con el primer dato.

Referencias: [Estructuras de datos](https://docs.python.org/es/3/tutorial/datastructures.html) y [funciones incorporadas](https://docs.python.org/es/3/library/functions.html).
