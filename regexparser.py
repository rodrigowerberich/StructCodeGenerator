from parseresultinterface import ParseResult
from parserinterface import Parser
from regexexpressions import RegexExpressions
from parsefunctions import ParseFunctions
import re


class RegexParseResult(ParseResult):
    def is_valid(self) -> bool:
        return True if self._result else False

    def __init__(self, original_content: str, result):
        self._original_content = original_content
        self._result = result

    def original_content(self) -> str:
        return self._original_content

    def parts(self) -> list:
        if self.is_valid():
            parts = self._result[0]
            if type(parts) is str:
                return [parts]
            else:
                return parts
        else:
            return []


class RegexFinder:
    @staticmethod
    def find(regex_expression, string):
        result = re.findall(regex_expression, string)
        return RegexParseResult(string, result)


class RegexParser(Parser):

    def __init__(self, regex_expressions: RegexExpressions, parse_functions: ParseFunctions, context):
        self._regex_expressions = regex_expressions
        self._parse_functions = parse_functions
        self._context = context

    def parse_line(self, line):
        for line_type in self._regex_expressions:
            result = RegexFinder.find(self._regex_expressions[line_type].regex_str, line)
            if result.is_valid():
                self._parse_functions[line_type].call(result, self._context)
