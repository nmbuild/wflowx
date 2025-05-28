#!/usr/bin/env python3
"""
GitHub Actions → GitLab CI Converter CLI

Usage:
  python gh_to_gl_ci.py -i path/to/.github/workflows/ci.yml -o path/to/.gitlab-ci.yml

Dependencies:
  pip install pyyaml
"""

import yaml
import argparse


def load_yaml(path):
    with open(path, 'r') as f:
        return yaml.safe_load(f)


def convert_variables(gh):
    return gh.get('env', {})


def convert_triggers(on):
    rules = []
    if not on:
        return []
    # push
    push = on.get('push', {})
    for branch in push.get('branches', []):
        rules.append({ 'if': f'$CI_COMMIT_REF_NAME == "{branch}"' })

    # pull_request
    if 'pull_request' in on:
        rules.append({ 'if': '$CI_MERGE_REQUEST_IID' })

    # schedule
    for sch in on.get('schedule', []):
        cron = sch.get('cron')
        if cron:
            rules.append({ 'when': 'always', 'cron': cron })
    return rules


def map_runner(runner):
    mapping = {
        'ubuntu-latest': 'ubuntu:latest',
        'ubuntu-22.04': 'ubuntu:22.04',
        'windows-latest': 'mcr.microsoft.com/windows:latest'
    }
    return mapping.get(runner, runner)


def convert_steps(steps):
    script = []
    for s in steps:
        if s.get('uses', '').startswith('actions/checkout'):
            continue
        if 'run' in s:
            script.append(s['run'])
        elif 'uses' in s:
            script.append(f'# TODO: handle action {s["uses"]}')
    return script


def convert_jobs(gh):
    jobs = {}
    stages = []
    on = gh.get('on', {})

    for name, job in gh.get('jobs', {}).items():
        stages.append(name)
        job_rules = convert_triggers(on)
        job_cfg = {
            'stage': name,
            'image': map_runner(job.get('runs-on')),
            **({'rules': job_rules} if job_rules else {}),
            'script': convert_steps(job.get('steps', []))
        }
        jobs[name] = job_cfg

    return stages, jobs


def main():
    parser = argparse.ArgumentParser(description='Convert GitHub Actions YAML to GitLab CI YAML')
    parser.add_argument('-i', '--input', required=True, help='GitHub Actions workflow file')
    parser.add_argument('-o', '--output', required=True, help='Output GitLab CI YAML file')
    args = parser.parse_args()

    gh = load_yaml(args.input)
    variables = convert_variables(gh)
    stages, jobs = convert_jobs(gh)

    gl = {}
    if variables:
        gl['variables'] = variables
    gl['stages'] = stages
    gl.update(jobs)

    with open(args.output, 'w') as f:
        yaml.dump(gl, f, sort_keys=False)

    print(f"Generated GitLab CI file at {args.output}")


if __name__ == '__main__':
    main()
