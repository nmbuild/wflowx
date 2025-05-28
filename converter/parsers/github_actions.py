import yaml
from ci_converter.parsers.base import Parser
from ci_converter.core.ir import Pipeline, Job, Step, Trigger
from ci_converter.core.registry import register_parser

class GitHubActionsParser(Parser):
    def parse(self, filepath: str) -> Pipeline:
        data = yaml.safe_load(open(filepath))
        pipeline = Pipeline(name=data.get('name'))
        # top‑level env
        pipeline.variables = data.get('env', {})

        # extract triggers for reuse
        on_cfg = data.get('on', {})
        shared_triggers = []
        # push
        push = on_cfg.get('push', {})
        for branch in push.get('branches', []):
            shared_triggers.append(Trigger('push', {'branch': branch}))
        # pull_request
        if 'pull_request' in on_cfg:
            shared_triggers.append(Trigger('pull_request', {}))
        # schedule
        for sch in on_cfg.get('schedule', []):
            shared_triggers.append(Trigger('schedule', sch))

        # jobs
        for job_name, job_cfg in data.get('jobs', {}).items():
            job = Job(
                name=job_name,
                runs_on=job_cfg.get('runs-on'),
                triggers=list(shared_triggers),
                condition=job_cfg.get('if'),
                variables=job_cfg.get('env', {})
            )
            # steps
            for s in job_cfg.get('steps', []):
                step = Step(
                    name=s.get('name'),
                    run=s.get('run'),
                    uses=s.get('uses'),
                    with_args=s.get('with', {})
                )
                job.steps.append(step)

            pipeline.jobs.append(job)
        return pipeline

# register under key 'github'
register_parser('github', GitHubActionsParser())