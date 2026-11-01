# Tema 02 · Programación modular

[Volver al repositorio](../README.md)

Prácticas para aprender a dividir un programa en **funciones, módulos y paquetes**. La relación de clase propone 30 proyectos de consola independientes.

## Objetivos

- Definir funciones con parámetros y valores de retorno.
- Utilizar argumentos con valores por defecto.
- Organizar funciones relacionadas en módulos y paquetes.
- Importar y utilizar código de otros módulos.
- Separar la interacción con el usuario de los cálculos y comprobaciones cuando corresponda.
- Utilizar la biblioteca estándar de Python.

## Organización de cada proyecto

Cada carpeta `pNN_nombre` contiene un proyecto independiente. Por ejemplo:

```text
p01_fichaje/
├── main.py
└── fichaje/
    ├── __init__.py
    ├── reloj.py
    └── validar.py
```

- **`main.py`:** punto de entrada. Coordina las llamadas a las funciones y la interacción con el usuario, con el bloque `if __name__ == "__main__":`.
- **Paquete:** carpeta que agrupa los módulos del proyecto y conserva su archivo `__init__.py`, aunque esté vacío.
- **Módulos:** archivos `.py` que contienen las funciones de cada responsabilidad.

Los apuntes y ejemplos de consulta se incorporarán en `apuntes/` conforme se elaboren. Las carpetas `__pycache__` y los archivos `.pyc` son generados por Python y se excluyen mediante el `.gitignore` general.

## Índice de proyectos

Los enlaces llevan a los proyectos incorporados al repositorio. Su presencia no implica que estén revisados o entregados.

| Nº | Proyecto | Conceptos practicados |
|---|---|---|
| 01 | [Terminal automática de fichaje y control horario](p01_fichaje/) | Fechas, horas y comparación de horarios |
| 02 | [Servidor de claves temporales](p02_otp/) | Aleatoriedad y caducidad |
| 03 | [Parquímetro con emisión de ticket](p03_parquimetro/) | Tarifas, fechas y formato monetario |
| 04 | [Gestor de copias de seguridad en ZIP](p04_backups/) | Rutas y creación de archivos ZIP |
| 05 | [Diagnóstico y monitor de red](p05_monitor/) | Subprocesos, sistema operativo y tiempo simulado |
| 06 | [Simulador de cuotas de préstamos](p06_hipotecas/) | Cálculos financieros y formato de salida |
| 07 | [Planificador de mantenimiento](p07_mantenimiento/) | Calendarios y cálculo de fechas |
| 08 | [Validador de licencias desde terminal](p08_licencias/) | Argumentos de consola y códigos de salida |
| 09 | [Control de calidad de piezas](p09_calidad/) | Media y tolerancias |
| 10 | [Tómbola digital](p10_ruleta/) | Selección aleatoria y descuentos |
| 11 | [Conversor marítimo de navegación](p11_conversor/) | Conversión de distancias y velocidades |
| 12 | [Centro de notificaciones](p12_notificaciones/) | Formato de mensajes y funciones de salida |
| 13 | [Buscador de archivos temporales](p13_espacio/) | Exploración de archivos |
| 14 | [Calculadora de combate RPG](p14_juego/) | Dados y cálculo de daño |
| 15 | [Dispensador de turnos](p15_turnos/) | Generación de turnos y marcas de tiempo |
| 16 | [Asistente de dosificación (práctica académica)](p16_farmacia/) | Parámetros y cálculos |
| 17 | [Verificador de archivos críticos](p17_integridad/) | Comprobación de existencia de archivos |
| 18 | [Generador de nombres de informes](p18_ventas/) | Sumas y nombres de archivo |
| 19 | [Calculadora geométrica](p19_construccion/) | Superficies y triángulos |
| 20 | [Cronómetro de intervalos](p20_deporte/) | Medición de tiempo y pausas |
| 21 | [Validador de datos de registro](p21_formulario/) | Validaciones de texto y números |
| 22 | [Gestor de reservas con cita previa](p22_citas/) | Fechas e identificadores |
| 23 | [Monitor de procesamiento por lotes](p23_lotes/) | Separación de cálculos y proceso |
| 24 | [Generador de fichas de empleado](p24_usuarios/) | Formato de fichas y opciones |
| 25 | [Auditor del sistema operativo](p25_logs/) | Información del sistema y salida por consola |
| 26 | [Gestor de promociones de temporada](p26_promociones/) | Mes actual y descuentos |

### Proyectos de la relación pendientes de incorporar

| Nº | Proyecto |
|---|---|
| 27 | Torno de control de aforo |
| 28 | Tarificador de envíos express |
| 29 | Comprobador de horario comercial |
| 30 | Empaquetador de proyectos en archivo ZIP |

## Ejecución

Abre la terminal de VS Code y sitúate **dentro de la carpeta del proyecto** antes de ejecutarlo. Desde la raíz del repositorio:

```powershell
cd Tema02_ProgramacionModular/p01_fichaje
python main.py
```

En Windows puedes sustituir `python` por `py -3` si utilizas el lanzador de Python.

### Proyectos con rutas relativas

Algunas prácticas consultan archivos o carpetas mediante rutas relativas, como `"main.py"` o `"almacenamiento"`. Estas rutas se interpretan desde la carpeta de trabajo de la terminal.

Por ello, para el proyecto de copias de seguridad, ejecuta desde su propia carpeta:

```powershell
cd Tema02_ProgramacionModular/p04_backups
python main.py
```

Este ejemplo también parte de la raíz del repositorio. Los archivos ZIP generados son resultados de ejecución, no código fuente del proyecto.

### Argumentos de consola

El proyecto de licencias recibe la clave como argumento. Desde su carpeta:

```powershell
python main.py ADM-1234-OK
```

### Requisitos particulares

Las prácticas utilizan módulos propios y la biblioteca estándar de Python. El monitor de red también utiliza el comando `ping` del sistema y necesita conectividad para comprobar un equipo remoto. Su latencia se simula con una pausa aleatoria; no representa una medición del tiempo de respuesta de la red.

## Estado del aprendizaje

Tema en curso. Los proyectos se están desarrollando y revisando antes de su presentación. El código conserva las soluciones trabajadas durante esta etapa de aprendizaje y podrá modificarse en commits posteriores.
