import re
import typing
from abc import ABC, abstractmethod
from dataclasses import dataclass
from enum import Enum


class Parser(ABC):
    @abstractmethod
    def parse_line(self, line):
        pass


@dataclass
class RegexExpression:
    id: typing.Any
    regex_str: str


@dataclass
class ParseFunction:
    id: typing.Any
    call: typing.Any


class DictOfIdObject:
    def __init__(self, objects_with_id):
        self._objects_with_id = {}
        for object_with_id in objects_with_id:
            self._objects_with_id[object_with_id.id] = object_with_id

    def __iter__(self):
        return self._objects_with_id.__iter__()

    def __getitem__(self, item):
        return self._objects_with_id.__getitem__(item)

    def __contains__(self, item):
        return self._objects_with_id.__contains__(item)


class RegexExpressions:
    def __init__(self, regex_expressions):
        self._regex_expressions = DictOfIdObject(regex_expressions)

    def __iter__(self):
        return self._regex_expressions.__iter__()

    def __getitem__(self, item):
        return self._regex_expressions.__getitem__(item)

    def __contains__(self, item):
        return self._regex_expressions.__contains__(item)


class LineTypes(Enum):
    COMMENT = 1,
    MESSAGE_START = 2,
    MESSAGE_FIELD = 3,
    MESSAGE_END = 4


@dataclass
class Context:
    data_type_name: str


class ProcessEntryLine(ABC):
    @abstractmethod
    def comment(self, regex_result, constext: Context):
        pass

    @abstractmethod
    def data_type_start(self, regex_result, constext: Context):
        pass

    @abstractmethod
    def data_field(self, regex_result, constext: Context):
        pass

    @abstractmethod
    def data_type_end(self, regex_result, constext: Context):
        pass


class ParseFunctions:
    def __init__(self, process: ProcessEntryLine):
        self._process = process
        self._parse_functions = DictOfIdObject([
            ParseFunction(LineTypes.COMMENT, self._process.comment),
            ParseFunction(LineTypes.MESSAGE_START, self._process.data_type_start),
            ParseFunction(LineTypes.MESSAGE_FIELD, self._process.data_field),
            ParseFunction(LineTypes.MESSAGE_END, self._process.data_type_end)
        ])

    def __iter__(self):
        return self._parse_functions.__iter__()

    def __getitem__(self, item):
        return self._parse_functions.__getitem__(item)

    def __contains__(self, item):
        return self._parse_functions.__contains__(item)


class ProcessEntryLineC(ProcessEntryLine):

    def comment(self, regex_result, context: Context):
        print(f'/*{regex_result[0]} */')

    def data_type_start(self, regex_result, context: Context):
        context.data_type_name = regex_result[0]
        print('typedef struct {')

    def data_field(self, regex_result, context: Context):
        print(f'    {regex_result[0][1]} {regex_result[0][0]}')

    def data_type_end(self, regex_result, context: Context):
        print('} ', context.data_type_name, 'Msg;', sep='')


class ProcessEntryLinePascal(ProcessEntryLine):

    def comment(self, regex_result, context: Context):
        print(' {', regex_result[0], ' }', sep='')

    def data_type_start(self, regex_result, context: Context):
        context.data_type_name = regex_result[0]
        print(f'{regex_result[0]}Msg = packed record')

    def data_field(self, regex_result, context: Context):
        # Very simple naive solution
        type_str = regex_result[0][1]
        array_number_regex = re.findall(r'(\w+)\[(\d+)\]', type_str)
        if array_number_regex:
            type_str = array_number_regex[0][0]
            number = int(array_number_regex[0][1])
            type_str = f'array[{0}..{number-1}] of {type_str}'
        else:
            if type_str.lower() == 'int':
                type_str = 'LongInt'
        print(f'     {regex_result[0][0]}:    {type_str};')

    def data_type_end(self, regex_result, context: Context):
        print(f'end ;')


class RegexParser(Parser):

    def __init__(self, regex_expressions: RegexExpressions, parse_functions: ParseFunctions, context):
        self._regex_expressions = regex_expressions
        self._parse_functions = parse_functions
        self._context = context

    def parse_line(self, line):
        global data_type_name
        for line_type in self._regex_expressions:
            result = re.findall(self._regex_expressions[line_type].regex_str, line)
            if result:
                self._parse_functions[line_type].call(result, self._context)


class Languages(Enum):
    C = 1,
    PASCAL = 2


if __name__ == '__main__':
    with open('example.txt', 'r') as file_handler:
        lines = file_handler.readlines()
    data_type_name = ''

    regex_expressions = RegexExpressions([
        RegexExpression(LineTypes.COMMENT, r'#(.*)'),
        RegexExpression(LineTypes.MESSAGE_START, r'M\s+(\w+)\s*'),
        RegexExpression(LineTypes.MESSAGE_FIELD, r'F\s+(\w+)\s+([\w\[\]\d]+)'),
        RegexExpression(LineTypes.MESSAGE_END, r'E\s*')
    ])

    language = Languages.C

    if language == Languages.C:
        process = ProcessEntryLineC()
    elif language == Languages.PASCAL:
        process = ProcessEntryLinePascal()

    parse_functions = ParseFunctions(process)

    context = Context(data_type_name='')

    parser = RegexParser(regex_expressions=regex_expressions, parse_functions=parse_functions, context=context)

    for line in lines:
        parser.parse_line(line)
