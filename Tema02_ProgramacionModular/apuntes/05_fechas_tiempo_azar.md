# 05 · Fechas, tiempo, calendarios y aleatoriedad

[Índice del tema](../README.md) · [Anterior](04_biblioteca_estandar.md) · [Siguiente: archivos y ZIP](06_rutas_archivos_zip.md)

**Aplicación:** especialmente proyectos 01–03, 05, 07, 10, 14, 15, 18, 20, 22, 26 y 29.

## 1. Elegir la herramienta

| Módulo | Uso |
|---|---|
| datetime | Fechas, horas y diferencias entre instantes |
| time | Pausas y medición de duración |
| calendar | Representación de calendarios |
| random | Simulaciones y selección pseudoaleatoria |

## 2. Consultar un instante y formatearlo

```python
import datetime

ahora = datetime.datetime.now()
print(ahora.year)
print(ahora.month)
print(ahora.hour)
print(ahora.strftime("%d/%m/%Y %H:%M"))
```

now() obtiene un objeto datetime con fecha y hora locales. strftime() devuelve **texto** con el formato solicitado.

| Código | Representa |
|---|---|
| %Y | Año con cuatro cifras |
| %m | Mes numérico |
| %d | Día del mes |
| %H | Hora de 00 a 23 |
| %M | Minutos |
| %S | Segundos |

Mayúsculas y minúsculas importan: %m es mes y %M es minuto.

Para varias decisiones relacionadas, captura ahora una vez y reutilízalo. Así no mezclas datos tomados a ambos lados de un cambio de día o mes.

## 3. Convertir texto en fecha u hora

```python
import datetime

hora = datetime.datetime.strptime("08:45", "%H:%M")
print(hora.hour)    # 8
print(hora.minute)  # 45
```

strftime: objeto → texto. strptime: texto → objeto.

Si el texto no corresponde al formato, strptime puede producir ValueError. No es una función que adivine formatos.

## 4. Restar horas y sumar plazos

```python
import datetime

inicio = datetime.datetime.strptime("08:45", "%H:%M")
fin = datetime.datetime.strptime("10:15", "%H:%M")
diferencia = fin - inicio
minutos = int(diferencia.total_seconds() / 60)
print(minutos)  # 90
```

La resta devuelve timedelta. total_seconds() expresa la duración completa en segundos; no lo confundas con el atributo seconds, que no representa por sí solo todos los días de la diferencia.

Si solo conviertes horas, Python utiliza la misma fecha por defecto. Una salida "01:00" menos una entrada "23:00" será negativa. Para turnos nocturnos debes decidir si el final pertenece al día siguiente y representar ese cambio; no lo arregles tomando el valor absoluto.

```python
import datetime

base = datetime.datetime(2026, 11, 1, 10, 0)
caducidad = base + datetime.timedelta(minutes=5)
print(caducidad.strftime("%H:%M"))  # 10:05

revision = base.date() + datetime.timedelta(days=45)
print(revision.isoformat())  # 2026-12-16
```

Usamos un instante fijo para que el ejemplo tenga siempre el mismo resultado. En tus proyectos, sustituye la base por now() o date.today() cuando corresponda.

## 5. Calendario y día de la semana

```python
import calendar
import datetime

print(calendar.month(2026, 11))
dia = datetime.date(2026, 11, 2)
print(dia.weekday())  # 0: lunes
```

weekday() usa lunes=0 y domingo=6. Para lunes a viernes, comprueba dia.weekday() < 5. Esto no incluye festivos.

calendar.month devuelve un texto con el calendario. Los nombres y el aspecto pueden depender de la configuración regional y del calendario.

## 6. Pausa frente a medida de duración

```python
import time

inicio = time.perf_counter()
time.sleep(0.05)
duracion_ms = (time.perf_counter() - inicio) * 1000
print(f"{duracion_ms:.1f} ms")
```

sleep recibe segundos. perf_counter es apropiado para medir intervalos. El tiempo observado puede superar la pausa solicitada.

time.time() devuelve una marca de tiempo de reloj; aparece en tu relación, pero para medir duraciones perf_counter evita problemas derivados de ajustes del reloj.

En p05_monitor, esperar una duración aleatoria y medir esa espera genera una **latencia simulada**. No mide el ping del servidor.

## 7. Aleatoriedad

```python
import random

dado = random.randint(1, 6)
premio = random.choice(["ORO", "PLATA", "BRONCE"])
pausa = random.uniform(0.05, 0.2)

print(dado)
print(premio)
print(pausa)
```

| Función | Resultado |
|---|---|
| randint(a, b) | Entero, con ambos límites incluidos |
| choice(secuencia) | Un elemento de una secuencia no vacía |
| uniform(a, b) | Float entre los límites; el extremo final puede depender del redondeo |

choice sobre una secuencia vacía falla. Si necesitas un nuevo sorteo por vuelta, vuelve a llamar a la función.

El proyecto OTP practica random, pero los códigos de seguridad reales requieren herramientas como secrets: no conviertas una simulación didáctica en un sistema de autenticación.

## 8. Relación con tus proyectos

| Proyecto | Idea clave |
|---|---|
| 01 · Fichaje | Capturar hora, convertir textos y restar |
| 02 · OTP | Código aleatorio y caducidad con timedelta |
| 03 · Parquímetro | Fecha de emisión y texto monetario |
| 07 · Mantenimiento | Días de margen y calendario |
| 10 y 14 | Selección de premios y dados |
| 20 · Deporte | Pausa y duración de intervalos |
| 26 · Promociones | Comparar el mes actual con el mes objetivo fijo |
| 29 · Horario | Combinar día laborable y límites de hora |

**Errores frecuentes:** confundir formato y objeto; invertir %m y %M; comparar el mes consigo mismo; asumir que una hora de texto incluye la fecha; interpretar una simulación como medida real.

Referencias: [datetime](https://docs.python.org/es/3/library/datetime.html), [time](https://docs.python.org/es/3/library/time.html), [calendar](https://docs.python.org/es/3/library/calendar.html) y [random](https://docs.python.org/es/3/library/random.html).
