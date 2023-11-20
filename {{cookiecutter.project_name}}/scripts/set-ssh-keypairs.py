#!/usr/bin/env python3

from loguru import logger
from ruamel.yaml import YAML

PRIVATE_KEYS = {
    "operator": "operator_private_key",
    "configuration": "configuration_git_private_key",
}

SECRETSFILE = "environments/secrets.yml"
CONFIGURATIONFILE = "environments/configuration.yml"
CONFIGURATIONFILE_MANAGER = "environments/manager/configuration.yml"

yaml = YAML()
yaml.explicit_start = True
yaml.indent(mapping=2, sequence=4, offset=2)
yaml.preserve_quotes = True
yaml.width = float("inf")

# set private keys

logger.info(f"Prepare use of {SECRETSFILE}")
with open(SECRETSFILE) as fp:
    secrets = yaml.load(fp)

for key in PRIVATE_KEYS.keys():
    logger.info(f"Prepare use of secrets/id_rsa.{key}")
    with open(f"secrets/id_rsa.{key}", "r") as fp:
        data = fp.read()

    logger.info(f"Set {key}")
    secrets[PRIVATE_KEYS[key]] = data

logger.info(f"Write result to {SECRETSFILE}")
with open(SECRETSFILE, "w+") as fp:
    yaml.dump(secrets, fp)

# set public keys

logger.info(f"Prepare use of {CONFIGURATIONFILE}")
with open(CONFIGURATIONFILE) as fp:
    configuration = yaml.load(fp)

logger.info(f"Prepare use of {CONFIGURATIONFILE_MANAGER}")
with open(CONFIGURATIONFILE_MANAGER) as fp:
    configuration_manager = yaml.load(fp)

# set operator public key

with open("secrets/id_rsa.operator.pub", "r") as fp:
    data = fp.read()
    data = data.rstrip()

logger.info("Set operator_public_key")
configuration["operator_public_key"] = data

# set configuration public key

with open("secrets/id_rsa.configuration.pub", "r") as fp:
    data = fp.read()
    data = data.rstrip()

logger.info("Set configuration_git_public_key")
configuration_manager["configuration_git_public_key"] = data

# write configurations

logger.info(f"Write result to {CONFIGURATIONFILE}")
with open(CONFIGURATIONFILE, "w+") as fp:
    yaml.dump(configuration, fp)

logger.info(f"Write result to {CONFIGURATIONFILE_MANAGER}")
with open(CONFIGURATIONFILE_MANAGER, "w+") as fp:
    yaml.dump(configuration_manager, fp)
