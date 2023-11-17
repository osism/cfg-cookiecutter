#!/usr/bin/env python3

from pykeepass import PyKeePass
from ruamel.yaml import YAML

yaml = YAML()

with open("environments/secrets.yml") as fp:
    secrets = yaml.load(fp)

kp = PyKeePass("secrets/keepass.kdbx", password="password")

# FIXME(berendt): use attachments
kp.add_entry(
    kp.root_group,
    "SSH Keypair Configuration",
    username="",
    password=secrets.get("configuration_git_private_key"),
)
kp.add_entry(
    kp.root_group,
    "SSH Keypair Operator",
    username="",
    password=secrets.get("operator_private_key"),
)

try:
    with open("secrets/vaultpass") as fp:
        vaultpass = fp.read()

    kp.add_entry(kp.root_group, "Ansible Vault", username="", password=vaultpass)

# NOTE: If Ansible Vault is not used, the file does not exist.
except FileNotFoundError:
    pass

kp.add_entry(
    kp.root_group,
    "User - Operator",
    username="dragon",
    password=secrets.get("operator_password_unhashed"),
)
kp.add_entry(
    kp.root_group,
    "Keystone - Admin",
    username="admin",
    password=secrets.get("keystone_admin_password"),
)

kp.save()
