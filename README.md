# Cookiecutter template for an OSISM configuration repository

## Installation

The `pwgen` tool must be installed.

### Virtualenv

```
$ virtualenv -p python3 .venv
$ source .venv/bin/activate
$ pip3 install -r requirements.txt
```


## Usage

* http://cookiecutter.readthedocs.io/en/latest/

```
$ cookiecutter ssh://git@github.com:osism/cfg-cookiecutter.git
ceph_fsid [00000000-0000-0000-0000-000000000000]:
ceph_network_backend [192.168.80.0/20]:
[...]
```

Alternative:

```
$ git clone ssh://git@github.com:osism/cfg-cookiecutter.git
$ cd cookiecutter
$ cookiecutter .
ceph_fsid [00000000-0000-0000-0000-000000000000]:
ceph_network_backend [192.168.80.0/20]:
[...]
```

### User config

* https://cookiecutter.readthedocs.io/en/latest/advanced/user_config.html

In ``cookiecutter.yml.sample`` you can find a sample user config.

```
---
default_context:
  ceph_fsid: 00000000-0000-0000-0000-000000000000
```

```
$ cookiecutter --config-file cookiecutter.yml ssh://git@github.com:osism/cfg-cookiecutter.git
ceph_fsid [00000000-0000-0000-0000-000000000000]:
ceph_network_backend [192.168.80.0/20]:
[...]
```

## Post-processing

* The password for Ansible Vault encrypted files, ist stored at ``secrets/vaultpass``.
* The password of the generated Keepass file is ``password``. This should be changed.
* If a user config has been used, it can also be stored in the repository
* The contents in the generated ``cfg-customer`` directory is stored in the repository.
  Be careful not to forget dotfiles like ``.gitignore``. The directory itself is not
  stored in the repository.

## Parameters

<table>
  <tr>
    <th>Parameter</th>
    <th>Description</th>
    <th>Default</th>
  </tr>
  <tr>
    <td><code>ceph_fsid</code></td>
    <td>The UUID for the Ceph cluster, passed to ceph-ansible</td>
    <td></td>
  </tr>
  <tr>
    <td><code>docker_version</code></td>
    <td>The version of the Docker service. This <code>5:</code> must be prepended starting with version 18.09.</td>
    <td><code>5:19.03.13</code></td>
  </tr>
  <tr>
    <td><code>git_host</code></td>
    <td>The address of the used Git server on which this repository will be stored later</td>
    <td><code>github.com</code></td>
  </tr>
  <tr>
    <td><code>manager_version</code></td>
    <td>The version of the osism-ansible container</td>
    <td><code>latest</code></td>
  </tr>
  <tr>
    <td></td>
    <td></td>
    <td></td>
  </tr>
</table>
