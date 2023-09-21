# Cookiecutter template for an OSISM configuration repository

## Usage with Docker

Docker must be installed.

```
$ mkdir output
$ docker run --rm -v $(pwd)/output:/output -it quay.io/osism/cookiecutter 
```

## Usage without Docker

The `pwgen` tool must be installed.

```
$ virtualenv -p python3 .venv
$ source .venv/bin/activate
$ pip3 install -r https://raw.githubusercontent.com/osism/cfg-cookiecutter/main/requirements.txt
```

* http://cookiecutter.readthedocs.io/en/latest/

```
$ cookiecutter https://github.com/osism/cfg-cookiecutter.git
ceph_network_backend [192.168.80.0/20]:
[...]
```

Alternative:

```
$ git clone https://github.com/osism/cfg-cookiecutter.git
$ cd cookiecutter
$ cookiecutter .
ceph_network_backend [192.168.80.0/20]:
[...]
```

### User config

* https://cookiecutter.readthedocs.io/en/latest/advanced/user_config.html

In ``cookiecutter.yml.sample`` you can find a sample user config.

```
---
default_context:
  ceph_network_backend: 192.168.80.0/20
```

```
$ cookiecutter --config-file cookiecutter.yml https://github.com/osism/cfg-cookiecutter.git
ceph_network_backend [192.168.80.0/20]:
[...]
```

## Post-processing

* The password for Ansible Vault encrypted files, ist stored at ``secrets/vaultpass``.
* The password of the generated Keepass file is ``password``. This has to be changed.
* If a user config has been used, it can also be stored in the repository
* The contents in the generated ``configuration`` directory is stored in the repository.
  Be careful not to forget dotfiles like ``.gitignore``. The directory itself is not
  stored in the repository.

## Use of a stable release

This repository contains tags that were created at the time of a stable release.
These tags indicate the state of the repository that was tested at the time of a release.

An overview of all available stable releases can be found on https://release.osism.tech..

If a new configuration is to be created with the help of this repository and a stable
release is to be used, this must be explicitly stated when creating the configuration.

This is done via the parameter ``manager_version``. By default, this is always set to
``latest``. If, for example, the stable release ``4.2.0`` is to be used, the value for
this parameter is set to ``4.2.0``.

```
$ cookiecutter .
manager_version [latest]: 4.2.0
[...]
```

If the value for ``manager_version`` is set to a stable release, the values for
``ceph_version`` and ``openstack_version`` are ignored.

## Parameters

<table>
  <tr>
    <th>Parameter</th>
    <th>Description</th>
    <th>Default</th>
  </tr>
  <tr>
    <td><code>ceph_network_backend</code></td>
    <td>Address range for ceph's backend network</td>
    <td><code>192.168.80.0/20</code></td>
  </tr>
  <tr>
    <td><code>ceph_network_frontend</code></td>
    <td>Address range for ceph's frontend network</td>
    <td><code>192.168.64.0/20</code></td>
  </tr>
  <tr>
    <td><code>ceph_version</code></td>
    <td>The version of Ceph. When using a stable OSISM release (<code>manager_version != latest</code>), this value is ignored.</td>
    <td><code>quincy</code></td>
  </tr>
  <tr>
    <td><code>domain</code></td>
    <td>The Domain</td>
    <td><code>osism.xyz</code></td>
  </tr>
  <tr>
    <td><code>fqdn_external</code></td>
    <td>External API FQDN</td>
    <td><code>api.osism.xyz</code></td>
  </tr>
  <tr>
    <td><code>fqdn_internal</code></td>
    <td>Internal API FQDN</td>
    <td><code>api-int.osism.xyz</code></td>
  </tr>
  <tr>
    <td><code>git_host</code></td>
    <td>The address of the used Git server on which this repository will be stored later</td>
    <td><code>github.com</code></td>
  </tr>
  <tr>
    <td><code>git_port</code></td>
    <td>Port of the git repository</td>
    <td><code>22</code></td>
  </tr>
  <tr>
    <td><code>git_repository</code></td>
    <td>URI-Path to the git repository</td>
    <td><code>osism/cfg-cookiecutter</code></td>
  </tr>
  <tr>
    <td><code>git_username</code></td>
    <td>Username of the git repository</td>
    <td><code>git</code></td>
  </tr>
  <tr>
    <td><code>git_version</code></td>
    <td>Git Branch name</td>
    <td><code>main</code></td>
  </tr>
  <tr>
    <td><code>ip_external</code></td>
    <td>The external ip address of the API</td>
    <td><code>192.168.96.9</code></td>
  </tr>
  <tr>
    <td><code>ip_internal</code></td>
    <td>The internal ip address of the API</td>
    <td><code>192.168.32.9</code></td>
  </tr>
  <tr>
    <td><code>manager_version</code></td>
    <td>The version of OSISM. An overview of available OSISM releases can be found on <a href="https://release.osism.tech">release.osism.tech</a>.</td>
    <td><code>latest</code></td>
  </tr>
  <tr>
    <td><code>name_server</code></td>
    <td>Nameserver</td>
    <td><code>149.112.112.112</code></td>
  </tr>
  <tr>
    <td><code>ntp_server</code></td>
    <td>NTP server</td>
    <td><code>de.pool.ntp.org</code></td>
  </tr>
  <tr>
    <td><code>openstack_version</code></td>
    <td>The version of OpenStack. When using a stable OSISM release (<code>manager_version != latest</code>), this value is ignored.</td>
    <td><code>zed</code></td>
  </tr>
  <tr>
    <td><code>project_name</code></td>
    <td>Name of the configuration repository directory</td>
    <td><code>configuration</code></td>
  </tr>
  <tr>
    <td><code>with_ceph</code></td>
    <td>1 to use Ceph, 0 to not use Ceph</td>
    <td><code>1</code></td>
  </tr>
</table>
