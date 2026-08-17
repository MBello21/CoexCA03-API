FROM mcr.microsoft.com/devcontainers/python:3.14

ENV PYTHONUNBUFFERED=1

RUN apt-get update && export DEBIAN_FRONTEND=nointeractive\
    && apt-get -y install --no-install-recommends postgresql-client\
    && apt-get clean && rm -rf /var/lib/apt/lists/*

RUN pip install --no-cache-dir pipenv