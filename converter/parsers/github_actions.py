import yaml
from .base import Parser
from ci_converter.core.ir import Pipeline, Job, Step, Trigger

class GitHubActionsParser(Parser):
    def parse(self, filepath):
        data = yaml.safe_load(open(filepath))
        pipeline = Pipeline(name=data.get('name','GH-CI'))
        # env → pipeline.variables...
        # on → pipeline.jobs[].triggers...
        # jobs → for each job: Job(...), steps → Step(...)
        return pipeline

from ci_converter.core.registry import register_parser
register_parser('github', GitHubActionsParser)