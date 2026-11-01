# 03 · Condicionales

[Índice del tema](../README.md) · [Anterior](02_cadenas.md) · [Siguiente: while](04_while.md)

**Ejercicios relacionados:** 11–15. Clasificación, acceso, notas, tarifas y años bisiestos.

## 1. Una condición decide qué código se ejecuta

Una comparación produce un booleano: `True` o `False`.

| Operador | Significado |
|---|---|
| `==` | Igual |
| `!=` | Distinto |
| `<`, `>` | Menor, mayor |
| `<=`, `>=` | Menor o igual, mayor o igual |

```python
temperatura = 28
hace_calor = temperatura >= 25
print(hace_calor)  # True

if hace_calor:
    print("Lleva agua.")
```

`if hace_calor:` comprueba si la condición es verdadera. No necesitas añadir `== True`.

## 2. if, elif y else

```python
temperatura = 18

if temperatura < 10:
    mensaje = "Frío"
elif temperatura < 25:
    mensaje = "Templado"
else:
    mensaje = "Calor"

print(mensaje)  # Templado
```

Python evalúa las condiciones en orden. En una cadena `if/elif/else` solo se ejecuta la primera rama que corresponda.

Cada cabecera termina con dos puntos. La sangría indica qué instrucciones pertenecen al bloque; utiliza cuatro espacios por nivel.

## 3. Condiciones alternativas e independientes

Para categorías excluyentes, utiliza `elif`. Para preguntas que pueden cumplirse simultáneamente, utiliza varios `if`.

```python
numero = 8

if numero > 0:
    print("Positivo")

if numero % 2 == 0:
    print("Par")
```

Un número puede ser positivo y par a la vez. Si la segunda pregunta fuera un `elif`, se omitiría al haberse cumplido la primera.

## 4. and, or y not

| Expresión con booleanos | Es verdadera cuando… |
|---|---|
| `a and b` | Ambas condiciones son verdaderas |
| `a or b` | Al menos una es verdadera |
| `not a` | a es falsa |

```python
edad = 20
rol = "profesor"
autorizado = edad >= 18 and (rol == "admin" or rol == "profesor")
print(autorizado)  # True
```

Los paréntesis aclaran qué requisitos van juntos. También puedes expresar los roles con:

```python
rol_valido = rol in ("admin", "profesor")
```

No escribas `rol == "admin" or "profesor"`. El segundo operando es una cadena no vacía, que se considera verdadera; necesitas otra comparación o una prueba de pertenencia.

Al evaluar `and`, Python no evalúa la segunda parte si la primera es falsa. Con `or`, no la evalúa si la primera es verdadera. Esto se llama cortocircuito.

## 5. Validar un intervalo

Python permite comparaciones encadenadas:

```python
nota = 7.5
es_valida = 0 <= nota <= 10
fuera_de_rango = nota < 0 or nota > 10
```

Para estar dentro del intervalo deben cumplirse ambos límites. Para estar fuera basta con incumplir uno.

Valida primero y clasifica después. Si una nota es 15, no debería clasificarse como sobresaliente.

## 6. El orden de las ramas importa

Si una regla es más específica, debe evaluarse antes de otra que la incluya.

Ejemplo de una tarifa ficticia:

```python
edad = 7

if edad < 8:
    precio = 0
elif edad < 16:
    precio = 4
else:
    precio = 9

print(precio)  # 0
```

Si la primera condición fuera `edad < 16`, los menores de 8 entrarían en ella antes de alcanzar la gratuidad.

En intervalos ordenados puedes evitar repetir límites: al llegar al `elif`, sabes que las condiciones anteriores han sido falsas.

## 7. Divisibilidad y bisiestos

`numero % divisor == 0` comprueba divisibilidad. Para la paridad, utiliza divisor 2.

Un año es bisiesto si es divisible por 400, o si es divisible por 4 pero no por 100:

```python
anio = 1900
es_bisiesto = anio % 400 == 0 or (anio % 4 == 0 and anio % 100 != 0)
print(es_bisiesto)  # False
```

También puedes resolverlo con ramas: primero múltiplos de 400, después de 100, después de 4 y finalmente el resto. Comprueba 2000, 1900, 2024 y 2023 para cubrir los cuatro casos.

## 8. Guía de los ejercicios, en orden

| Ejercicio | Cómo razonar |
|---|---|
| 11 · Clasificador | Separar signo y paridad: son dos clasificaciones independientes. El cero también es par. |
| 12 · Acceso | Debe cumplirse la edad mínima y pertenecer a uno de los roles permitidos. Normalizar el rol antes de compararlo. |
| 13 · Calificaciones | Rechazar notas fuera de 0–10 y después recorrer los intervalos en orden. Probar sus límites. |
| 14 · Descuento | Evaluar primero la gratuidad; después la condición conjunta de descuento. Guardar el precio y mostrarlo al final. Respetar si el límite dice "mayores de" o "a partir de". |
| 15 · Bisiestos | Separar la regla general de las excepciones de los siglos. Probar casos que distingan ambas. |

## 9. Errores frecuentes

- `=` asigna; `==` compara.
- `else` no lleva condición. Si hay otra condición, usa `elif`.
- Una sangría incorrecta puede hacer que una salida solo aparezca en la última rama.
- `bool("False")` es True: cualquier cadena no vacía es verdadera. Para s/n, compara el texto normalizado con `"s"`.
- Si un resultado debe mostrarse en todos los casos, colócalo fuera de las ramas después de asignarlo en todas ellas.

## Consulta rápida

**Elegir una categoría:** if/elif/else · **Comprobar varias propiedades:** if independientes · **Exigir todo:** and · **Aceptar alternativas:** or · **Negar:** not.

Referencia: [Control de flujo](https://docs.python.org/es/3/tutorial/controlflow.html#if-statements).
