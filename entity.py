# entity.py abstract class for all entities in the system

from abc import ABC, abstractmethod
from datetime import datetime
from exceptions import InvalidDataError

class Entity(ABC):
    """
    Abstract Base class for all entities in the system.
    
    This class provides common attributes and methods that all entities 
    (client, service, reservation, etc.) should have.
    
    Implements encapsulation and abstraction principles.
       
        """
        
    def __init__(self, entity_id: str):
        """
        Initialize a genric entity.
        
        
        Args:
           entity_id (str):  Unique Identifier for the entity.
           
        
        Raises: 
           InvalidDataError: If entity_id is invalid
        """
    # Validacion del ID
        if not entity_id or not isinstance(entity_id, str):
            raise InvalidDataError("Entity ID must be a non-empty string.", field="entity_id")
    
    #Atributo protegido (encapsulacion)
        self._entity_id = entity_id
        self._created_at = datetime.now()
        
# Geter para el ID
    @property
    def entity_id(self):
        """Return the entity ID (read-only)."""
        return self._entity_id 
    
#Geter para la fecha de creacion
    @property
    def created_at(self):
        """return the creation timestamp."""
        return self._created_at
    
    @abstractmethod
    def to_dict(self) -> dict:
        """
        Convert the entity to a dictionary format.
        
        Must be implemented by all subclasses
        
        Returns:
            dict: Dictionary representation of the entity.
        
        """
        pass
    
    @abstractmethod
    def validate(self):
        """
        Validate  entity data.
        
        Must be implemented by  subclasses to ensure data integrity.
                
        """
        pass
    
    def __str__(self):
        """ String representation of the entity."""
        return f"{self.__class__.__name__}(ID={self.entity_id})"

