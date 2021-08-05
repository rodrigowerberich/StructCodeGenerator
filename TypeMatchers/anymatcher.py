from TypeMatchers.typematchers import TypeMatcher
from TypeRepresentations.typerepresentation import TypeRepresentation


class AnyMatcher(TypeMatcher):

    def __init__(self, representation: TypeRepresentation):
        self._representation = representation

    def matches(self, type_str: str) -> bool:
        return True

    def get_representation(self) -> TypeRepresentation:
        return self._representation
