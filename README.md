# Sistema Integral de Gestión - Software FJ

## Descripción del Proyecto

Este proyecto fue desarrollado para la Fase 4 del curso de Programación de la Universidad Nacional Abierta y a Distancia (UNAD).

El sistema simula la gestión de clientes, servicios y reservas para la empresa ficticia **Software FJ**, aplicando los principios de Programación Orientada a Objetos (POO) y manejo avanzado de excepciones en Python.

El programa permite:

* Registrar clientes
* Crear diferentes tipos de servicios
* Gestionar reservas
* Confirmar reservas
* Cancelar reservas
* Procesar reservas
* Validar errores
* Registrar eventos y excepciones en logs

Todo el sistema funciona sin bases de datos, utilizando únicamente objetos, clases y archivos de logs.

---

# Objetivos del Proyecto

* Implementar Programación Orientada a Objetos.
* Aplicar encapsulación, herencia, abstracción y polimorfismo.
* Utilizar manejo avanzado de excepciones.
* Garantizar estabilidad del sistema ante errores.
* Registrar eventos y errores mediante logs.

---

# Estructura del Proyecto

```plaintext
Proyecto/
│
├── Cliente.py
├── entity.py
├── Servicio.py
├── Reservation.py
├── exceptions.py
├── logger_config.py
├── main.py
├── README.md
```

---

# Explicación de Cada Archivo

## Cliente.py

Contiene la clase `Cliente`.

Funciones principales:

* Registrar clientes
* Validar:

  * nombre
  * identificación
  * correo
  * teléfono
* Aplicar encapsulación mediante atributos privados
* Lanzar excepciones personalizadas

Ejemplo de validaciones:

```python
if not nombre:
    raise ClienteError("El nombre no puede estar vacío")
```

---

## Servicio.py

Contiene:

### Clase abstracta `Servicio`

Define la estructura base de todos los servicios.

Métodos abstractos:

* `calcular_costo()`
* `obtener_descripcion()`

### Servicios derivados

* `ServicioReservaSala`
* `ServicioAlquilerEquipos`
* `ServicioAsesoria`

Cada servicio implementa polimorfismo mediante diferentes cálculos de costo.

---

## Reservation.py

Gestiona las reservas del sistema.

Funciones principales:

* Crear reservas
* Validar reservas
* Confirmar reservas
* Cancelar reservas
* Procesar reservas
* Mostrar información de reservas
* Registrar logs

También implementa:

* `try`
* `except`
* `else`
* `finally`
* encadenamiento de excepciones

Ejemplo:

```python
raise ReservationError(
    "La reserva no pudo ser creada."
) from error
```

---

## exceptions.py

Contiene todas las excepciones personalizadas del sistema:

* `SystemError`
* `InvalidDataError`
* `ReservationError`
* `ServiceUnavailableError`
* `ClientNotFoundError`
* `CalculationError`

Esto permite manejar errores de forma organizada y profesional.

---

## logger_config.py

Configura el sistema de logs.

Funciones:

* Crear carpeta `logs`
* Generar archivo `system.log`
* Registrar errores
* Registrar eventos del sistema

---

## main.py

Archivo principal del proyecto.

Aquí se ejecutan todas las simulaciones del sistema.

Incluye:

* Clientes válidos
* Clientes inválidos
* Servicios válidos
* Servicios inválidos
* Reservas exitosas
* Reservas fallidas
* Validaciones
* Manejo de excepciones

---

# Principios de Programación Orientada a Objetos Aplicados

## Encapsulación

Se utilizaron atributos privados y métodos getters/setters.

Ejemplo:

```python
self.__nombre
```

---

## Herencia

Las clases de servicios heredan de la clase abstracta `Servicio`.

Ejemplo:

```python
class ServicioReservaSala(Servicio)
```

---

## Abstracción

Uso de clases abstractas y métodos abstractos.

Ejemplo:

```python
@abstractmethod
def calcular_costo():
```

---

## Polimorfismo

Cada servicio calcula costos de forma diferente.

Ejemplo:

* Reserva de salas
* Alquiler de equipos
* Asesorías

Todos implementan el método:

```python
calcular_costo()
```

---

# Manejo de Excepciones

El sistema implementa manejo avanzado de excepciones utilizando:

* `try`
* `except`
* `else`
* `finally`
* excepciones personalizadas
* encadenamiento de excepciones

Ejemplo:

```python
try:
    reserva.procesar_reserva()

except ReservationError as error:
    print(error)
```

---

# Sistema de Logs

Todos los errores y eventos importantes se almacenan en:

```plaintext
logs/system.log
```

Esto permite:

* rastrear errores
* mantener estabilidad
* registrar operaciones del sistema

---

# Operaciones Simuladas

El sistema realiza al menos 10 operaciones completas:

1. Cliente válido
2. Cliente inválido
3. Servicios válidos
4. Servicio inválido
5. Reserva válida
6. Reserva sin cliente
7. Reserva con duración inválida
8. Procesar sin confirmar
9. Doble confirmación
10. Cancelar después de procesar

---

# Errores Corregidos Durante el Desarrollo

Durante el desarrollo del proyecto se corrigieron diversos errores:

## 1. Falta de importación de excepciones

Problema:

```python
ReservationError no estaba importado
```

Solución:

```python
from exceptions import ReservationError
```

---

## 2. Duplicación de logs

Problema:

Se escribían logs manualmente y también mediante logger.

Solución:

Se unificó todo el sistema utilizando `logger_config.py`.

---

## 3. Tracebacks visibles en consola

Problema:

Los errores mostraban información técnica extensa.

Solución:

Se configuró el logger para guardar traceback únicamente en el archivo `.log`.

---

## 4. Inconsistencia de idioma

Problema:

El proyecto mezclaba inglés y español.

Solución:

Se unificaron nombres de clases, métodos y mensajes en español.

---

## 5. Validaciones incompletas

Problema:

Algunos datos no eran validados correctamente.

Solución:

Se agregaron validaciones robustas para clientes, servicios y reservas.

---

# Requisitos Cumplidos

El proyecto cumple con:

* Programación Orientada a Objetos
* Encapsulación
* Herencia
* Polimorfismo
* Abstracción
* Manejo avanzado de excepciones
* Logs
* Validaciones
* Sistema sin base de datos
* Simulación de operaciones válidas e inválidas

---

# Tecnologías Utilizadas

* Python 3
* Programación Orientada a Objetos
* Logging de Python

---

# Autores

Grupo 91
Curso Programación - UNAD
Ingeniería de Sistemas

Integrantes:
* Andres becerra
* Marlon Salazar
* Juan Esteban Lezcano
* Hanny pico vergara

---

# Conclusiones

El desarrollo de este proyecto permitió aplicar de forma práctica los principios fundamentales de Programación Orientada a Objetos y manejo avanzado de excepciones en Python.

Además, se logró construir un sistema estable y modular capaz de continuar funcionando aun cuando se presentan errores durante su ejecución.

El proyecto fortaleció habilidades relacionadas con:

* diseño de software
* validación de datos
* manejo de errores
* depuración
* trabajo colaborativo mediante GitHub

---
