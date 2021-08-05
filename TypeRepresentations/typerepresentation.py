from abc import ABC, abstractmethod

class TypeRepresentation(ABC):
    @abstractmethod
    def get_representation(self) -> str:
        pass