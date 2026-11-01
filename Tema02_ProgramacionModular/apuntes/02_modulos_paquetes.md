# 02 · Módulos, paquetes y main.py

[Índice del tema](../README.md) · [Anterior](01_funciones.md) · [Siguiente: importaciones](03_importaciones.md)

**Aplicación:** estructura común a los proyectos 01–30.

## 1. Distinguir las piezas

| Concepto | Qué representa en estas prácticas |
|---|---|
| Función | Una tarea definida con def |
| Módulo | Un archivo .py que puede contener funciones y otras definiciones |
| Paquete | Carpeta que agrupa módulos; en estos proyectos incluye __init__.py |
| Proyecto | Carpeta completa de una práctica con main.py y su paquete |
| Biblioteca | Conjunto de herramientas reutilizables; puede incluir módulos y paquetes |

La biblioteca estándar viene con Python. Tus módulos son código que escribes tú. Ambos pueden importarse.

## 2. Ejemplo completo de un proyecto pequeño

Crea los archivos indicados respetando los nombres:

```text
demo_tienda/
├── main.py
└── tienda/
    ├── __init__.py
    ├── calculos.py
    └── formato.py
```

**Archivo tienda/calculos.py:**

```python
def calcular_total(unidades, precio):
    return unidades * precio
```

**Archivo tienda/formato.py:**

```python
def formatear_euros(importe):
    return f"{importe:.2f} €"
```

**Archivo tienda/__init__.py:** vacío.

**Archivo main.py:**

```python
from tienda.calculos import calcular_total
from tienda.formato import formatear_euros

if __name__ == "__main__":
    unidades = int(input("Unidades: "))
    precio = float(input("Precio: "))
    total = calcular_total(unidades, precio)
    print(formatear_euros(total))
```

Para probarlo, abre una terminal en demo_tienda y ejecuta:

```powershell
python main.py
```

Con 3 unidades a 2.5, muestra 7.50 €. Los bloques pertenecen a archivos diferentes; no debes pegarlos todos en un único archivo.

## 3. Quién hace cada tarea

main.py coordina: lee, convierte, llama y muestra.

calculos.py conoce cómo calcular el total; no necesita saber si las unidades vienen del teclado o de un caso de prueba.

formato.py transforma el importe en un texto. Devuelve ese texto; main.py decide cuándo mostrarlo.

Agrupa por responsabilidad. No necesitas crear un archivo por función si varias forman parte de la misma tarea.

## 4. Qué hace if __name__ == "__main__"

Python asigna un valor a __name__ en cada módulo:

| Forma de utilizar el archivo | Valor habitual de __name__ |
|---|---|
| Ejecutar main.py directamente | "__main__" |
| Importar tienda.calculos | "tienda.calculos" |

El bloque protegido se ejecuta si el archivo es el programa de entrada. Si otro módulo lo importa, ese bloque no se ejecuta.

Importar un archivo **sí ejecuta su código de nivel superior al cargarlo por primera vez en el proceso**. Por eso conviene evitar input() o acciones sueltas en módulos de biblioteca.

Definir funciones fuera de ese bloque es correcto: sus cuerpos no se ejecutan hasta llamarlas.

Un módulo de biblioteca puede tener un bloque __main__ para demostraciones o pruebas. No es obligatorio ni está prohibido; en tus prácticas, el enunciado reserva el punto de entrada para main.py.

## 5. Para qué sirve __init__.py

En estos proyectos identifica la carpeta como un paquete regular y puede estar vacío.

Python puede ejecutar su contenido al importar el paquete. No lo uses para pedir datos o arrancar el programa. Existen paquetes de espacio de nombres sin este archivo, pero no los necesitas para estas prácticas.

No borres __init__.py por estar vacío: forma parte de la estructura solicitada.

## 6. __pycache__ y .pyc

Al importar módulos, Python puede guardar versiones compiladas en __pycache__. Facilitan cargas posteriores.

No sustituyen al código fuente ni necesitas copiarlas entre ordenadores. El .gitignore las excluye; Python puede regenerarlas.

## 7. Orden para construir un proyecto

1. Leer la estructura que pide el enunciado.
2. Crear carpeta del proyecto, paquete y módulos.
3. Implementar una función pequeña y probar su resultado con valores conocidos.
4. Conectar sus importaciones desde main.py.
5. Añadir entradas y salidas.
6. Comprobar el programa desde la carpeta del proyecto.

Si falla, distingue: ¿no encuentra el módulo, falla al calcular o busca mal un archivo de datos? Cada problema tiene una causa diferente.

**No ejecutes un módulo interno esperando ver el programa completo.** Si solo contiene definiciones, que termine sin mostrar nada puede ser lo correcto.

Referencia: [Módulos y paquetes](https://docs.python.org/es/3/tutorial/modules.html).
