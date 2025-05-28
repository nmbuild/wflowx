import yaml
from .base import Generator

class GitLabCI(Generator):
    def generate(self, pipeline):
        out = {'stages': [j.name for j in pipeline.jobs]}
        # map pipeline.jobs → jobs entries, triggers → rules, steps → script
        return yaml.dump(out)