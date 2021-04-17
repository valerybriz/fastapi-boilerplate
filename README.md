# Fastapi Boiler plate
(based on the [Fastapi Coockie cutter](https://github.com/tiangolo/full-stack-fastapi-postgresql)

[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)](https://github.com/pre-commit/pre-commit)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)


for more info about endpoints usage: check /docs when all is mounted.

## Pre-requisites for local execution

> > 1. create a python virtualenv and install dependencies using ```poetry install```
>
> > 2. create .env file in root with your own credentials, use .env_sample as a guide
>
> > 3. ```pre-commit install```
> 
> > 4. start the ASGI server implementation```uvicorn app.main:app --reload --port 8000```

