# 07 · Matemáticas, estadística, consola y procesos

[Índice del tema](../README.md) · [Anterior](06_rutas_archivos_zip.md)

**Aplicación:** especialmente proyectos 05, 06, 08, 09, 11, 16, 19, 23, 25 y 28.

## 1. math: elegir una operación concreta

```python
import math

print(math.sqrt(81))    # 9.0
print(math.pow(2, 3))   # 8.0
print(math.ceil(2.3))   # 3
print(math.floor(2.9))  # 2
print(math.fabs(-4.5))  # 4.5
print(math.pi)
```

| Necesidad | Herramienta | Observación |
|---|---|---|
| Raíz cuadrada | math.sqrt(x) | En números reales, x no puede ser negativo |
| Potencia | math.pow(x, y) o x ** y | math.pow devuelve float; ** puede conservar enteros |
| Cobrar tramos enteros superiores | math.ceil(x) | No es redondear al más cercano |
| Redondear hacia abajo | math.floor(x) | Con negativos: floor(-2.3) es -3 |
| Valor absoluto | abs(x) o math.fabs(x) | abs no necesita import; fabs devuelve float |
| Aproximación de pi | math.pi | Constante, sin paréntesis |

Para envíos, ceil permite que 2.3 kg cuenten como 3 tramos de un kilo. round podría dar 2 y no cumpliría esa regla.

En cuotas de préstamos, valida meses > 0 y considera aparte el interés 0 si la fórmula general divide por una expresión que se anula en ese caso. No confundas 3.5 % con el factor 3.5: el porcentaje se divide entre 100 antes de operar y se adapta al periodo.

## 2. statistics: media y tolerancia

```python
import statistics

medidas = [9.9, 10.0, 10.1]
media = statistics.mean(medidas)
print(f"{media:.2f}")  # 10.00

nominal = 10.0
margen = 0.5
aceptada = abs(media - nominal) <= margen
print(aceptada)  # True
```

La media utiliza todos los datos entregados. Una colección vacía provoca StatisticsError.

El valor absoluto permite medir desviación por arriba o por abajo. El operador <= incluye el borde de tolerancia; < lo excluye. Respeta lo que pida el enunciado.

## 3. fractions: fracciones exactas sencillas

En tus módulos de conversión también aparece fractions.

```python
from fractions import Fraction

factor = Fraction(3, 2)
print(factor)       # 3/2
print(float(factor)) # 1.5
```

Fraction recibe numerador y denominador; el denominador no puede ser cero.

Si quieres representar una cantidad decimal concreta, Fraction("0.1") expresa 1/10. Fraction(0.1) parte del float binario ya aproximado y puede producir una fracción distinta de la esperada.

## 4. sys.argv: datos que llegan desde la terminal

Al ejecutar:

```powershell
python main.py CLAVE-DEMO
```

el programa puede consultar:

```python
import sys

print(sys.argv)

if len(sys.argv) > 1:
    clave = sys.argv[1]
else:
    clave = ""

print(f"Clave recibida: {clave}")
```

| Posición | Contenido |
|---|---|
| sys.argv[0] | Nombre o ruta del script |
| sys.argv[1] | Primer argumento del usuario, si existe |
| sys.argv[2] | Segundo argumento, si existe |

Todos llegan como texto. Antes de acceder a una posición, comprueba la longitud. Si una entrada contiene espacios, agrúpala entre comillas en la terminal.

input() pide datos durante la ejecución; argv recibe los que ya acompañaban al comando.

## 5. sys.exit: terminar el programa

```python
import sys

clave = "incorrecta"

if clave != "DEMO":
    print("Clave no válida")
    sys.exit(1)

print("Acceso concedido")
```

Este ejemplo termina intencionadamente con estado 1.

El código 0 representa éxito por convención; los distintos de cero indican error u otras condiciones según el programa. sys.exit no devuelve ese código como resultado normal: eleva SystemExit para terminar la ejecución si no se intercepta.

Dentro de un cálculo reutilizable suele ser mejor devolver un resultado y dejar que main.py decida. En el ejercicio de licencias, sigue el contrato que pide el enunciado.

## 6. os.name: consultar el sistema

```python
import os

print(os.name)
```

En Windows suele ser "nt"; en Linux y macOS, "posix". Es un atributo, no una función: no escribas os.name().

Sirve en tu monitor para elegir la opción de conteo de ping.

## 7. subprocess.run: ejecutar otro programa

Ejemplo didáctico para comprobar el equipo local; requiere el comando ping instalado:

```python
import os
import subprocess

parametro = "-n" if os.name == "nt" else "-c"

resultado = subprocess.run(
    ["ping", parametro, "1", "127.0.0.1"],
    capture_output=True,
    timeout=10
)

print(resultado.returncode)
```

| Parte | Qué significa |
|---|---|
| Lista de argumentos | Programa y cada argumento por separado |
| capture_output=True | Guardar stdout y stderr en el resultado |
| timeout=10 | Limitar la espera; si se supera, produce TimeoutExpired |
| returncode | Estado devuelto por el proceso |

run espera a que el proceso termine y devuelve un objeto CompletedProcess. No devuelve directamente True o False. Tu función puede transformar su returncode en un booleano.

La expresión condicional usada arriba equivale a elegir "-n" con un if para Windows y "-c" en el otro caso.

Por defecto, la salida capturada son bytes. Para obtener texto puedes usar text=True, teniendo en cuenta la codificación del programa externo si muestra caracteres incorrectos.

No necesitas shell=True para este ejemplo: pasa los argumentos en una lista. Si ping no existe puede producir FileNotFoundError. Un retorno no exitoso no demuestra por sí solo que un servidor esté apagado: puede haber filtros de red o problemas de resolución.

## 8. Retorno de función y retorno de proceso

No son lo mismo:

- return True entrega un booleano a tu programa Python.
- resultado.returncode consulta el estado de un programa externo.
- sys.exit(1) establece una terminación con error del programa Python.

El proyecto 05 conecta las dos primeras ideas. El proyecto 08 practica la tercera.

## Consulta por ejercicio

| Proyecto | Herramientas que debes entender |
|---|---|
| 05 · Monitor | os.name, subprocess.run y diferencia entre estado y latencia simulada |
| 06 · Cuotas | Fórmulas, math.pow y casos especiales |
| 08 · Licencias | sys.argv, longitud de lista y sys.exit |
| 09 · Calidad | statistics.mean y desviación absoluta |
| 11 · Conversión | Factores, tipos y fractions si se utiliza |
| 19 · Geometría | math.pi, potencias y raíz |
| 25 · Auditor | os.name y formato de salida |
| 28 · Envíos | math.ceil y tarifa por tramo |

Referencias: [math](https://docs.python.org/es/3/library/math.html), [statistics](https://docs.python.org/es/3/library/statistics.html), [fractions](https://docs.python.org/es/3/library/fractions.html), [sys](https://docs.python.org/es/3/library/sys.html) y [subprocess](https://docs.python.org/es/3/library/subprocess.html).
