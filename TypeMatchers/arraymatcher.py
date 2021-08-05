import re
from abc import ABC, abstractmethod

from TypeMatchers.arrayprocessingtypematcher import ArrayProcessingTypeMatchers
from TypeMatchers.typematchers import TypeMatcher
from TypeRepresentations.echorepresentation import EchoRepresentation
from TypeRepresentations.typerepresentation import TypeRepresentation


class ArrayRepresentationGenerator(ABC):
    @abstractmethod
    def get_representation(self, type_name, num_of_elements) -> TypeRepresentation:
        pass


class ArrayMatcher(TypeMatcher):
    def __init__(self, type_str: str, type_matcher: ArrayProcessingTypeMatchers, array_representation: ArrayRepresentationGenerator):
        self._type_str = type_str
        self._representation = EchoRepresentation('')
        self._type_matcher = type_matcher
        self._array_representation = array_representation

    def matches(self, original_type_str: str) -> bool:
        array_number_regex = re.findall(r'(\w+)\[(\d+)\]', original_type_str)
        if array_number_regex:
            array_type_str = self._type_matcher.process_type_str_without_arrays(array_number_regex[0][0])
            number = int(array_number_regex[0][1])
            self._representation = self._array_representation.get_representation(array_type_str, number)
            return True
        else:
            return False

    def get_representation(self) -> TypeRepresentation:
        return self._representation
