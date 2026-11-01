# DAM · Python Learning Log

![Python](https://img.shields.io/badge/Python-3-3776AB?logo=python&logoColor=white)
![VS Code](https://img.shields.io/badge/Editor-VS%20Code-007ACC?logo=visualstudiocode&logoColor=white)
![DAM](https://img.shields.io/badge/CFGS-DAM-8B00FF)
![Status](https://img.shields.io/badge/Status-En%20desarrollo-FF003C)
![GitHub](https://img.shields.io/badge/Git-GitHub-181717?logo=github&logoColor=white)

Repositorio de aprendizaje donde documento ejercicios, prácticas y pequeños proyectos desarrollados con **Python** durante mi formación en el Ciclo Formativo de Grado Superior de **Desarrollo de Aplicaciones Multiplataforma (DAM)**.

Su objetivo es conservar un registro ordenado de los contenidos trabajados en clase y mostrar mi evolución como desarrollador, desde los primeros programas hasta la organización del código en funciones, módulos y paquetes.

---

## Objetivos

- Consolidar los fundamentos de Python y el razonamiento algorítmico.
- Aplicar los conceptos mediante ejercicios y proyectos de consola.
- Aprender a organizar el código en funciones, módulos y paquetes.
- Mejorar progresivamente la legibilidad y mantenibilidad del código.
- Elaborar apuntes y ejemplos que sirvan de consulta durante el aprendizaje.
- Utilizar Git y GitHub como parte habitual del trabajo entre casa y clase.

---

## Contenido del curso

El repositorio sigue el orden real de los **temas de la asignatura**. Dentro de cada tema, los materiales se organizan según el tipo de práctica.

| Tema | Contenidos | Organización |
|---|---|---|
| **01 — Introducción a Python** | Variables, tipos de datos, entrada/salida, operadores, cadenas, condicionales, bucles y patrones algorítmicos. | Una relación de 30 ejercicios distribuida en seis bloques. |
| **02 — Programación modular** | Funciones, parámetros, valores de retorno, importaciones, módulos, paquetes y uso de la biblioteca estándar. | Una relación de 30 proyectos independientes, cada uno con su punto de entrada y su paquete. |

Estas relaciones describen los ejercicios y proyectos propuestos en clase; no implican que todos estén completados o incorporados al repositorio.

Los índices detallados y las indicaciones particulares se documentarán en el README de cada tema. Se añadirán nuevos temas conforme avance el curso.

---

## Estructura del repositorio

La organización acordada, que se irá completando con los materiales del curso, es la siguiente:

```text
dam-python-learning/
├── README.md
├── .gitignore
├── Tema01_IntroduccionPython/
│   ├── README.md
│   ├── apuntes/
│   ├── Bloque01_Fundamentos/
│   ├── Bloque02_Cadenas/
│   ├── Bloque03_Condicionales/
│   ├── Bloque04_While/
│   ├── Bloque05_For/
│   └── Bloque06_PatronesAlgoritmicos/
└── Tema02_ProgramacionModular/
    ├── README.md
    ├── apuntes/
    ├── p01_fichaje/
    ├── p02_otp/
    └── ...
```

### Organización de los materiales

- **Ejercicios introductorios:** archivos individuales como `ejer01.py` o `ejer06.py`, agrupados por bloques y conservando la numeración original del enunciado.
- **Proyectos modulares:** carpetas independientes como `p01_fichaje`, con un archivo `main.py` y un paquete que contiene `__init__.py` y los módulos correspondientes.
- **Apuntes:** esquemas, explicaciones y ejemplos de consulta dentro de cada tema.
- **Documentación:** un README general para presentar el repositorio y un README por tema para consultar su contenido.

---

## Entorno de desarrollo

- **Lenguaje:** Python 3.
- **Editor:** Visual Studio Code.
- **Sistema operativo:** Windows.
- **Control de versiones:** Git.
- **Cliente de Git:** GitHub Desktop.
- **Repositorio remoto:** GitHub.

El repositorio conserva el código fuente y la documentación. Las cachés de Python, los entornos virtuales y la configuración local de VS Code se excluyen mediante `.gitignore`.

---

## Ejecución

Los ejercicios y proyectos se ejecutan de forma independiente desde la terminal de VS Code, utilizando un intérprete de Python 3 instalado en el equipo.

Para ejecutar un ejercicio introductorio, sitúate en su bloque:

```powershell
cd Tema01_IntroduccionPython/Bloque01_Fundamentos
python ejer01.py
```

Para ejecutar un proyecto modular, sitúate en la carpeta del proyecto:

```powershell
cd Tema02_ProgramacionModular/p01_fichaje
python main.py
```

Ambos ejemplos parten de la raíz del repositorio. Si tu instalación de Windows utiliza el lanzador `py`, puedes sustituir `python` por `py -3`.

Algunos proyectos utilizan rutas relativas a la carpeta de trabajo o requieren argumentos de consola. Sus instrucciones particulares se detallarán en la documentación del tema.

---

## Flujo de trabajo entre casa y clase

El mismo repositorio se clona una vez en cada ordenador. A partir de ese momento, los cambios se comparten a través de GitHub.

1. **Antes de empezar:** abrir GitHub Desktop, pulsar **Fetch origin** y, si hay cambios remotos, **Pull origin**.
2. **Durante el trabajo:** editar y guardar los archivos desde VS Code.
3. **Al terminar:** revisar los cambios en GitHub Desktop y crear un **commit** con un mensaje descriptivo.
4. **Antes de cambiar de equipo:** pulsar **Push origin** para enviar los commits a GitHub.

El commit registra los cambios en el ordenador; el push los envía al repositorio remoto para poder recuperarlos desde el otro equipo.

---

## Estado

🟢 **En desarrollo**

El repositorio se actualiza a medida que avanzo en la asignatura, rehago ejercicios para practicar y completo nuevos proyectos.

---

## Nota

Este repositorio tiene una **finalidad educativa**.

El código refleja diferentes etapas de mi aprendizaje. Las soluciones iniciales pueden ser sencillas y se revisarán conforme incorpore nuevos conocimientos. La presencia de un archivo no implica que su solución sea definitiva.

---

## Autor

**Sergio Alcántara**

Estudiante de **Desarrollo de Aplicaciones Multiplataforma (DAM)**.

[GitHub](https://github.com/seralcesc)
