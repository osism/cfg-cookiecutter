
venv = . .venv/bin/activate
export PATH := ${PATH}:${PWD}/venv/bin


deps: .venv/bin/activate system-installations ## Install software preconditions to `.venv`.

prune:
	rm -rf .venv

.venv/bin/activate: Makefile requirements.txt requirements-cfg.txt
	@which python3 > /dev/null || { echo "Missing requirement: python3" >&2; exit 1; }
	[ -e venv/bin/python ] || virtualenv -p $$(which python3) .venv > /dev/null
	@virtualenv --version > /dev/null || { echo "Missing requirement: virtualenv -- aborting" >&2; exit 1; }
	@${venv} && pip3 install -r requirements.txt
	@${venv} && pip3 install -r requirements-cfg.txt
	@${venv} ; gilt overlay && gilt overlay
	touch .venv/bin/activate

system-installations:
	@which keepass2 > /dev/null || { echo "Missing requirement: keepass" >&2; exit 1; }

ansible_vault_rekey: deps
	pwgen -1 32 > secrets/vaultpass.new
	${venv} && find environments/ inventory/ -name "*.yml" -exec grep -l ANSIBLE_VAULT {} \+|\
		sort -u|\
		xargs -n 1 --verbose ansible-vault rekey  -v \
		--vault-password-file secrets/vaultpass \
		--new-vault-password-file secrets/vaultpass.new
	mv secrets/vaultpass.new secrets/vaultpass

ansible_vault_show: deps
	${venv} && find environments/ inventory/ -name "*.yml" -exec grep -l ANSIBLE_VAULT {} \+|\
		sort -u|\
		xargs -n 1 --verbose ansible-vault view --vault-password-file secrets/vaultpass | cat

phony: deps prune system-installations ansible_vault_rekey ansible_vault_show
