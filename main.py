from dataclasses import dataclass
from enum import Enum
from regexexpressions import RegexExpressions, RegexExpression
from linetypes import LineTypes
from processentrylinec import ProcessEntryLineC
from processentrylinepascal import ProcessEntryLinePascal
from parsefunctions import ParseFunctions
from regexparser import RegexParser


@dataclass
class Context:
    data_type_name: str


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

    language = Languages.PASCAL

    if language == Languages.C:
        process = ProcessEntryLineC()
    elif language == Languages.PASCAL:
        process = ProcessEntryLinePascal()

    parse_functions = ParseFunctions(process)

    context = Context(data_type_name='')

    parser = RegexParser(regex_expressions=regex_expressions, parse_functions=parse_functions, context=context)

    for line in lines:
        parser.parse_line(line)
