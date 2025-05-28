from abc import ABC, abstractmethod
from ci_converter.core.ir import Pipeline

class Parser(ABC):
    @abstractmethod
    def parse(self, filepath: str) -> Pipeline:
        """Load a file and return a Pipeline IR object."""
        pass