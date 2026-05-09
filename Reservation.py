from datetime import datetime
from exceptions import ReservationError
from logger_config import setup_logger

# Configurar logger
logger = setup_logger()


class Reserva:

    def __init__(self, cliente, servicio, duracion):

        try:
            self.cliente = cliente
            self.servicio = servicio
            self.duracion = duracion
            self.estado = "Pendiente"
            self.costo_total = 0

            self.validar_reserva()

            self.escribir_log("Reserva creada correctamente.")

        except Exception as error:

            self.escribir_log(
                "Error al crear la reserva: " + str(error)
            )

            raise ReservationError(
                "La reserva no pudo ser creada."
            ) from error

        finally:
            print("Proceso de creación de reserva finalizado.")

    # ==================================================
    # VALIDAR RESERVA
    # ==================================================

    def validar_reserva(self):

        try:

            if self.cliente is None:
                raise ReservationError(
                    "El cliente es obligatorio."
                )

            if self.servicio is None:
                raise ReservationError(
                    "El servicio es obligatorio."
                )

            if self.duracion is None:
                raise ReservationError(
                    "La duración es obligatoria."
                )

            if not isinstance(self.duracion, (int, float)):
                raise ReservationError(
                    "La duración debe ser numérica."
                )

            if self.duracion <= 0:
                raise ReservationError(
                    "La duración debe ser mayor que cero."
                )

            if self.estado not in [
                "Pendiente",
                "Confirmada",
                "Cancelada",
                "Procesada"
            ]:
                raise ReservationError(
                    "Estado de reserva inválido."
                )

        except ReservationError as error:

            self.escribir_log(
                "Error de validación: " + str(error)
            )

            raise

    # ==================================================
    # CONFIRMAR RESERVA
    # ==================================================

    def confirmar_reserva(self):

        try:

            if self.estado == "Cancelada":
                raise ReservationError(
                    "Una reserva cancelada no puede confirmarse."
                )

            if self.estado == "Procesada":
                raise ReservationError(
                    "Una reserva procesada no puede confirmarse nuevamente."
                )

            if self.estado == "Confirmada":
                raise ReservationError(
                    "La reserva ya está confirmada."
                )

        except ReservationError as error:

            self.escribir_log(
                "Error al confirmar reserva: " + str(error)
            )

            print("Error:", error)

        else:

            self.estado = "Confirmada"

            self.escribir_log(
                "Reserva confirmada correctamente."
            )

            print(
                "Reserva confirmada correctamente."
            )

        finally:

            print(
                "Proceso de confirmación finalizado."
            )

    # ==================================================
    # CANCELAR RESERVA
    # ==================================================

    def cancelar_reserva(self):

        try:

            if self.estado == "Procesada":
                raise ReservationError(
                    "Una reserva procesada no puede cancelarse."
                )

            if self.estado == "Cancelada":
                raise ReservationError(
                    "La reserva ya está cancelada."
                )

        except ReservationError as error:

            self.escribir_log(
                "Error al cancelar reserva: " + str(error)
            )

            print("Error:", error)

        else:

            self.estado = "Cancelada"

            self.escribir_log(
                "Reserva cancelada correctamente."
            )

            print(
                "Reserva cancelada correctamente."
            )

        finally:

            print(
                "Proceso de cancelación finalizado."
            )

    # ==================================================
    # PROCESAR RESERVA
    # ==================================================

    def procesar_reserva(self):

        try:

            if self.estado != "Confirmada":
                raise ReservationError(
                    "Solo las reservas confirmadas pueden procesarse."
                )

            try:

                self.costo_total = (
                    self.servicio.calcular_costo(
                        self.duracion,
                        impuesto=0.19,
                        descuento=0.05
                    )
                )

            except Exception as error:

                self.escribir_log(
                    "Error en cálculo de costo: " + str(error)
                )

                raise ReservationError(
                    "Hubo un problema calculando el costo de la reserva."
                ) from error

            if self.costo_total <= 0:
                raise ReservationError(
                    "El costo total es inválido."
                )

        except ReservationError as error:

            self.escribir_log(
                "Error al procesar reserva: " + str(error)
            )

            print("Error:", error)

        else:

            self.estado = "Procesada"

            self.escribir_log(
                f"Reserva procesada correctamente. Costo total: {self.costo_total}"
            )

            print(
                "Reserva procesada correctamente."
            )

            print(
                "Costo total:",
                self.costo_total
            )

        finally:

            print(
                "Proceso de procesamiento finalizado."
            )

    # ==================================================
    # MOSTRAR RESERVA
    # ==================================================

    def mostrar_reserva(self):

        print("\n--- Información de la Reserva ---")

        print("Cliente:", self.cliente)

        print("Servicio:", self.servicio)

        print("Duración:", self.duracion)

        print("Estado:", self.estado)

        print("Costo total:", self.costo_total)

    # ==================================================
    # MÉTODO LOG
    # ==================================================

    def escribir_log(self, mensaje):

        logger.info(mensaje)

    # ==================================================
    # REPRESENTACIÓN EN STRING
    # ==================================================

    def __str__(self):

        return (
            f"Reserva("
            f"Cliente={self.cliente}, "
            f"Servicio={self.servicio}, "
            f"Duración={self.duracion}, "
            f"Estado={self.estado}, "
            f"Costo={self.costo_total}"
            f")"
        )