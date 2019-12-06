SHELL := /bin/bash -euxo pipefail

include lint.mk

# Treat Sphinx warnings as errors
SPHINXOPTS := -W

.PHONY: lint
lint: \
    check-manifest \
    flake8 \
    isort \
    mypy \
    pip-extra-reqs \
    pip-missing-reqs \
    pyroma \
    shellcheck \
    vulture \
    pylint \
    pydocstyle \
    yapf

.PHONY: fix-lint
fix-lint:
	# Move imports to a single line so that autoflake can handle them.
	# See https://github.com/myint/autoflake/issues/8.
	# Then later we put them back.
	isort --force-single-line --recursive --apply
	$(MAKE) autoflake
	$(MAKE) fix-yapf
	isort --recursive --apply
