# 06 · Rutas, archivos y ZIP: os, shutil y zipfile

[Índice del tema](../README.md) · [Anterior](05_fechas_tiempo_azar.md) · [Siguiente: otras herramientas](07_otras_herramientas.md)

**Aplicación:** proyectos 04, 13, 17, 25 y 30. Lee primero las secciones de rutas, aunque tu duda sea sobre ZIP.

## 1. Una ruta es una dirección

| Tipo | Ejemplo | Se interpreta desde… |
|---|---|---|
| Absoluta en Windows | C:/practicas/datos/nota.txt | La ubicación completa indicada |
| Relativa | datos/nota.txt | La carpeta de trabajo del proceso |
| Relativa al nivel superior | ../nota.txt | El padre de la carpeta de trabajo |

Estar editando un archivo en VS Code no garantiza que la terminal esté situada en esa misma carpeta.

```python
import os

print(os.getcwd())
```

getcwd() muestra la carpeta de trabajo. Es lo primero que debes comprobar si exists devuelve False cuando ves el archivo en el explorador.

Ejemplo: si trabajas desde dam-python-learning, la ruta "main.py" busca en la raíz, no dentro de p04_backups.

## 2. Cómo ejecutar tus prácticas

Haz clic derecho sobre la carpeta p04_backups y selecciona **Abrir en terminal integrado**. Después:

```powershell
python main.py
```

Ahora "main.py" y "almacenamiento" se buscan desde p04_backups, como esperan los ejemplos de esa práctica.

La ubicación de un módulo importado no cambia automáticamente la carpeta de trabajo.

## 3. Escribir rutas en Windows

Puedes utilizar barras normales:

```python
ruta = "C:/practicas/datos/nota.txt"
```

Para rutas con barras invertidas, una cadena raw evita interpretar secuencias como barra-n o barra-t:

```python
ruta = r"C:\practicas\datos\nota.txt"
```

Una cadena raw no puede terminar en una única barra invertida.

Para componer rutas, utiliza herramientas de rutas en lugar de concatenar separadores manualmente.

## 4. Elegir la comprobación correcta

```python
import os

ruta = "datos"
print(os.path.exists(ruta))
print(os.path.isfile(ruta))
print(os.path.isdir(ruta))
```

| Función | Pregunta |
|---|---|
| exists(ruta) | ¿Existe esa ruta? |
| isfile(ruta) | ¿Es un archivo regular? |
| isdir(ruta) | ¿Es un directorio? |
| join(a, b) | ¿Cómo se compone una ruta con esas partes? |
| abspath(ruta) | ¿Cuál es su representación absoluta desde aquí? |
| relpath(ruta, inicio) | ¿Cómo se expresa ruta desde inicio? |

exists no distingue archivo de carpeta. Si una función se llama existe_archivo y solo usa exists, su nombre es más específico que lo que realmente comprueba.

```python
import os

ruta = os.path.join("datos", "nota.txt")
print(os.path.abspath(ruta))
```

join y abspath construyen o transforman rutas; no crean archivos ni verifican por sí mismos que existan.

## 5. listdir y walk: un nivel o todo el árbol

```python
import os

if os.path.isdir("datos"):
    for nombre in os.listdir("datos"):
        ruta = os.path.join("datos", nombre)
        if os.path.isfile(ruta):
            print(ruta)
```

listdir devuelve nombres de entradas inmediatas, no sus rutas completas. Usa join antes de comprobarlas desde otra ubicación.

Para recorrer también subcarpetas:

```python
import os

for carpeta_actual, subcarpetas, archivos in os.walk("datos"):
    for nombre in archivos:
        ruta = os.path.join(carpeta_actual, nombre)
        print(ruta)
```

En cada vuelta:

- carpeta_actual es la carpeta que se está visitando.
- subcarpetas es una lista de nombres de sus directorios.
- archivos es una lista de nombres de sus archivos.

Si filtras temporales con nombre.endswith(".tmp"), estás eligiendo entradas por extensión; no implica que debas borrarlas. La práctica puede limitarse a encontrarlas.

## 6. Leer y escribir un archivo de prueba

La función incorporada open no necesita importar os.

```python
with open("ejemplo_apuntes.txt", "w", encoding="utf-8") as archivo:
    archivo.write("Primera línea\n")

with open("ejemplo_apuntes.txt", "r", encoding="utf-8") as archivo:
    contenido = archivo.read()

print(contenido)
```

Este ejemplo crea un archivo de práctica en la carpeta de trabajo. El modo w reemplaza su contenido si ya existe. El modo r lee y requiere que exista; a añade al final.

with gestiona el cierre del recurso, también si se produce una excepción dentro del bloque. No elimina el archivo ni garantiza que no haya errores.

## 7. shutil: empaquetar una carpeta con pocos pasos

**Preparación:** crea una carpeta datos de prueba con algún archivo, en la carpeta de trabajo.

```python
import os
import shutil

if os.path.isdir("datos"):
    ruta_zip = shutil.make_archive(
        "respaldo_apuntes",
        "zip",
        root_dir="datos"
    )
    print(ruta_zip)
else:
    print("No existe la carpeta datos.")
```

| Argumento | Significado |
|---|---|
| "respaldo_apuntes" | Nombre base de salida, sin .zip |
| "zip" | Formato |
| root_dir="datos" | Carpeta cuyo contenido se empaqueta |

Genera respaldo_apuntes.zip con el contenido de datos. Devuelve la ruta del archivo creado. No devuelve True automáticamente.

Si tu función propia debe devolver un bool, ese contrato lo implementas tú. Una comprobación previa de existencia no elimina posibles errores posteriores de permisos o escritura.

Utiliza un nombre de salida distinto si necesitas conservar una copia anterior.

## 8. zipfile: controlar qué archivos entran

ZipFile es una clase del módulo zipfile. Al llamarla obtienes un objeto que representa un archivo ZIP.

**Preparación:** crea datos/nota.txt. Este ejemplo crea copia_apuntes.zip en la carpeta de trabajo:

```python
import zipfile

with zipfile.ZipFile(
    "copia_apuntes.zip",
    mode="w",
    compression=zipfile.ZIP_DEFLATED
) as archivo_zip:
    archivo_zip.write("datos/nota.txt", arcname="nota.txt")
```

Se lee así:

1. Abrir o crear copia_apuntes.zip para escribir.
2. Usar compresión DEFLATE.
3. Dentro del bloque, acceder al ZIP mediante archivo_zip.
4. Añadir el archivo de disco datos/nota.txt.
5. Guardarlo dentro del ZIP con el nombre nota.txt.
6. Al salir de with, cerrar el ZIP.

No necesitas dominar POO todavía para usar el objeto. Distingue el módulo zipfile, la clase ZipFile y el objeto archivo_zip.

### Modos de apertura

| Modo | Uso |
|---|---|
| r | Leer un ZIP existente |
| w | Crear o reemplazar el ZIP |
| a | Añadir entradas a un ZIP |
| x | Crear solo si no existe; si existe, falla |

La compresión predeterminada de ZipFile es ZIP_STORED: empaqueta sin comprimir. Si el ejercicio pide compresión, indica ZIP_DEFLATED u otro método apropiado.

Añadir una carpeta con write() no recorre automáticamente su contenido. Para incluir todos sus archivos necesitas recorrerla o utilizar make_archive.

## 9. Ruta de disco y nombre dentro del ZIP

```python
archivo_zip.write(ruta_disco, arcname=nombre_interno)
```

Esta línea es un fragmento: supone que el ZIP y las variables ya existen.

- ruta_disco identifica el archivo real que Python debe leer.
- nombre_interno es la ubicación que tendrá en el ZIP.
- arcname no mueve ni renombra el archivo original.

Si datos/subcarpeta/nota.txt se expresa respecto de datos, su ruta relativa es subcarpeta/nota.txt. Esa es una buena opción de nombre interno.

## 10. Combinar os.walk con ZipFile

**Preparación:** carpeta datos con archivos y, si quieres, subcarpetas. La salida se guarda fuera de datos.

```python
import os
import zipfile

origen = "datos"
salida = "carpeta_apuntes.zip"

if os.path.isdir(origen):
    with zipfile.ZipFile(
        salida, "w", compression=zipfile.ZIP_DEFLATED
    ) as archivo_zip:
        for carpeta, subcarpetas, archivos in os.walk(origen):
            subcarpetas[:] = [
                nombre for nombre in subcarpetas
                if nombre != "__pycache__"
            ]
            for nombre in archivos:
                if nombre.endswith(".pyc"):
                    continue
                ruta_disco = os.path.join(carpeta, nombre)
                nombre_interno = os.path.relpath(ruta_disco, origen)
                archivo_zip.write(ruta_disco, arcname=nombre_interno)
    print("ZIP creado.")
else:
    print("La carpeta de origen no existe.")
```

La asignación subcarpetas[:] modifica la lista que os.walk utiliza para decidir por dónde descender. Es una ampliación para excluir cachés; puedes estudiar primero el recorrido sin ese filtro.

Coloca la salida fuera del árbol que recorres para evitar incluir el ZIP mientras se escribe. Esta versión guarda archivos y conserva sus rutas relativas; no guarda directorios vacíos.

## 11. Comprobar el contenido del ZIP

```python
import zipfile

with zipfile.ZipFile("carpeta_apuntes.zip", "r") as archivo_zip:
    print(archivo_zip.namelist())
```

Debe ejecutarse después de crear ese archivo. Revisa que los nombres internos tengan sentido y que estén los archivos esperados.

El .gitignore no controla lo que entra en un ZIP creado por tu programa: sus reglas afectan a Git, no a os.walk ni a ZipFile.

## 12. Ampliación: rutas basadas en el propio script

Si necesitas que un recurso esté junto al archivo .py independientemente de la terminal:

```python
import os

carpeta_script = os.path.dirname(os.path.abspath(__file__))
ruta_datos = os.path.join(carpeta_script, "datos")
print(ruta_datos)
```

Ejecuta este ejemplo como archivo .py: __file__ no está disponible normalmente en el intérprete interactivo.

Para estas prácticas puedes empezar ejecutando desde la carpeta correcta. Más adelante, pathlib ofrece otra forma de trabajar con rutas.

## Guía de elección

| Si necesitas… | Elige |
|---|---|
| Saber por qué no encuentra el archivo | getcwd y abspath |
| Comprobar el tipo de origen | isfile o isdir |
| Empaquetar todo con una llamada | shutil.make_archive |
| Filtrar y controlar nombres internos | os.walk más ZipFile |
| Añadir una extensión al nombre | Distinguir: make_archive la añade; ZipFile utiliza el nombre que pasas |

Referencias: [os](https://docs.python.org/es/3/library/os.html), [os.path](https://docs.python.org/es/3/library/os.path.html), [shutil](https://docs.python.org/es/3/library/shutil.html) y [zipfile](https://docs.python.org/es/3/library/zipfile.html).
