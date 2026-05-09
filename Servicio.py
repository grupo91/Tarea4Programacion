from abc import ABC, abstractmethod
from exceptions import InvalidDataError, CalculationError


class Servicio(ABC):

    def __init__(self, id_servicio, nombre, tarifa_base):

        self.id_servicio = id_servicio
        self.nombre = nombre
        self.tarifa_base = tarifa_base

        self.validar()

    # ==========================================
    # VALIDAR DATOS
    # ==========================================

    def validar(self):

        if not self.id_servicio:
            raise InvalidDataError(
                "El ID del servicio no puede estar vacío."
            )

        if not self.nombre:
            raise InvalidDataError(
                "El nombre del servicio no puede estar vacío."
            )

        if not isinstance(self.tarifa_base, (int, float)):
            raise InvalidDataError(
                "La tarifa base debe ser numérica."
            )

        if self.tarifa_base <= 0:
            raise InvalidDataError(
                "La tarifa base debe ser mayor que cero."
            )

    # ==========================================
    # MÉTODOS ABSTRACTOS
    # ==========================================

    @abstractmethod
    def calcular_costo(
        self,
        duracion,
        impuesto=0,
        descuento=0
    ):
        pass

    @abstractmethod
    def obtener_descripcion(self):
        pass

    # ==========================================
    # STRING
    # ==========================================

    def __str__(self):

        return (
            f"{self.nombre} | "
            f"Tarifa base: {self.tarifa_base}"
        )


# =====================================================
# SERVICIO RESERVA DE SALAS
# =====================================================

class ServicioReservaSala(Servicio):

    def calcular_costo(
        self,
        duracion,
        impuesto=0,
        descuento=0
    ):

        try:

            total = self.tarifa_base * duracion

            total += total * impuesto

            total -= total * descuento

            if total <= 0:
                raise CalculationError(
                    "Costo inválido."
                )

            return total

        except Exception as error:

            raise CalculationError(
                "Error calculando costo de reserva de sala."
            ) from error

    def obtener_descripcion(self):

        return "Servicio de reserva de salas."


# =====================================================
# SERVICIO ALQUILER DE EQUIPOS
# =====================================================

class ServicioAlquilerEquipos(Servicio):

    def calcular_costo(
        self,
        duracion,
        impuesto=0,
        descuento=0
    ):

        try:

            costo_extra = 20

            total = (
                self.tarifa_base * duracion
            ) + costo_extra

            total += total * impuesto

            total -= total * descuento

            if total <= 0:
                raise CalculationError(
                    "Costo inválido."
                )

            return total

        except Exception as error:

            raise CalculationError(
                "Error calculando costo de alquiler."
            ) from error

    def obtener_descripcion(self):

        return "Servicio de alquiler de equipos."


# =====================================================
# SERVICIO DE ASESORÍAS
# =====================================================

class ServicioAsesoria(Servicio):

    def calcular_costo(
        self,
        duracion,
        impuesto=0,
        descuento=0
    ):

        try:

            tarifa_profesional = 50

            total = (
                self.tarifa_base * duracion
            ) + tarifa_profesional

            total += total * impuesto

            total -= total * descuento

            if total <= 0:
                raise CalculationError(
                    "Costo inválido."
                )

            return total

        except Exception as error:

            raise CalculationError(
                "Error calculando costo de asesoría."
            ) from error

    def obtener_descripcion(self):

        return "Servicio de asesoría especializada."