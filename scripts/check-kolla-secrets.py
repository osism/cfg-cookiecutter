#!/usr/bin/env python3

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import subprocess
import sys

import yaml

# Keys that are intentionally left blank
BLANK_KEYS = [
    "docker_registry_password",
]

# Keys that contain nested sub-keys (private_key / public_key)
SSH_KEYS = [
    "bifrost_ssh_key",
    "haproxy_ssh_key",
    "keystone_ssh_key",
    "kolla_ssh_key",
    "neutron_ssh_key",
    "nova_ssh_key",
    "octavia_amp_ssh_key",
]


def main():
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <project-directory>")
        sys.exit(1)

    project_dir = sys.argv[1]
    secrets_file = f"{project_dir}/environments/kolla/secrets.yml"
    vault_pass_file = f"{project_dir}/secrets/vaultpass"

    result = subprocess.run(
        [
            "ansible-vault",
            "view",
            "--vault-password-file",
            vault_pass_file,
            secrets_file,
        ],
        capture_output=True,
        text=True,
    )

    if result.returncode != 0:
        print(f"ERROR: Failed to decrypt {secrets_file}")
        print(result.stderr)
        sys.exit(1)

    secrets = yaml.safe_load(result.stdout)

    if not secrets:
        print("ERROR: secrets.yml is empty")
        sys.exit(1)

    errors = []

    for key, value in secrets.items():
        if key in BLANK_KEYS:
            print(f"  SKIP {key} (intentionally blank)")
            continue

        if key in SSH_KEYS:
            if not isinstance(value, dict):
                errors.append(
                    f"{key}: expected dict with private_key/public_key, got {type(value).__name__}"
                )
                print(f"  FAIL {key}")
                continue
            if not value.get("private_key"):
                errors.append(f"{key}.private_key: not set")
                print(f"  FAIL {key}.private_key")
            else:
                print(f"  OK   {key}.private_key")
            if not value.get("public_key"):
                errors.append(f"{key}.public_key: not set")
                print(f"  FAIL {key}.public_key")
            else:
                print(f"  OK   {key}.public_key")
        elif value is None or value == "":
            errors.append(f"{key}: not set")
            print(f"  FAIL {key}")
        else:
            print(f"  OK   {key}")

    print()

    if errors:
        print(
            "ERROR: The following secrets in environments/kolla/secrets.yml are not set:\n"
        )
        for error in errors:
            print(f"  - {error}")
        sys.exit(1)

    print(f"OK: All {len(secrets)} secrets in environments/kolla/secrets.yml are set.")


if __name__ == "__main__":
    main()
