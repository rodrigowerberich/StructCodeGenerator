from TypeMatchers.anymatcher import AnyMatcher
from TypeMatchers.arraymatcher import ArrayRepresentationGenerator, ArrayMatcher
from TypeMatchers.stringmatcher import StringMatcher
from TypeRepresentations.echorepresentation import EchoRepresentation
from TypeRepresentations.typerepresentation import TypeRepresentation
from TypeMatchers.arrayprocessingtypematcher import ArrayProcessingTypeMatchers


class PascalIntRepresentation(TypeRepresentation):
    def get_representation(self) -> str:
        return "LongInt"


class PascalArrayRepresentationGenerator(ArrayRepresentationGenerator):
    def get_representation(self, type_name: str, num_of_elements: int) -> TypeRepresentation:
        return EchoRepresentation(f'array[{0}..{num_of_elements - 1}] of {type_name}')


class PascalTypeMatcher(ArrayProcessingTypeMatchers):

    def __init__(self):
        self._process_array = True

    def _build_matchers(self, type_str: str, include_array_matchers: bool):
        array_matcher = [ArrayMatcher(type_str, self, PascalArrayRepresentationGenerator())]
        matchers = [
            StringMatcher('int', PascalIntRepresentation()),
            AnyMatcher(EchoRepresentation(type_str))
        ]
        if include_array_matchers:
            matchers = array_matcher + matchers
        return matchers

    @staticmethod
    def _process_type_str(type_str: str, matchers) -> str:
        for matcher in matchers:
            if matcher.matches(type_str):
                return matcher.get_representation().get_representation()

    def process_type_str_without_arrays(self, type_str: str) -> str:
        matchers = self._build_matchers(type_str, include_array_matchers=False)
        return self._process_type_str(type_str, matchers)

    def process_type_str(self, type_str: str) -> str:
        matchers = self._build_matchers(type_str, include_array_matchers=True)
        return self._process_type_str(type_str, matchers)