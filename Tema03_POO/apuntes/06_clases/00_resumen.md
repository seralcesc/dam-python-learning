# 📘 Guía Completa de POO y Arquitectura Modular en Python (1º DAM)

> **Propósito de esta guía:** Manual de consulta rápida y estructurada para diseñar, implementar y depurar proyectos orientados a objetos distribuidos en paquetes dentro del módulo de Programación (1º DAM).

---

## 📑 Índice de Contenidos

1. [Arquitectura Modular y Comunicación entre Paquetes](#1-arquitectura-modular-y-comunicación-entre-paquetes)
2. [Las 2 Formas de Comunicar Objetos (Colaboración)](#2-las-2-formas-de-comunicar-objetos-colaboración)
3. [Regla de Oro: Clase (Plano) vs. Objeto (Instancia)](#3-regla-de-oro-clase-plano-vs-objeto-instancia)
4. [Fundamentos de Clases: `__init__` y `self`](#4-fundamentos-de-clases-__init__-y-self)
5. [Niveles de Visibilidad y Encapsulación (`_`, `__`)](#5-niveles-de-visibilidad-y-encapsulación-_-__)
6. [Getters (`@property`), Setters (`@setter`) y Solo Lectura](#6-getters-property-setters-setter-y-solo-lectura)
7. [Anotaciones de Tipo (*Type Hints* - PEP 484)](#7-anotaciones-de-tipo-type-hints---pep-484)
8. [Plantilla Estándar de `main.py` (CLI + Interactivo)](#8-plantilla-estándar-de-mainpy-cli--interactivo)
9. [Checklist de 4 Pasos antes de Escribir Código](#9-checklist-de-4-pasos-antes-de-escribir-código)

---

## 1. Arquitectura Modular y Comunicación entre Paquetes

En proyectos reales no se mezcla toda la lógica en un único archivo. Se divide el sistema por responsabilidades en **paquetes** (carpetas) coordinados desde un punto de entrada central (`main.py`).

### Estructura estándar de directorios

```text
mi_proyecto/
├── main.py                  <-- Coordinador principal (Entrada/Salida)
├── paquete_a/
│   ├── __init__.py          <-- Archivo vacío OBLIGATORIO (convierte la carpeta en paquete)
│   └── modulo_a.py          <-- Contiene 'class ClaseA'
└── paquete_b/
    ├── __init__.py          <-- Archivo vacío OBLIGATORIO
    └── modulo_b.py          <-- Contiene 'class ClaseB'
```

### Reglas de importación
* Las rutas **siempre** parten desde la carpeta raíz donde reside `main.py` (nunca desde carpetas superiores de tu ordenador como `Tema03_POO...`).
* **Si `modulo_b.py` necesita usar `ClaseA`:**
  ```python
  # Línea 1 de paquete_b/modulo_b.py
  from paquete_a.modulo_a import ClaseA
  ```
* **En `main.py` (necesita ambas clases):**
  ```python
  from paquete_a.modulo_a import ClaseA
  from paquete_b.modulo_b import ClaseB
  ```

---

## 2. Las 2 Formas de Comunicar Objetos (Colaboración)

Cuando tienes dos objetos creados en `main.py` y el segundo necesita información del primero para hacer un cálculo o evaluación, fíjate en la **firma del método** del enunciado:

### Forma A: Pasar un dato suelto (`float`, `int`, `str`)
Cuando el parámetro pide un tipo básico:
```python
# En CalculadorAutonomia:
def estimar_distancia_m(self, pct_disponible: float) -> float:
    return pct_disponible / 0.05
```
* **En `main.py`:** Extraes el atributo con el punto y lo pasas:
  ```python
  distancia = calculador.estimar_distancia_m(mi_robot.bateria_pct)
  ```

### Forma B: Pasar el objeto completo (Asociación / Colaboración)
Cuando el parámetro pide una clase propia (`trabajo_obj: TrabajoImpresion3D`):
```python
# En EstimadorImpresion:
def calcular_tiempo_min(self, trabajo_obj: TrabajoImpresion3D, seg_por_capa: float = 12.0) -> float:
    # ⚠️ NUNCA multipliques 'trabajo_obj' directamente; accede a sus atributos con el punto:
    return (trabajo_obj.capas_totales * seg_por_capa) / 60
```
* **En `main.py`:** Pasas la variable que contiene el objeto entero:
  ```python
  tiempo = estimador.calcular_tiempo_min(mi_trabajo)
  ```

---

## 3. Regla de Oro: Clase (Plano) vs. Objeto (Instancia)

| Concepto | Analogía | Sintaxis | ¿Puede ejecutar métodos con `self`? |
| :--- | :--- | :--- | :--- |
| **Clase** | Plano arquitectónico en papel | `ValidadorRedOT` | ❌ **NO.** Si haces `ValidadorRedOT.es_ip_valida(ip)` da `TypeError`. |
| **Objeto (Instancia)** | Edificio construido en memoria | `val = ValidadorRedOT()` | ✅ **SÍ.** Se invoca sobre la instancia: `val.es_ip_valida(ip)`. |

> **Regla:** Todo método cuya firma empiece por `(self, ...)` exige **instanciar primero** la clase con paréntesis `()` antes de invocar el método con el punto.

---

## 4. Fundamentos de Clases: `__init__` y `self`

* **`class NombreClase:`** Siempre en **PascalCase** (cada palabra empieza en mayúscula, sin guiones bajos).
* **`def __init__(self, ...):`** Es el **constructor**. Python lo ejecuta automáticamente al instanciar el objeto para inicializar su estado interno.
* **`self`:** Representa a **la instancia concreta** que está ejecutando el código en ese momento.
  * Si creas `horno_1` y `horno_2`, cada uno tiene su propio espacio en memoria.
  * Todo dato que deba conservar el objeto tras terminar `__init__` debe asignarse a `self.atributo`. Si no lleva `self.`, es una variable local temporal que desaparece al acabar el método.

---

## 5. Niveles de Visibilidad y Encapsulación (`_`, `__`)

La encapsulación protege la integridad de los datos internos de un objeto frente a modificaciones inválidas desde el exterior.

| Nivel | Prefijo | Ejemplo | Comportamiento y Acceso |
| :--- | :---: | :--- | :--- |
| **Público** | *Ninguno* | `self.id_motor` | Libre lectura y escritura desde cualquier parte del programa (`obj.id_motor`). |
| **Protegido** | `_` | `self._vibracion` | **Convenio profesional (PEP 8):** Indica que es interno de la clase y sus subclases. Desde fuera debe accederse mediante `@property`, nunca tocando `obj._vibracion`. |
| **Privado** | `__` | `self.__temperatura` | **Candado estricto (*Name Mangling*):** Python renombra internamente el atributo a `_Clase__temperatura`. Intentar leer `obj.__temperatura` desde `main.py` lanza `AttributeError`. Solo accesible dentro de su propia clase. |

---

## 6. Getters (`@property`), Setters (`@setter`) y Solo Lectura

### Patrón A: Lectura y Escritura Validada (`@property` + `@setter`)
Úsalo cuando un dato pueda modificarse desde fuera, pero deba cumplir reglas de negocio (ej. no aceptar valores negativos):

```python
class SensorVibracion:
    def __init__(self, id_motor_in: str, vibracion_rms_val: float):
        self.id_motor = id_motor_in
        # ✅ Llamamos al SETTER (sin guion bajo) para validar desde el nacimiento:
        self.vibracion_rms = vibracion_rms_val

    # GETTER: Permite leer 'sensor.vibracion_rms' desde fuera
    @property
    def vibracion_rms(self) -> float:
        return self._vibracion_rms      # Lee del almacén interno (con _)

    # SETTER: Se dispara automáticamente al hacer 'sensor.vibracion_rms = valor'
    @vibracion_rms.setter
    def vibracion_rms(self, nuevo_valor: float) -> None:
        if nuevo_valor < 0.0:
            raise ValueError("La vibración RMS no puede ser negativa.")
        self._vibracion_rms = nuevo_valor  # Guarda en el almacén interno (con _)
```

* **`raise ValueError("mensaje")`:** Interrumpe la ejecución lanzando una excepción (equivalente a `throw new IllegalArgumentException()` en Java) cuando llega un dato ilegal.
* **Trampa mortal a evitar:** Nunca escribas `self._vibracion_rms = valor` dentro de `__init__` si tienes un `@setter`, ni accedas a `obj._vibracion_rms` desde `main.py`, o te saltarás la validación del *setter*.

### Patrón B: Propiedad de Solo Lectura (Solo `@property`, SIN `@setter`)
Úsalo cuando un atributo privado (`__`) deba poder consultarse desde fuera, pero **nadie** pueda sobrescribirlo manualmente (solo cambian mediante métodos propios como `enfriar()` o `validar_acceso()`):

```python
class GemeloHorno:
    def __init__(self, id_horno_in: str, temp_inicial_val: float):
        self.id_horno = id_horno_in
        # ✅ Como NO existe setter, aquí SÍ asignamos directo al privado (__):
        self.__temperatura = temp_inicial_val

    @property
    def temperatura(self) -> float:
        return self.__temperatura
```
* Leer `horno.temperatura` en `main.py` $\rightarrow$ **Funciona.**
* Intentar `horno.temperatura = 500.0` en `main.py` $\rightarrow$ **`AttributeError: property 'temperatura' has no setter`.**

---

## 7. Anotaciones de Tipo (*Type Hints* - PEP 484)

Documentan qué tipo de dato entra por cada parámetro y qué tipo devuelve cada método, habilitando el autocompletado inteligente en VS Code:

* **Tipos básicos:** `codigo: str`, `capas: int`, `temperatura: float`, `activo: bool`
* **Objetos propios:** `sensor_obj: SensorVibracion`
* **Valores por defecto:** `tasa: float = 2.5` (opcional al llamar; toma `2.5` si se omite).
* **Retorno del método (`-> tipo`):**
  * `-> float` / `-> int` / `-> str` / `-> bool`: El método **debe** ejecutar un `return` con un valor de ese tipo.
  * `-> None`: El método **no** devuelve ningún valor (ej. `__init__` o `@setter`).

---

## 8. Plantilla Estándar de `main.py` (CLI + Interactivo)

Todos los proyectos requieren soporte dual: lectura por argumentos de línea de comandos (`sys.argv`) para corrección automatizada y lectura interactiva (`input()`) para ejecución manual.

```python
import sys

from paquete_a.modulo_a import ClaseA
from paquete_b.modulo_b import ClaseB


def ejecutar_aplicacion():
    print("=== TÍTULO EXACTO DEL ENUNCIADO ===")

    # Si el programa pide N datos de entrada, len(sys.argv) debe ser N + 1
    # (porque sys.argv[0] siempre es el nombre del archivo 'main.py')
    if len(sys.argv) == 3:
        dato_1 = sys.argv[1]
        dato_2 = float(sys.argv[2])          # ⚠️ Convertir siempre int() o float()
    else:
        dato_1 = input("Texto exacto 1: ")
        dato_2 = float(input("Texto exacto 2: "))

    # Instanciación y lógica de negocio
    obj_a = ClaseA(dato_1, dato_2)
    obj_b = ClaseB()
    resultado = obj_b.procesar(obj_a)

    # Salida formateada al milímetro
    print("-------------------------------------------")
    print(f"Resultado: {resultado:.2f}")


# Atajo en VS Code: escribe 'main' y pulsa Tab
if __name__ == "__main__":
    ejecutar_aplicacion()
```

---

## 9. Checklist de 4 Pasos antes de Escribir Código

1. **Estructura de paquetes:** Crea las carpetas al mismo nivel que `main.py` (nunca una dentro de otra) con su `__init__.py` vacío.
2. **Clases independientes primero:** Implementa las clases base, revisando que `@property` y `@setter` estén al mismo nivel de indentación que `__init__` (4 espacios).
3. **Clases colaboradoras después:** Importa desde la raíz (`from paquete.archivo import Clase`) y recuerda usar el punto (`obj.atributo`) al operar con objetos recibidos.
4. **Verificación dual en terminal:** Prueba siempre el proyecto tanto con `python main.py` (interactivo) como con `python main.py arg1 arg2` (CLI) comprobando que la salida coincida carácter por carácter con el enunciado.