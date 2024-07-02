#!/usr/bin/env python3

import random
import string

from loguru import logger
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

CONFIGURATIONFILE_OUTPUT_ALL = "environments/configuration.yml"
CONFIGURATIONFILE_OUTPUT_CEPH = "environments/ceph/configuration.yml"
CONFIGURATIONFILE_OUTPUT_KOLLA = "environments/kolla/configuration.yml"

yaml = YAML()
yaml.explicit_start = True
yaml.indent(mapping=2, sequence=4, offset=2)
yaml.preserve_quotes = True
yaml.width = float("inf")

logger.info(f"Prepare use of {SECRETSFILE_INPUT_KOLLA}")
with open(SECRETSFILE_INPUT_KOLLA) as fp:
    secrets_input = yaml.load(fp)

logger.info(f"Prepare use of {SECRETSFILE_OUTPUT_ALL}")
with open(SECRETSFILE_OUTPUT_ALL) as fp:
    secrets_output_all = yaml.load(fp)

logger.info(f"Prepare use of {SECRETSFILE_OUTPUT_CEPH}")
with open(SECRETSFILE_OUTPUT_CEPH) as fp:
    secrets_output_ceph = yaml.load(fp)

logger.info(f"Prepare use of {SECRETSFILE_OUTPUT_INFRASTRUCTURE}")
with open(SECRETSFILE_OUTPUT_INFRASTRUCTURE) as fp:
    secrets_output_infrastructure = yaml.load(fp)

logger.info(f"Prepare use of {SECRETSFILE_OUTPUT_KOLLA}")
with open(SECRETSFILE_OUTPUT_KOLLA) as fp:
    secrets_output_kolla = yaml.load(fp)

logger.info(f"Prepare use of {SECRETSFILE_OUTPUT_MANAGER}")
with open(SECRETSFILE_OUTPUT_MANAGER) as fp:
    secrets_output_manager = yaml.load(fp)

logger.info(f"Prepare use of {SECRETSFILE_OUTPUT_MONITORING}")
with open(SECRETSFILE_OUTPUT_MONITORING) as fp:
    secrets_output_monitoring = yaml.load(fp)

logger.info(f"Prepare use of {CONFIGURATIONFILE_OUTPUT_ALL}")
with open(CONFIGURATIONFILE_OUTPUT_ALL) as fp:
    configuration_output_all = yaml.load(fp)

logger.info(f"Prepare use of {CONFIGURATIONFILE_OUTPUT_CEPH}")
with open(CONFIGURATIONFILE_OUTPUT_CEPH) as fp:
    configuration_output_ceph = yaml.load(fp)

logger.info(f"Prepare use of {CONFIGURATIONFILE_OUTPUT_KOLLA}")
with open(CONFIGURATIONFILE_OUTPUT_KOLLA) as fp:
    configuration_output_kolla = yaml.load(fp)

for key in SECRETS_ALL.keys():
    logger.info(f"Set {key}")
    secrets_output_all[key] = secrets_input[SECRETS_ALL[key]]

if "ceph_cluster_fsid" in secrets_output_kolla:
    del secrets_output_kolla["ceph_cluster_fsid"]

logger.info("Set ara_server_mariadb_password")
secrets_output_all["ara_server_mariadb_password"] = "".join(
    [
        random.SystemRandom().choice(string.ascii_letters + string.digits)
        for n in range(16)
    ]
)
logger.info("Set ara_password")
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
logger.info("Set operator_password_unhashed")
secrets_output_all["operator_password_unhashed"] = operator_password
logger.info("Set operator_password")
secrets_output_all["operator_password"] = sha512_crypt.hash(operator_password)
secrets_output_all.yaml_add_eol_comment(operator_password, key="operator_password")

ceph_fsid = uuidutils.generate_uuid()
logger.info("Set ceph_cluster_fsid")
configuration_output_all["ceph_cluster_fsid"] = ceph_fsid
logger.info("Set fsid")
configuration_output_ceph["fsid"] = ceph_fsid

k3s_token = "".join([random.SystemRandom().choice(string.digits) for n in range(32)])
logger.info("Set k3s_token")
secrets_output_manager["k3s_token"] = k3s_token

netbox_api_token = "".join(
    [random.SystemRandom().choice(string.digits) for n in range(40)]
)
logger.info("Set netbox_api_token")
secrets_output_manager["netbox_api_token"] = netbox_api_token
logger.info("Set manager_listener_broker_password")
secrets_output_manager["manager_listener_broker_password"] = secrets_input[
    "rabbitmq_password"
]

logger.info("Set netbox_user_api_token")
secrets_output_infrastructure["netbox_user_api_token"] = netbox_api_token
logger.info("Set netbox_secret_key")
secrets_output_infrastructure["netbox_secret_key"] = "".join(
    [
        random.SystemRandom().choice(string.ascii_letters + string.digits)
        for n in range(50)
    ]
)
logger.info("Set netbox_superuser_api_token")
secrets_output_infrastructure["netbox_superuser_api_token"] = "".join(
    [random.SystemRandom().choice(string.digits) for n in range(40)]
)
logger.info("Set netbox_superuser_password")
secrets_output_infrastructure["netbox_superuser_password"] = "".join(
    [
        random.SystemRandom().choice(string.ascii_letters + string.digits)
        for n in range(16)
    ]
)

logger.info("Set netdata_api_key")
secrets_output_monitoring["netdata_api_key"] = uuidutils.generate_uuid()

logger.info("Set ceph_rgw_keystone_password")
secrets_output_ceph["ceph_rgw_keystone_password"] = secrets_output_kolla[
    "ceph_rgw_keystone_password"
]

logger.info("Set ceph_dashboard_password")
secrets_output_ceph["ceph_dashboard_password"] = "".join(
    [
        random.SystemRandom().choice(string.ascii_letters + string.digits)
        for n in range(16)
    ]
)

logger.info(f"Write result to {SECRETSFILE_OUTPUT_ALL}")
with open(SECRETSFILE_OUTPUT_ALL, "w+") as fp:
    yaml.dump(secrets_output_all, fp)

logger.info(f"Write result to {SECRETSFILE_OUTPUT_CEPH}")
with open(SECRETSFILE_OUTPUT_CEPH, "w+") as fp:
    yaml.dump(secrets_output_ceph, fp)

logger.info(f"Write result to {SECRETSFILE_OUTPUT_INFRASTRUCTURE}")
with open(SECRETSFILE_OUTPUT_INFRASTRUCTURE, "w+") as fp:
    yaml.dump(secrets_output_infrastructure, fp)

logger.info(f"Write result to {SECRETSFILE_OUTPUT_KOLLA}")
with open(SECRETSFILE_OUTPUT_KOLLA, "w+") as fp:
    yaml.dump(secrets_output_kolla, fp)

logger.info(f"Write result to {SECRETSFILE_OUTPUT_MANAGER}")
with open(SECRETSFILE_OUTPUT_MANAGER, "w+") as fp:
    yaml.dump(secrets_output_manager, fp)

logger.info(f"Write result to {SECRETSFILE_OUTPUT_MONITORING}")
with open(SECRETSFILE_OUTPUT_MONITORING, "w+") as fp:
    yaml.dump(secrets_output_monitoring, fp)

logger.info(f"Write result to {CONFIGURATIONFILE_OUTPUT_ALL}")
with open(CONFIGURATIONFILE_OUTPUT_ALL, "w+") as fp:
    yaml.dump(configuration_output_all, fp)

logger.info(f"Write result to {CONFIGURATIONFILE_OUTPUT_CEPH}")
with open(CONFIGURATIONFILE_OUTPUT_CEPH, "w+") as fp:
    yaml.dump(configuration_output_ceph, fp)

logger.info(f"Write result to {CONFIGURATIONFILE_OUTPUT_KOLLA}")
with open(CONFIGURATIONFILE_OUTPUT_KOLLA, "w+") as fp:
    yaml.dump(configuration_output_kolla, fp)
