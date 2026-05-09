from Cliente import Cliente, ClienteError
from Reservation import Reserva

from Servicio import (
    ServicioReservaSala,
    ServicioAlquilerEquipos,
    ServicioAsesoria
)

from exceptions import (
    ReservationError,
    InvalidDataError
)

from logger_config import (
    setup_logger,
    log_exception
)

# ==========================================
# CONFIGURAR LOGGER
# ==========================================

logger = setup_logger()


# ==========================================
# FUNCIONES AUXILIARES
# ==========================================

def separador():
    print("\n" + "=" * 70 + "\n")


def titulo(texto):
    separador()
    print(f" {texto}")
    separador()


# ==========================================
# INICIO DEL SISTEMA
# ==========================================

print("\n")
print("█" * 70)
print("        SISTEMA INTEGRAL SOFTWARE FJ")
print(" Gestión de Clientes, Servicios y Reservas")
print("█" * 70)
print("\n")


# =====================================================
# OPERACIÓN 1
# =====================================================

titulo("OPERACIÓN 1 - CREAR CLIENTE VÁLIDO")

try:

    cliente1 = Cliente(
        "Juan Perez",
        "12345678",
        "juan@email.com",
        "3001234567"
    )

    print(" Cliente creado correctamente")
    print(cliente1)

except ClienteError as error:

    print(" Error al crear cliente")
    logger.error(str(error))


# =====================================================
# OPERACIÓN 2
# =====================================================

titulo("OPERACIÓN 2 - CREAR CLIENTE INVÁLIDO")

try:

    cliente2 = Cliente(
        "",
        "12",
        "correo_invalido",
        "abc"
    )

except ClienteError as error:

    print(" Cliente inválido detectado")
    print(" Motivo:", error)

    logger.error(str(error))


# =====================================================
# OPERACIÓN 3
# =====================================================

titulo("OPERACIÓN 3 - CREAR SERVICIOS VÁLIDOS")

try:

    servicio_sala = ServicioReservaSala(
        "S001",
        "Reserva de Sala",
        100
    )

    servicio_equipos = ServicioAlquilerEquipos(
        "S002",
        "Alquiler de Equipos",
        80
    )

    servicio_asesoria = ServicioAsesoria(
        "S003",
        "Asesoría TI",
        150
    )

    print(" Servicios creados correctamente")
    print(servicio_sala)
    print(servicio_equipos)
    print(servicio_asesoria)

except InvalidDataError as error:

    print(" Error al crear servicios")
    logger.error(str(error))


# =====================================================
# OPERACIÓN 4
# =====================================================

titulo("OPERACIÓN 4 - CREAR SERVICIO INVÁLIDO")

try:

    servicio_invalido = ServicioReservaSala(
        "",
        "",
        -50
    )

except InvalidDataError as error:

    print(" Servicio inválido detectado")
    print(" Motivo:", error)

    logger.error(str(error))


# =====================================================
# OPERACIÓN 5
# =====================================================

titulo("OPERACIÓN 5 - RESERVA VÁLIDA")

try:

    reserva1 = Reserva(
        cliente1,
        servicio_sala,
        5
    )

    reserva1.confirmar_reserva()

    reserva1.procesar_reserva()

    reserva1.mostrar_reserva()

except ReservationError as error:

    print(" Error en reserva")
    logger.error(str(error))


# =====================================================
# OPERACIÓN 6
# =====================================================

titulo("OPERACIÓN 6 - RESERVA SIN CLIENTE")

try:

    reserva2 = Reserva(
        None,
        servicio_sala,
        2
    )

except ReservationError as error:

    print(" Reserva inválida detectada")
    print(" Motivo:", error)

    logger.error(str(error))


# =====================================================
# OPERACIÓN 7
# =====================================================

titulo("OPERACIÓN 7 - RESERVA CON DURACIÓN INVÁLIDA")

try:

    reserva3 = Reserva(
        cliente1,
        servicio_equipos,
        -5
    )

except ReservationError as error:

    print(" Duración inválida detectada")
    print(" Motivo:", error)

    logger.error(str(error))


# =====================================================
# OPERACIÓN 8
# =====================================================

titulo("OPERACIÓN 8 - PROCESAR SIN CONFIRMAR")

try:

    reserva4 = Reserva(
        cliente1,
        servicio_asesoria,
        3
    )

    reserva4.procesar_reserva()

except ReservationError as error:

    print(" Error al procesar reserva")
    print(" Motivo:", error)

    logger.error(str(error))


# =====================================================
# OPERACIÓN 9
# =====================================================

titulo("OPERACIÓN 9 - DOBLE CONFIRMACIÓN")

try:

    reserva5 = Reserva(
        cliente1,
        servicio_sala,
        2
    )

    reserva5.confirmar_reserva()

    reserva5.confirmar_reserva()

except ReservationError as error:

    print(" Error en confirmación")
    print(" Motivo:", error)

    logger.error(str(error))


# =====================================================
# OPERACIÓN 10
# =====================================================

titulo("OPERACIÓN 10 - CANCELAR DESPUÉS DE PROCESAR")

try:

    reserva6 = Reserva(
        cliente1,
        servicio_asesoria,
        4
    )

    reserva6.confirmar_reserva()

    reserva6.procesar_reserva()

    reserva6.cancelar_reserva()

except ReservationError as error:

    print(" Error al cancelar reserva")
    print(" Motivo:", error)

    logger.error(str(error))


# ==========================================
# FIN DEL SISTEMA
# ==========================================

print("\n")
print("█" * 70)
print("        TODAS LAS OPERACIONES FINALIZARON")
print("█" * 70)
print("\n")