from processentryline import ProcessEntryLine
from parseresultinterface import ParseResult
import re
from abc import ABC, abstractmethod


class TypeRepresentation(ABC):
    @abstractmethod
    def get_representation(self) -> str:
        pass


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


class ArrayProcessingTypeMatchers(TypeMatchers):
    @abstractmethod
    def process_type_str_without_arrays(self, type_str: str) -> str:
        pass

    @abstractmethod
    def process_type_str(self, type_str: str) -> str:
        pass


class PascalIntRepresentation(TypeRepresentation):
    def get_representation(self) -> str:
        return "LongInt"


class EchoRepresentation(TypeRepresentation):

    def __init__(self, str_to_echo: str):
        self._str_to_echo = str_to_echo

    def get_representation(self) -> str:
        return self._str_to_echo


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


class AnyMatcher(TypeMatcher):

    def __init__(self, representation: TypeRepresentation):
        self._representation = representation

    def matches(self, type_str: str) -> bool:
        return True

    def get_representation(self) -> TypeRepresentation:
        return self._representation


class ArrayMatcher(TypeMatcher):
    def __init__(self, type_str: str, type_matcher: ArrayProcessingTypeMatchers):
        self._type_str = type_str
        self._representation = EchoRepresentation('')
        self._type_matcher = type_matcher

    def matches(self, original_type_str: str) -> bool:
        array_number_regex = re.findall(r'(\w+)\[(\d+)\]', original_type_str)
        if array_number_regex:
            array_type_str = self._type_matcher.process_type_str_without_arrays(array_number_regex[0][0])
            number = int(array_number_regex[0][1])
            self._representation = EchoRepresentation(f'array[{0}..{number - 1}] of {array_type_str}')
            return True
        else:
            return False

    def get_representation(self) -> TypeRepresentation:
        return self._representation


class PascalTypeMatcher(ArrayProcessingTypeMatchers):

    def __init__(self):
        self._process_array = True

    def _build_matchers(self, type_str: str, include_array_matchers: bool):
        array_matcher = [ArrayMatcher(type_str, self)]
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


class ProcessEntryLinePascal(ProcessEntryLine):

    def comment(self, regex_result: ParseResult, context):
        print('{ ', regex_result.parts()[0], ' }', sep='')

    def data_type_start(self, regex_result, context):
        print(f'{regex_result.parts()[0]}Msg = packed record')

    def data_field(self, regex_result, context):
        name_str = regex_result.parts()[0]
        raw_type_str = regex_result.parts()[1]
        type_str = PascalTypeMatcher().process_type_str(raw_type_str)
        print(f'     {name_str}:    {type_str};')

    def data_type_end(self, regex_result, context):
        print(f'end ;')
