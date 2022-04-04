#!/usr/bin/env bash

python3 scripts/generate-secrets.py -p environments/kolla/secrets.yml.{{ cookiecutter.openstack_version }}
cp environments/kolla/secrets.yml.{{ cookiecutter.openstack_version }} environments/kolla/secrets.yml
