from abc import ABC, abstractmethod


class ParseResult(ABC):
    @abstractmethod
    def original_content(self) -> str:
        pass

    @abstractmethod
    def parts(self) -> list:
        pass

    @abstractmethod
    def is_valid(self) -> bool:
        pass