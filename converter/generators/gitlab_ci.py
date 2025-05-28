import yaml
from ci_converter.generators.base import Generator
from ci_converter.core.registry import register_generator

class GitLabCI(Generator):
    def generate(self, pipeline) -> str:
        out = {}
        if pipeline.variables:
            out['variables'] = pipeline.variables

        # stages in order
        out['stages'] = [job.name for job in pipeline.jobs]

        for job in pipeline.jobs:
            rules = []
            for trig in job.triggers:
                if trig.event == 'push':
                    rules.append({'if': f'$CI_COMMIT_REF_NAME == "{trig.config["branch"]}"'})
                elif trig.event == 'pull_request':
                    rules.append({'if': '$CI_MERGE_REQUEST_IID'})
                elif trig.event == 'schedule':
                    rules.append({'when': 'always', 'cron': trig.config.get('cron')})
            if job.condition:
                rules.append({'if': job.condition})

            script_lines = []
            for step in job.steps:
                if step.uses and step.uses.startswith('actions/checkout'):
                    continue
                if step.run:
                    script_lines.append(step.run)
                elif step.uses:
                    script_lines.append(f'# TODO: action {step.uses}')

            out[job.name] = {
                'stage': job.name,
                'image': job.runs_on.replace('ubuntu-latest', 'ubuntu:latest'),
                **({'rules': rules} if rules else {}),
                'script': script_lines
            }

        return yaml.dump(out, sort_keys=False)

# register under key 'gitlab'
register_generator('gitlab', GitLabCI())