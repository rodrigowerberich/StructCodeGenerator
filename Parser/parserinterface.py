from abc import ABC, abstractmethod


class Parser(ABC):
    @abstractmethod
    def parse_line(self, line):
        pass