from dataclasses import dataclass
from enum import Enum

from CPP.processentrylinecpp import ProcessEntryLineCpp
from RegexParser.regexexpressions import RegexExpressions, RegexExpression
from Parser.linetypes import LineTypes
from C.processentrylinec import ProcessEntryLineC
from Pascal.processentrylinepascal import ProcessEntryLinePascal
from Parser.parsefunctions import ParseFunctions
from RegexParser.regexparser import RegexParser


@dataclass
class Context:
    data_type_name: str


class Languages(Enum):
    C = 1,
    CPP = 2,
    PASCAL = 3


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

    # Select the output language
    language = Languages.CPP

    if language == Languages.C:
        process = ProcessEntryLineC()
    elif language == Languages.CPP:
        process = ProcessEntryLineCpp()
    elif language == Languages.PASCAL:
        process = ProcessEntryLinePascal()

    parse_functions = ParseFunctions(process)

    context = Context(data_type_name='')

    parser = RegexParser(regex_expressions=regex_expressions, parse_functions=parse_functions, context=context)

    for line in lines:
        parser.parse_line(line)
