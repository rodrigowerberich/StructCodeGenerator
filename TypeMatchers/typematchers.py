from abc import ABC, abstractmethod
from TypeRepresentations.typerepresentation import TypeRepresentation


class TypeMatcher(ABC):
    @abstractmethod
    def matches(self, type_str: str) -> bool:
        pass

    @abstractmethod
    def get_representation(self) -> TypeRepresentation:
        pass


class TypeMatchers(ABC):
    @abstractmethod
    def process_type_str(type_str: str) -> str:
        pass