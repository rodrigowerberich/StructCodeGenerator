from abc import ABC, abstractmethod
from Parser.parseresultinterface import ParseResult


class ProcessEntryLine(ABC):
    @abstractmethod
    def comment(self, regex_result: ParseResult, context):
        pass

    @abstractmethod
    def data_type_start(self, regex_result: ParseResult, context):
        pass

    @abstractmethod
    def data_field(self, regex_result: ParseResult, context):
        pass

    @abstractmethod
    def data_type_end(self, regex_result: ParseResult, context):
        pass
