from datetime import datetime

# Excepción personalizada
class ClienteError(Exception):
    """Excepción personalizada para errores en Cliente"""
    pass


class Cliente:
    def __init__(self, nombre, identificacion, correo, telefono):
        self.__nombre = None
        self.__identificacion = None
        self.__correo = None
        self.__telefono = None

        # Uso de setters para validar desde el inicio
        self.set_nombre(nombre)
        self.set_identificacion(identificacion)
        self.set_correo(correo)
        self.set_telefono(telefono)

    # =========================
    # GETTERS
    # =========================
    def get_nombre(self):
        return self.__nombre

    def get_identificacion(self):
        return self.__identificacion

    def get_correo(self):
        return self.__correo

    def get_telefono(self):
        return self.__telefono

    # =========================
    # SETTERS CON VALIDACIÓN
    # =========================
    def set_nombre(self, nombre):
        if not nombre or not isinstance(nombre, str):
            raise ClienteError("El nombre no puede estar vacío y debe ser texto")
        if len(nombre) < 3:
            raise ClienteError("El nombre debe tener al menos 3 caracteres")
        self.__nombre = nombre.strip().title()

    def set_identificacion(self, identificacion):
        if not str(identificacion).isdigit():
            raise ClienteError("La identificación debe ser numérica")
        if len(str(identificacion)) < 5:
            raise ClienteError("La identificación es demasiado corta")
        self.__identificacion = str(identificacion)

    def set_correo(self, correo):
        if "@" not in correo or "." not in correo:
            raise ClienteError("Correo inválido")
        self.__correo = correo.lower()

    def set_telefono(self, telefono):
        if not str(telefono).isdigit():
            raise ClienteError("El teléfono debe contener solo números")
        if len(str(telefono)) < 7:
            raise ClienteError("Teléfono inválido")
        self.__telefono = str(telefono)

    # =========================
    # MÉTODO DE REPRESENTACIÓN
    # =========================
    def __str__(self):
        return f"Cliente: {self.__nombre} | ID: {self.__identificacion} | Email: {self.__correo}"
