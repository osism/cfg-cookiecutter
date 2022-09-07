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
ceph_fsid [00000000-0000-0000-0000-000000000000]:
ceph_network_backend [192.168.80.0/20]:
[...]
```

Alternative:

```
$ git clone https://github.com/osism/cfg-cookiecutter.git
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
$ cookiecutter --config-file cookiecutter.yml https://github.com/osism/cfg-cookiecutter.git
ceph_fsid [00000000-0000-0000-0000-000000000000]:
ceph_network_backend [192.168.80.0/20]:
[...]
```

## Post-processing

* The password for Ansible Vault encrypted files, ist stored at ``secrets/vaultpass``.
* The password of the generated Keepass file is ``password``. This has to be changed.
* If a user config has been used, it can also be stored in the repository
* The contents in the generated ``customer`` directory is stored in the repository.
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
    <td><code>00000000-0000-0000-0000-000000000000</code></td>
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
    <td>The version of Ceph</td>
    <td><code>pacific</code></td>
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
    <td>the internal ip address of the API</td>
    <td><code>192.168.32.9</code></td>
  </tr>
  <tr>
    <td><code>manager_version</code></td>
    <td>The version of the osism-ansible container</td>
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
    <td>The version of OpenStack</td>
    <td><code>yoga</code></td>
  </tr>
  <tr>
    <td><code>project_name</code></td>
    <td>Name of the first OpenStack project</td>
    <td><code>customer</code></td>
  </tr>
  <tr>
    <td><code>with_ceph</code></td>
    <td>1 to use Ceph, 0 to not use Ceph</td>
    <td><code>1</code></td>
  </tr>
  <tr>
    <td><code>with_vault</code></td>
    <td>1 to use Ansible-Vault, 0 to not use Ansible-Vault</td>
    <td><code>1</code></td>
  </tr>
  <tr>
    <td></td>
    <td></td>
    <td><code></code></td>
  </tr>
</table>
