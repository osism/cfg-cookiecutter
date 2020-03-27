#!/usr/bin/env bash

# NOTE: this is being done twice on purpose here
MANAGER_VERSION={{ cookiecutter.osism_manager_version }} gilt overlay
MANAGER_VERSION={{ cookiecutter.osism_manager_version }} gilt overlay

if [[ "{{ cookiecutter.openstack_version }}" == "queens" || "{{ cookiecutter.openstack_version }}" == "rocky" ]]; then
    mv environments/kolla/files/overlays/haproxy/haproxy.cfg.{{ cookiecutter.openstack_version }} environments/kolla/files/overlays/haproxy/haproxy.cfg
    rm -rf environments/kolla/files/overlays/haproxy/services.d/
fi
rm -f environments/kolla/files/overlays/haproxy/haproxy.cfg.*

rm -rf environments/kolla/files/overlays/gnocchi-api
rm -rf environments/kolla/files/overlays/gnocchi-metricd
rm -rf environments/kolla/files/overlays/gnocchi-statsd

for name in operator configuration; do
    ssh-keygen -t rsa -b 4096 -N "" -f secrets/id_rsa.$name -C "" -m PEM
done

bash scripts/generate-secrets.sh
rm -f environments/kolla/secrets.yml.*

python scripts/set-secrets.py
python scripts/set-ssh-keypairs.py

# pwgen -1 32 > secrets/keepass
python scripts/generate-keepass.py

if [[ {{ cookiecutter.with_vault }} == 1 ]]; then
    pwgen -1 32 > secrets/vaultpass
    for secretsfile in $(find environments -name 'secrets.yml'); do
        ansible-vault encrypt --vault-password-file secrets/vaultpass $secretsfile
    done
else
    rm environments/.vault_pass
fi

if [[ {{ cookiecutter.with_ceph }} == 0 ]]; then
    rm -rf environments/ceph

    rm -rf environments/kolla/files/overlays/gnocchi

    rm -rf environments/kolla/files/overlays/glance-api
    rm -f environments/kolla/files/overlays/glance/ceph.conf

    rm -rf environments/kolla/files/overlays/cinder/cinder-backup
    rm -rf environments/kolla/files/overlays/cinder/cinder-volume
    rm -f environments/kolla/files/overlays/cinder/ceph.conf
    rm -f environments/kolla/files/overlays/cinder/cinder-volume.conf

    rm -rf environments/kolla/files/overlays/nova/ceph.conf
    rm -rf environments/kolla/files/overlays/nova/ceph.client.cinder.keyring
    rm -rf environments/kolla/files/overlays/nova/ceph.client.nova.keyring
fi

rm -rf scripts
