from TypeMatchers.typematchers import TypeMatcher
from TypeRepresentations.typerepresentation import TypeRepresentation


class StringMatcher(TypeMatcher):
    def __init__(self, str_to_match: str, representation: TypeRepresentation, ignore_case: bool = True):
        self._str_to_match = str_to_match
        self._ignore_case = ignore_case
        self._representation = representation
        if self._ignore_case:
            self._str_to_match = self._str_to_match.lower()

    def matches(self, type_str: str) -> bool:
        _type_str = type_str if not self._ignore_case else type_str.lower()
        return _type_str == self._str_to_match

    def get_representation(self) -> TypeRepresentation:
        return self._representation
