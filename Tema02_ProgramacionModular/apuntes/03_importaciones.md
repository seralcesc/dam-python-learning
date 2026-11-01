# 03 · Importaciones: cómo leerlas y utilizarlas

[Índice del tema](../README.md) · [Anterior](02_modulos_paquetes.md) · [Siguiente: buscar herramientas](04_biblioteca_estandar.md)

**Aplicación:** todos los proyectos; especialmente entender import os, datetime y los módulos propios.

## 1. Importar hace accesible un nombre

No copies el código de una biblioteca dentro de tu programa. Impórtalo y utiliza su interfaz.

```python
import math

resultado = math.sqrt(81)
print(resultado)  # 9.0
```

math es el módulo; sqrt es una función que contiene. El punto permite acceder a un nombre dentro de otro objeto o módulo; los paréntesis realizan una llamada.

## 2. Tres formas de utilizar la misma función

Estos ejemplos son alternativas:

| Importación | Llamada correspondiente |
|---|---|
| import math | math.sqrt(81) |
| from math import sqrt | sqrt(81) |
| import math as matematicas | matematicas.sqrt(81) |
| from math import sqrt as raiz | raiz(81) |

Importar sqrt directamente no introduce automáticamente el nombre math. Elige una forma y mantén coherencia con la llamada.

Los alias no traducen ni modifican la función: solo cambian el nombre con que accedes a ella en ese archivo.

## 3. Aplicarlo a tu proyecto de fichaje

| Importación en main.py | Cómo llamar |
|---|---|
| import fichaje.reloj | fichaje.reloj.obtener_hora_actual() |
| import fichaje.reloj as reloj | reloj.obtener_hora_actual() |
| from fichaje import reloj | reloj.obtener_hora_actual() |
| from fichaje.reloj import obtener_hora_actual | obtener_hora_actual() |

No añadas .py en el import. La ruta de módulos usa puntos, no barras.

Si el profesor solicita expresamente una forma concreta de importación, respeta esa forma aunque otras sean válidas.

## 4. Por qué datetime.datetime no es una errata

El módulo datetime contiene una clase que también se llama datetime.

```python
import datetime

ahora = datetime.datetime.now()
print(ahora.year)
```

Se lee: del módulo datetime, toma la clase datetime y llama a now().

La alternativa:

```python
from datetime import datetime

ahora = datetime.now()
print(ahora.year)
```

Ahora el nombre datetime representa la clase importada directamente. No puedes mezclar ambas sintaxis sin adaptar las llamadas.

## 5. Importar en el archivo donde lo necesitas

Si reloj.py utiliza datetime, debe importarlo. Que main.py haya importado datetime no lo hace visible automáticamente dentro de reloj.py.

Cada módulo tiene su propio espacio de nombres.

Ubica habitualmente los imports al principio del archivo, antes de las funciones. Separa visualmente los de biblioteca estándar de los de tus módulos para leerlos mejor.

Evita from modulo import *: dificulta saber de dónde procede cada nombre y puede ocultar otros.

## 6. Cómo encuentra Python tus módulos

Al ejecutar python main.py de la forma habitual, el directorio de ese script forma parte de la búsqueda de módulos. Por eso puede encontrar el paquete hermano fichaje.

No confundas esta búsqueda con la resolución de rutas de datos:

- import fichaje.reloj busca un módulo.
- os.path.exists("main.py") consulta un archivo desde la carpeta de trabajo.

Una importación puede funcionar y, aun así, fallar una ruta relativa de archivos. La guía de rutas explica esa diferencia.

## 7. Errores frecuentes

| Error | Qué revisar primero |
|---|---|
| ModuleNotFoundError | Nombre, ubicación del paquete y archivo que estás ejecutando |
| ImportError al importar un nombre | Si ese nombre existe y está escrito igual; posibles importaciones circulares |
| NameError | Si importaste ese nombre concreto o necesitas anteponer el módulo |
| AttributeError | Si la función pertenece a ese objeto y si mezclaste formas de importar |

No llames a tus archivos math.py, random.py, os.py o zipfile.py para practicar esas bibliotecas: un archivo local puede ocultar el módulo esperado.

Evita dependencias circulares: main.py puede importar tus módulos, pero estos no deberían importar main.py para recuperar sus variables. Pasa datos mediante parámetros.

## Consulta rápida

Pregunta siempre: **¿Qué nombre ha quedado disponible en este archivo?** Ese nombre determina cómo comienza la llamada.

Referencia: [Importaciones en el tutorial oficial](https://docs.python.org/es/3/tutorial/modules.html).
