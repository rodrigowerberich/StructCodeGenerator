from dataclasses import dataclass
import typing
from dictofidobject import DictOfIdObject


@dataclass
class RegexExpression:
    id: typing.Any
    regex_str: str


class RegexExpressions:
    def __init__(self, regex_expressions):
        self._regex_expressions = DictOfIdObject(regex_expressions)

    def __iter__(self):
        return self._regex_expressions.__iter__()

    def __getitem__(self, item):
        return self._regex_expressions.__getitem__(item)

    def __contains__(self, item):
        return self._regex_expressions.__contains__(item)