from abc import ABC, abstractmethod
from ci_converter.core.ir import Pipeline

class Generator(ABC):
    @abstractmethod
    def generate(self, pipeline: Pipeline) -> str:
        """Emit a string representing the target config."""
        pass