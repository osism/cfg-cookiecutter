#!/usr/bin/env python3

import random
import string

from passlib.hash import sha512_crypt
from ruamel.yaml import YAML

SECRETS_ALL = {
    'keystone_admin_password': 'keystone_admin_password'
}

SECRETSFILE_INPUT = 'environments/kolla/secrets.yml'
SECRETSFILE_OUTPUT_ALL = 'environments/secrets.yml'
SECRETSFILE_OUTPUT_KOLLA = 'environments/kolla/secrets.yml'

yaml = YAML()
yaml.explicit_start = True
yaml.indent(mapping=2, sequence=4, offset=2)
yaml.preserve_quotes = True
yaml.width = float("inf")

with open(SECRETSFILE_INPUT) as fp:
    secrets_input = yaml.load(fp)

with open(SECRETSFILE_OUTPUT_ALL) as fp:
    secrets_output_all = yaml.load(fp)

with open(SECRETSFILE_OUTPUT_KOLLA) as fp:
    secrets_output_kolla = yaml.load(fp)

for key in SECRETS_ALL.keys():
    secrets_output_all[key] = secrets_input[SECRETS_ALL[key]]

if 'ceph_cluster_fsid' in secrets_output_kolla:
    del secrets_output_kolla['ceph_cluster_fsid']

secrets_output_all['ara_server_mariadb_password'] = ''.join([
    random.SystemRandom().choice(
        string.ascii_letters + string.digits)
    for n in range(16)
])
secrets_output_all['ara_password'] = ''.join([
    random.SystemRandom().choice(
        string.ascii_letters + string.digits)
    for n in range(16)
])

operator_password = ''.join([
    random.SystemRandom().choice(
        string.ascii_letters + string.digits)
    for n in range(16)
])
secrets_output_all['operator_password_unhashed'] = operator_password
secrets_output_all['operator_password'] = sha512_crypt.hash(operator_password)
secrets_output_all.yaml_add_eol_comment(operator_password,
                                        key='operator_password')

with open(SECRETSFILE_OUTPUT_ALL, 'w+') as fp:
    yaml.dump(secrets_output_all, fp)

with open(SECRETSFILE_OUTPUT_KOLLA, 'w+') as fp:
    yaml.dump(secrets_output_kolla, fp)
