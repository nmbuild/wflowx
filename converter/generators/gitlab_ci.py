import yaml
from ci_converter.generators.base import Generator
from ci_converter.core.registry import register_generator

class GitLabCI(Generator):
    def generate(self, pipeline) -> str:
        out = {}
        for job in pipeline.jobs:
            # emit each step-name as an echo in script
            out[job.name] = {
                'script': [f'echo "{step.name}"' for step in job.steps]
            }
        return yaml.dump(out, sort_keys=False)

# register under key 'gitlab'
register_generator('gitlab', GitLabCI())
