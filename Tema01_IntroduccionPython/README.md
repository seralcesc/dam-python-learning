# Tema 01 · Introducción a Python

[Volver al repositorio](../README.md)

Primeros ejercicios de Python para practicar la sintaxis del lenguaje y consolidar el razonamiento algorítmico. La relación consta de **30 ejercicios organizados en seis bloques**, conservando la numeración del enunciado original.

## Organización

Cada ejercicio es un programa independiente, guardado en un archivo `ejerNN.py` dentro de su bloque. Los enunciados se incluyen como comentarios al principio de los archivos.

## Apuntes de consulta

Lee los apuntes en orden la primera vez y utiliza después las tablas y los apartados de errores frecuentes para resolver dudas. Incluyen ejemplos comentados y guías para plantear los ejercicios, sin sustituir la práctica por soluciones completas.

| Orden | Apunte | Ejercicios |
|---|---|---|
| 01 | [Fundamentos, variables y entrada/salida](apuntes/01_fundamentos.md) | 01–05 |
| 02 | [Cadenas de texto](apuntes/02_cadenas.md) | 06–10 |
| 03 | [Condicionales](apuntes/03_condicionales.md) | 11–15 |
| 04 | [Bucles while y validación](apuntes/04_while.md) | 16–20 |
| 05 | [Bucles for y rangos](apuntes/05_for.md) | 21–25 |
| 06 | [Patrones algorítmicos](apuntes/06_patrones_algoritmicos.md) | 26–30 |

En VS Code puedes abrir cualquier archivo Markdown y pulsar **Ctrl + Shift + V** para leerlo en vista previa. Copia cada ejemplo que quieras probar en un archivo `.py` independiente. Algunos fragmentos ilustran una expresión y necesitan las variables del ejemplo anterior.

## Índice de bloques

| Bloque | Contenido | Ejercicios |
|---|---|---|
| [01 — Fundamentos, variables y entrada/salida](Bloque01_Fundamentos/) | Variables, tipos básicos, conversiones con `int()` y `float()`, `input()`, `print()`, operaciones y f-strings. | 1–5 |
| [02 — Operadores y cadenas de texto](Bloque02_Cadenas/) | Slicing, métodos de cadenas, longitud, búsquedas y formato de texto. | 6–10 |
| [03 — Estructuras condicionales](Bloque03_Condicionales/) | `if`, `elif`, `else`, comparaciones y operadores lógicos. | 11–15 |
| [04 — Bucles while y validación](Bloque04_While/) | Repetición condicionada, intentos limitados, valores de finalización y menús. | 16–20 |
| [05 — Bucles for y rangos](Bloque05_For/) | `for`, `range()`, recorridos de cadenas y construcción de patrones. | 21–25 |
| [06 — Patrones algorítmicos](Bloque06_PatronesAlgoritmicos/) | Contadores, acumuladores, indicadores booleanos, máximos, mínimos y divisores. | 26–30 |

## Relación de ejercicios

### Bloque 01 — Fundamentos, variables y entrada/salida

Variables, tipos básicos, conversiones con `int()` y `float()`, `input()`, `print()`, operaciones y f-strings.

| Nº | Ejercicio | Archivo |
|---|---|---|
| 01 | Registro de alumno | [ejer01.py](Bloque01_Fundamentos/ejer01.py) |
| 02 | Conversor de temperatura | [ejer02.py](Bloque01_Fundamentos/ejer02.py) |
| 03 | Cálculo del salario bruto | [ejer03.py](Bloque01_Fundamentos/ejer03.py) |
| 04 | Desglose de tiempo | [ejer04.py](Bloque01_Fundamentos/ejer04.py) |
| 05 | Factura de módulo DAM | [ejer05.py](Bloque01_Fundamentos/ejer05.py) |

### Bloque 02 — Operadores y cadenas de texto

Slicing, métodos de cadenas, longitud, búsquedas y formato de texto.

| Nº | Ejercicio | Archivo |
|---|---|---|
| 06 | Inversión de texto | [ejer06.py](Bloque02_Cadenas/ejer06.py) |
| 07 | Formateador de nombres de usuarios | [ejer07.py](Bloque02_Cadenas/ejer07.py) |
| 08 | Generador de handles de correo | [ejer08.py](Bloque02_Cadenas/ejer08.py) |
| 09 | Detector de subcadenas | [ejer09.py](Bloque02_Cadenas/ejer09.py) |
| 10 | Ocultador de datos sensibles | [ejer10.py](Bloque02_Cadenas/ejer10.py) |

### Bloque 03 — Estructuras condicionales

`if`, `elif`, `else`, comparaciones y operadores lógicos.

| Nº | Ejercicio | Archivo |
|---|---|---|
| 11 | Clasificador de números | [ejer11.py](Bloque03_Condicionales/ejer11.py) |
| 12 | Control de acceso al servidor | [ejer12.py](Bloque03_Condicionales/ejer12.py) |
| 13 | Calculadora de calificaciones oficiales | [ejer13.py](Bloque03_Condicionales/ejer13.py) |
| 14 | Tarifario con descuento | [ejer14.py](Bloque03_Condicionales/ejer14.py) |
| 15 | Comprobador de años bisiestos | [ejer15.py](Bloque03_Condicionales/ejer15.py) |

### Bloque 04 — Bucles while y validación

Repetición condicionada, intentos limitados, valores de finalización y menús.

| Nº | Ejercicio | Archivo |
|---|---|---|
| 16 | Validación de contraseña | [ejer16.py](Bloque04_While/ejer16.py) |
| 17 | Sumador continuo hasta cero | [ejer17.py](Bloque04_While/ejer17.py) |
| 18 | Contador regresivo | [ejer18.py](Bloque04_While/ejer18.py) |
| 19 | Menú interactivo de consola | Pendiente de incorporar |
| 20 | Algoritmo de Collatz | [ejer20.py](Bloque04_While/ejer20.py) |

### Bloque 05 — Bucles for y rangos

`for`, `range()`, recorridos de cadenas y construcción de patrones.

| Nº | Ejercicio | Archivo |
|---|---|---|
| 21 | Tabla de multiplicar | [ejer21.py](Bloque05_For/ejer21.py) |
| 22 | Generador de pares en rango | [ejer22.py](Bloque05_For/ejer22.py) |
| 23 | Contador de vocales | [ejer23.py](Bloque05_For/ejer23.py) |
| 24 | Cálculo de factorial | [ejer24.py](Bloque05_For/ejer24.py) |
| 25 | Dibujo de patrón de asteriscos | [ejer25.py](Bloque05_For/ejer25.py) |

### Bloque 06 — Patrones algorítmicos

Contadores, acumuladores, indicadores booleanos, máximos, mínimos y divisores.

| Nº | Ejercicio | Archivo |
|---|---|---|
| 26 | Estadísticas de evaluaciones | [ejer26.py](Bloque06_PatronesAlgoritmicos/ejer26.py) |
| 27 | Buscador de números primos | [ejer27.py](Bloque06_PatronesAlgoritmicos/ejer27.py) |
| 28 | Filtro y acumulador de ventas | [ejer28.py](Bloque06_PatronesAlgoritmicos/ejer28.py) |
| 29 | Registro del mayor y menor número | [ejer29.py](Bloque06_PatronesAlgoritmicos/ejer29.py) |
| 30 | Detector de números perfectos | [ejer30.py](Bloque06_PatronesAlgoritmicos/ejer30.py) |

## Ejecución

Desde la raíz del repositorio, entra en el bloque y ejecuta el archivo correspondiente:

```powershell
cd Tema01_IntroduccionPython/Bloque01_Fundamentos
python ejer01.py
```

En Windows también puedes utilizar `py -3 ejer01.py` si empleas el lanzador de Python.

Estos bloques agrupan scripts independientes; no necesitan archivos `__init__.py`.

## Estado del aprendizaje

Los ejercicios se están rehaciendo para practicar y afianzar los conceptos. Los enlaces del índice indican que el archivo está disponible, no que la solución esté revisada o sea definitiva.

El ejercicio 19 está pendiente de incorporar al repositorio.
