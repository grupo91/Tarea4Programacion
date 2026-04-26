

# exeptions.py 
# defines custom exceptions for the sistem to handle errors properly.


class SystemError(Exception):
    # General system exception
    pass

class InvalidDataError(SystemError):
    # Invalid input data
    pass

class ServiceUnavailableError(SystemError):
    # service not avaible
    pass

class ReservationError(SystemError):
    # Reservation process error
    pass


