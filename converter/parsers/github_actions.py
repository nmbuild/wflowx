import yaml
from ci_converter.parsers.base import Parser
from ci_converter.core.ir import Pipeline, Job, Step
from ci_converter.core.registry import register_parser

class GitHubActionsParser(Parser):
    def parse(self, filepath: str) -> Pipeline:
        data = yaml.safe_load(open(filepath))
        jobs = []
        for job_name, cfg in data.get('jobs', {}).items():
            steps = []
            for s in cfg.get('steps', []):
                # only grab the 'name' field
                if 'name' in s:
                    steps.append(Step(name=s['name']))
            jobs.append(Job(name=job_name, steps=steps))
        return Pipeline(jobs=jobs)

# register under key 'github'
register_parser('github', GitHubActionsParser())
