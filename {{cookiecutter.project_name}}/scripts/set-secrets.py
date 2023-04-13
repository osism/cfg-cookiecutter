#!/usr/bin/env python3

import random
import string

from oslo_utils import uuidutils
from passlib.hash import sha512_crypt
from ruamel.yaml import YAML

SECRETS_ALL = {"keystone_admin_password": "keystone_admin_password"}

SECRETSFILE_INPUT_KOLLA = "environments/kolla/secrets.yml"

SECRETSFILE_OUTPUT_ALL = "environments/secrets.yml"
SECRETSFILE_OUTPUT_CEPH = "environments/ceph/secrets.yml"
SECRETSFILE_OUTPUT_INFRASTRUCTURE = "environments/infrastructure/secrets.yml"
SECRETSFILE_OUTPUT_KOLLA = "environments/kolla/secrets.yml"
SECRETSFILE_OUTPUT_MANAGER = "environments/manager/secrets.yml"
SECRETSFILE_OUTPUT_MONITORING = "environments/monitoring/secrets.yml"

yaml = YAML()
yaml.explicit_start = True
yaml.indent(mapping=2, sequence=4, offset=2)
yaml.preserve_quotes = True
yaml.width = float("inf")

with open(SECRETSFILE_INPUT_KOLLA) as fp:
    secrets_input = yaml.load(fp)

with open(SECRETSFILE_OUTPUT_ALL) as fp:
    secrets_output_all = yaml.load(fp)

with open(SECRETSFILE_OUTPUT_CEPH) as fp:
    secrets_output_ceph = yaml.load(fp)

with open(SECRETSFILE_OUTPUT_INFRASTRUCTURE) as fp:
    secrets_output_infrastructure = yaml.load(fp)

with open(SECRETSFILE_OUTPUT_KOLLA) as fp:
    secrets_output_kolla = yaml.load(fp)

with open(SECRETSFILE_OUTPUT_MANAGER) as fp:
    secrets_output_manager = yaml.load(fp)

with open(SECRETSFILE_OUTPUT_MONITORING) as fp:
    secrets_output_monitoring = yaml.load(fp)

for key in SECRETS_ALL.keys():
    secrets_output_all[key] = secrets_input[SECRETS_ALL[key]]

if "ceph_cluster_fsid" in secrets_output_kolla:
    del secrets_output_kolla["ceph_cluster_fsid"]

secrets_output_all["ara_server_mariadb_password"] = "".join(
    [
        random.SystemRandom().choice(string.ascii_letters + string.digits)
        for n in range(16)
    ]
)
secrets_output_all["ara_password"] = "".join(
    [
        random.SystemRandom().choice(string.ascii_letters + string.digits)
        for n in range(16)
    ]
)

operator_password = "".join(
    [
        random.SystemRandom().choice(string.ascii_letters + string.digits)
        for n in range(16)
    ]
)
secrets_output_all["operator_password_unhashed"] = operator_password
secrets_output_all["operator_password"] = sha512_crypt.hash(operator_password)
secrets_output_all.yaml_add_eol_comment(operator_password, key="operator_password")

ceph_fsid = uuidutils.generate_uuid()
secrets_output_all["ceph_cluster_fsid"] = ceph_fsid
secrets_output_ceph["fsid"] = ceph_fsid

netbox_api_token = "".join(
    [random.SystemRandom().choice(string.digits) for n in range(40)]
)
secrets_output_manager["netbox_api_token"] = netbox_api_token
secrets_output_manager["manager_listener_broker_password"] = secrets_input["rabbitmq_password"]

secrets_output_infrastructure["netbox_user_api_token"] = netbox_api_token
secrets_output_infrastructure["netbox_secret_key"] = "".join(
    [
        random.SystemRandom().choice(string.ascii_letters + string.digits)
        for n in range(16)
    ]
)
secrets_output_infrastructure["netbox_superuser_api_token"] = "".join(
    [random.SystemRandom().choice(string.digits) for n in range(40)]
)
secrets_output_infrastructure["netbox_superuser_password"] = "".join(
    [
        random.SystemRandom().choice(string.ascii_letters + string.digits)
        for n in range(16)
    ]
)

secrets_output_monitoring["netdata_api_key"] = uuidutils.generate_uuid()

with open(SECRETSFILE_OUTPUT_ALL, "w+") as fp:
    yaml.dump(secrets_output_all, fp)

with open(SECRETSFILE_OUTPUT_CEPH, "w+") as fp:
    yaml.dump(secrets_output_ceph, fp)

with open(SECRETSFILE_OUTPUT_INFRASTRUCTURE, "w+") as fp:
    yaml.dump(secrets_output_infrastructure, fp)

with open(SECRETSFILE_OUTPUT_KOLLA, "w+") as fp:
    yaml.dump(secrets_output_kolla, fp)

with open(SECRETSFILE_OUTPUT_MANAGER, "w+") as fp:
    yaml.dump(secrets_output_manager, fp)

with open(SECRETSFILE_OUTPUT_MONITORING, "w+") as fp:
    yaml.dump(secrets_output_monitoring, fp)
