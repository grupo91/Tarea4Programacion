



# entity.py abstract class for all entities in the system

from abc import ABC, abstractmethod

class Entity(ABC):
    
    # Base abstract class that enforces structure for all entities
        
    def __init__(self, id):
        self._id = id

    @abstractmethod
    def display(self):
        # this method must be implement by all subclasses
        
        pass

