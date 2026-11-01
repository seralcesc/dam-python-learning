# 04 · Encontrar y entender una herramienta de Python

[Índice del tema](../README.md) · [Anterior](03_importaciones.md) · [Siguiente: fechas, tiempo y azar](05_fechas_tiempo_azar.md)

**Objetivo:** pasar de "necesito hacer algo" a una llamada que entiendas.

## 1. No todo necesita un import

| Tipo de herramienta | Ejemplos | ¿Importar? |
|---|---|---|
| Función incorporada | print, input, len, sum, round | No |
| Método de un objeto | texto.lower(), lista.append(...) | Necesitas ese objeto, no un import de lower |
| Biblioteca estándar | os, zipfile, datetime, math | Sí; vienen con Python |
| Módulo propio | fichaje.reloj | Sí; debe estar en el proyecto o ser localizable |
| Biblioteca externa | Un paquete de terceros | Se instala en el entorno y se importa |

No necesitas pip install os ni pip install zipfile. Son parte de la biblioteca estándar.

"Comando" puede referirse a cosas distintas:

- python main.py: comando de terminal.
- import os: instrucción de Python.
- os.getcwd(): llamada a una función.
- archivo.write(...): llamada a un método de un objeto.
- os.name: consulta de un atributo; no lleva paréntesis.

## 2. Elegir por necesidad

| Necesito… | Herramienta inicial |
|---|---|
| Saber desde qué carpeta se resuelven las rutas | os.getcwd() |
| Comprobar si existe una ruta | os.path.exists(ruta) |
| Distinguir archivo y carpeta | os.path.isfile(ruta), os.path.isdir(ruta) |
| Recorrer subcarpetas | os.walk(ruta) |
| Empaquetar una carpeta completa | shutil.make_archive(...) |
| Elegir qué entra en un ZIP | zipfile.ZipFile y write() |
| Obtener fecha u hora | datetime |
| Esperar o medir un intervalo | time |
| Elegir al azar | random |
| Calcular una raíz | math.sqrt(...) |
| Calcular una media | statistics.mean(...) |
| Leer argumentos de terminal | sys.argv |
| Ejecutar ping | subprocess.run(...) |

No memorices primero toda la biblioteca. Identifica la operación y busca su herramienta concreta.

## 3. Leer una firma

Una firma resumida puede ser:

```text
random.randint(a, b)
```

Preguntas útiles:

1. ¿De qué módulo procede?
2. ¿Cuántos argumentos obligatorios tiene?
3. ¿Qué tipos espera?
4. ¿Qué devuelve?
5. ¿Incluye los límites?
6. ¿Qué errores puede producir?

En randint, a y b son enteros y ambos extremos se incluyen. No presupongas que funciona igual que range, que excluye su final.

Otra firma:

```text
shutil.make_archive(base_name, format, root_dir=...)
```

Los dos primeros argumentos son obligatorios. root_dir tiene valor por defecto, pero suele ser conveniente pasarlo por nombre para indicar claramente qué carpeta empaquetas.

La documentación puede mostrar / o * como marcadores de argumentos posicionales o por nombre. No debes copiarlos como argumentos al realizar la llamada.

## 4. Buscar en la documentación oficial

1. Entra en el [índice de la biblioteca estándar](https://docs.python.org/es/3/library/index.html).
2. Abre el módulo adecuado.
3. Busca el nombre de la función con Ctrl + F.
4. Lee la descripción, los parámetros, el retorno y las excepciones.
5. Comprueba si la función está disponible en la versión de Python que utilizas.
6. Prueba una llamada pequeña con datos conocidos.

Para ver tu versión:

```powershell
python --version
```

Las páginas de /3/ pueden corresponder a una versión distinta de la instalada. Selecciona la versión adecuada en la documentación si ves una función nueva que no existe en tu equipo.

## 5. Explorar con help y dir

En una terminal, ejecuta python para abrir el intérprete. Después:

```python
import os

print(os.getcwd())
help(os.path.exists)
```

help muestra ayuda del objeto. Aquí pasamos os.path.exists **sin llamarlo**, porque queremos consultar la función, no ejecutar una comprobación.

dir(os.path) lista nombres disponibles, pero no sustituye a la documentación: no explica por sí solo qué argumentos necesitan.

En VS Code, el autocompletado y la ayuda de parámetros orientan. Contrasta su significado antes de elegir una función solo porque su nombre parece adecuado.

## 6. Ficha que puedes repetir

| Campo | Ejemplo |
|---|---|
| Necesidad | Comprobar si hay una carpeta de datos |
| Importación | import os |
| Llamada | os.path.isdir("datos") |
| Entrada | Una ruta de texto |
| Retorno | bool |
| Interpretación | True si esa ruta corresponde a un directorio |
| Contexto | La ruta es relativa a la carpeta de trabajo |

Separar retorno y efectos evita errores: una función puede crear un archivo y devolver su ruta, devolver None o devolver un booleano, según su diseño.

## 7. Cuando no funciona

Reduce el caso. Antes de revisar todo un proyecto, muestra la entrada, el tipo y el resultado de la función problemática.

Si una biblioteca no se importa, revisa el intérprete seleccionado y los nombres de tus archivos. Si una ruta no existe, muestra la carpeta de trabajo. Si el retorno no es el esperado, revisa el contrato de la función.

Referencia: [Biblioteca estándar de Python](https://docs.python.org/es/3/library/index.html).
