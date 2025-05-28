from dataclasses import dataclass, field
from typing import List, Dict, Optional

@dataclass
class Trigger:
    event: str               # e.g. 'push', 'pull_request', 'schedule'
    config: Dict             # raw trigger config (branches, cron, etc.)

@dataclass
class Step:
    name: Optional[str] = None
    run: Optional[str] = None
    uses: Optional[str] = None
    with_args: Dict = field(default_factory=dict)

@dataclass
class Job:
    name: str
    runs_on: str
    steps: List[Step] = field(default_factory=list)
    triggers: List[Trigger] = field(default_factory=list)
    condition: Optional[str] = None   # GitHub's job-level `if:`
    variables: Dict = field(default_factory=dict)

@dataclass
class Pipeline:
    name: Optional[str]
    variables: Dict = field(default_factory=dict)
    jobs: List[Job] = field(default_factory=list)