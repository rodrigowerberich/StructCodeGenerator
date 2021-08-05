from TypeMatchers.typematchers import TypeMatchers
from abc import abstractmethod


class ArrayProcessingTypeMatchers(TypeMatchers):
    @abstractmethod
    def process_type_str_without_arrays(self, type_str: str) -> str:
        pass

    @abstractmethod
    def process_type_str(self, type_str: str) -> str:
        pass
