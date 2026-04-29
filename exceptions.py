

# exceptions.py 
# defines custom exceptions for the sistem to handle errors properly.


class SystemError(Exception):
    """ Base exception for all systems errors
     serves as the parent class for all custom exceptions"""
    
    def __init__(self, message: str, error_code: str = "SYS_ERROR"):
        
        """inicialize a SystemError exception.
        
        Args:
            message (str): Human-readable description of what went wrong
            error_code (str): Unique code to identify the error type
                           Default is "SYS_ERROR" if not specified"""
        
        # gurda el mensaje de error como una variable de instancia                  
        self.message = message    
        self.error_code = error_code
        # llama al constructor de la clase padre(Exception)
        super().__init__(self.message) 
     
    def __str__(self):
        
        """Return a readable string representation of the exception."""
        
        # usa f-string para formatear el mensaje de error con el código de error
        return f"{self.error_code}: {self.message}"         
      
        

# Specific exceptions classes.
        
class InvalidDataError(SystemError):
    """
    Exception raised when data provided to the system is invalid."""
    
    def __init__(self, message: str, field: str = None):
        
        """ Initialize an InvalidDataError exception.
    Args:
            message (str): Description of what data is invalid
            field (str): Optional - name of the field that has invalid data
            """
    # guarda en que campo esta el problema        
        self.field = field
    # llama al constructor padre (systemError)
        super().__init__(message, error_code="INVALID_DATA")
    

class ServiceUnavailableError(SystemError):
    
    """Exception raised when a service is not available."""
    
    def __init__(self, message: str, service_id: str = None):
       
        """Initialize a ServiceUnavailableError exception.
        
        Args:
            message (str): Description of the service unavailability
            service_id (str): Optional - ID of the unavailable service
        """
        # Guarda el ID del servicio para poder rastrearlo
        self.service_id = service_id
        # Llama al constructor padre con el codigo de error específico
        super().__init__(message, error_code="SERVICE_UNAVAILABLE")


class ReservationError(SystemError):
    
    """Exception raised when there's an error in reservation operations."""
    
    def __init__(self, message: str, reservation_id: str = None):
        
        """Initialize a ReservationError exception.
        
        Args:
            message (str): Description of the reservation problem
            reservation_id (str): Optional - ID of affected reservation
        """
        # Guarda el ID de la reserva para rastrearla en los logs
        self.reservation_id = reservation_id
        # Llama al constructor padre con el codigo de error específico
        super().__init__(message, error_code="RESERVATION_ERROR")
        
        
class ClientNotFoundError(SystemError):
    
    """Exception raised when a client cannot be found in the system."""
    
    def __init__(self, message: str, client_id: str = None):
        
        """Initialize a ClientNotFoundError exception.
        
        Args:
            message (str): Description of the lookup failure
            client_id (str): Optional - ID of  client that was not found
        """
        # Guarda el ID del cliente que no fue encontrado.
        self.client_id = client_id
        # Llama al constructor padre con el codigo de error específico
        super().__init__(message, error_code="CLIENT_NOT_FOUND")
       
       
class CalculationError(SystemError):
    
    """Exception raised when calculations fail or produce invalid results."""
    
    def __init__(self, message: str, calculation_type: str = None):
        
        """Initialize a CalculationError exception.
        
        Args:
            message (str): Description of the calculation failure
            calculation_details (str): Optional - type of  calculation that failed
        """
        # Guarda el tipo de calculo que fallo 
        self.calculation_type = calculation_type
        # Llama al constructor padre con el codigo de error específico
        super().__init__(message, error_code="CALCULATION_ERROR")       
       
    


