from dataclasses import dataclass, field
from typing import List, Dict

@dataclass
class Trigger:
    event: str       
    config: Dict

@dataclass
class Step:
    name: str
    run: str = None
    uses: str = None
    with_args: Dict = field(default_factory=dict)

@dataclass
class Job:
    name: str
    runs_on: str
    steps: List[Step] = field(default_factory=list)
    variables: Dict = field(default_factory=dict)
    triggers: List[Trigger] = field(default_factory=list)

@dataclass
class Pipeline:
    name: str
    variables: Dict = field(default_factory=dict)
    jobs: List[Job] = field(default_factory=list)
