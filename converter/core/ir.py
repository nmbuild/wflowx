from dataclasses import dataclass
from typing import List

@dataclass
class Step:
    name: str

@dataclass
class Job:
    name: str
    steps: List[Step]

@dataclass
class Pipeline:
    jobs: List[Job]
