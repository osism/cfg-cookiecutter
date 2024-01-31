

venv = . .venv/bin/activate
export PATH := ${PATH}:${PWD}/venv/bin


deps: venv/bin/activate gilt ## Install software preconditions to `venv`.

gilt: deps
	 ${venv} ; gilt overlay && gilt overlay

venv/bin/activate: Makefile requirements.txt
	@which python3 > /dev/null || { echo "Missing requirement: python3" >&2; exit 1; }
	@which jq > /dev/null || { echo "Missing requirement: jq" >&2; exit 1; }
	virtualenv --version > /dev/null || { echo "Missing requirement: virtualenv -- aborting" >&2; exit 1; }
	[ -e venv/bin/python ] || virtualenv -p $$(which python3) .venv > /dev/null
	@${venv} && pip3 install -r requirements.txt
	touch .venv/bin/activate

phony: help deps
