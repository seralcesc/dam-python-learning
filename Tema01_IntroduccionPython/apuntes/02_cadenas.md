# 02 · Cadenas de texto

[Índice del tema](../README.md) · [Anterior](01_fundamentos.md) · [Siguiente: condicionales](03_condicionales.md)

**Ejercicios relacionados:** 06–10. Inversión, formato de nombres, correo, búsqueda y enmascaramiento.

## 1. Qué es una cadena

Un `str` es una secuencia de caracteres. Sus posiciones empiezan en **0**.

| Carácter de "Python" | P | y | t | h | o | n |
|---|---|---|---|---|---|---|
| Índice | 0 | 1 | 2 | 3 | 4 | 5 |
| Índice negativo | -6 | -5 | -4 | -3 | -2 | -1 |

```python
texto = "Python"
print(texto[0])   # P
print(texto[-1])  # n
print(len(texto)) # 6
```

La última posición positiva es `len(texto) - 1`. Acceder con `texto[6]` provoca `IndexError`. Si el texto está vacío, no existe ni el primer ni el último carácter.

Las cadenas son **inmutables**: no puedes asignar `texto[0] = "J"`. Los métodos de transformación devuelven otro texto.

## 2. Slicing: extraer partes

Sintaxis: `texto[inicio:fin:paso]`. El inicio se incluye y el fin se excluye.

```python
texto = "Python"
print(texto[1:4])  # yth
print(texto[:3])   # Pyt
print(texto[3:])   # hon
print(texto[-2:])  # on
print(texto[::2])  # Pto
print(texto[::-1]) # nohtyP
```

Omitir límites utiliza los extremos correspondientes al sentido del recorrido. Un paso -1 permite recorrer desde el final hacia el principio.

El slicing tolera límites que superen el tamaño del texto; el acceso a una posición individual inexistente no.

## 3. Métodos que vas a utilizar

| Expresión | Qué devuelve | Ejemplo |
|---|---|---|
| `texto.lower()` | Texto en minúsculas | `"HOLA".lower()` → "hola" |
| `texto.upper()` | Texto en mayúsculas | `"hola".upper()` → "HOLA" |
| `texto.title()` | Texto con formato de título | `"ana lópez".title()` → "Ana López" |
| `texto.strip()` | Texto sin blancos en los extremos | `" Ana ".strip()` → "Ana" |
| `texto.replace(" ", "")` | Texto sin espacios ordinarios | `"Ana Luz".replace(" ", "")` → "AnaLuz" |
| `texto.isdigit()` | Booleano: todos sus caracteres son dígitos y no está vacío | `"0123".isdigit()` → True |

`strip()` también elimina tabulaciones y saltos de línea de los extremos. No elimina los espacios interiores.

```python
nombre = "  Ana Luz  "
print(len(nombre.strip()))             # 7: cuenta el espacio interior
print(len(nombre.replace(" ", "")))    # 6
```

Para ignorar también otros blancos interiores existe `"".join(texto.split())`. Es una ampliación; para enunciados que solo hablen del espacio ordinario, `replace(" ", "")` suele bastar.

```python
texto = "HOLA"
texto.lower()
print(texto)  # HOLA: no guardamos el resultado

texto = texto.lower()
print(texto)  # hola
```

## 4. Buscar con in y find()

Si solo necesitas saber si aparece un texto, utiliza `in`.

```python
frase = "Aprendo Python"
print("Python" in frase)  # True
print("python" in frase)  # False
print("java" not in frase) # True
```

Para ignorar mayúsculas, transforma tanto el texto como la búsqueda:

```python
frase = "Aprendo Python"
busqueda = "PYTHON"
encontrada = busqueda.lower() in frase.lower()
print(encontrada)  # True
```

Esto busca una **subcadena**, no necesariamente una palabra completa: `"pan" in "pantalla"` es True.

Si necesitas la posición de la primera aparición, `find()` devuelve el índice o -1:

```python
texto = "programación"
print(texto.find("o"))  # 2
print(texto.find("ó"))  # 10
print(texto.find("z"))  # -1
```

Las letras con tilde son caracteres distintos de sus equivalentes sin tilde. `lower()` transforma "Ó" en "ó", pero no elimina la tilde.

## 5. Encadenar operaciones

Cada método devuelve un resultado que puede utilizar el siguiente:

```python
usuario = "  ANA LUZ  "
usuario_limpio = usuario.strip().lower().replace(" ", "")
print(usuario_limpio)  # analuz
```

Puedes escribirlo en varios pasos si así entiendes mejor el proceso. La legibilidad es más útil que condensarlo todo en una línea.

## 6. Repetición y enmascaramiento

```python
codigo = "12345678"
oculto = "*" * 5 + codigo[-3:]
print(oculto)  # *****678
```

Multiplicar un texto por un entero repite ese texto. Los últimos caracteres se extraen mediante slicing.

Una tarjeta se guarda como texto, no como entero. Para limitar una entrada a los dígitos ASCII 0–9, `isdigit()` por sí solo admite más caracteres Unicode; puedes combinar `texto.isascii()` y `texto.isdigit()`. En estas prácticas, aclara primero qué entradas espera el enunciado.

## 7. Guía de los ejercicios, en orden

| Ejercicio | Herramientas y planteamiento |
|---|---|
| 06 · Inversión | Leer la frase y recorrerla con slicing de paso -1. |
| 07 · Nombres | Obtener cada transformación desde el texto original. Para contar sin espacios, quitar los interiores antes de usar len(). |
| 08 · Correo | Normalizar nombre y apellido, eliminar los espacios pedidos y unirlos con el punto y el dominio. |
| 09 · Subcadenas | Normalizar ambos textos y guardar el resultado booleano de in. |
| 10 · Enmascaramiento | Comprobar la longitud y el tipo de caracteres; construir la parte oculta y añadir los últimos cuatro caracteres. |

## 8. Errores frecuentes y consulta rápida

- Escribe `texto.lower()`, con paréntesis: necesitas ejecutar el método.
- `len(texto)` es una función; no se escribe `texto.len()`.
- `texto[1:4]` no incluye la posición 4.
- No conviertas códigos a números si necesitas conservar sus ceros iniciales.
- Una búsqueda vacía está contenida en cualquier cadena: valida ese caso si no tiene sentido para tu ejercicio.

**Transformar:** métodos de str · **Longitud:** len() · **Fragmento:** slicing · **Presencia:** in · **Posición:** find().

Referencia: [Tipos y operaciones de cadenas](https://docs.python.org/es/3/library/stdtypes.html#text-sequence-type-str).
