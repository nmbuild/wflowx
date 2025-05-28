from abc import ABC, abstractmethod
from ci_converter.core.ir import Pipeline

class Generator(ABC):
    @abstractmethod
    def generate(self, pipeline: Pipeline) -> str:
        \"\"\"Return generated text (YAML or DSL).\"\"\"
        pass