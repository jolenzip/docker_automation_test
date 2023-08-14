[![Repo Status](https://github.com/jolenzip/docker_automation_test/actions/workflows/main.yml/badge.svg)](https://github.com/jolenzip/docker_automation_test/actions/workflows/main.yml)
[![Py-Tests](https://github.com/jolenzip/docker_automation_test/actions/workflows/python-package-conda.yml/badge.svg)](https://github.com/jolenzip/docker_automation_test/actions/workflows/python-package-conda.yml)

# docker_automation_test

following the steps from https://docs.github.com/en/actions/creating-actions/creating-a-docker-container-action

This action prints "Hello World" or "Hello" + the name of a person to greet to the log.

## Inputs

## `who-to-greet`

**Required** The name of the person to greet. Default `"World"`.

## Outputs

## `time`

The time we greeted you.

## Example usage

uses: actions/hello-world-docker-action@v2
with:
  who-to-greet: 'Mona the Octocat'
