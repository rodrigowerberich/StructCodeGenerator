import typing
from dataclasses import dataclass
from dictofidobject import DictOfIdObject
from linetypes import LineTypes
from processentryline import ProcessEntryLine


@dataclass
class ParseFunction:
    id: typing.Any
    call: typing.Any


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