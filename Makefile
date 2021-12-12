SHELL := /bin/bash -euxo pipefail

include lint.mk

.PHONY: lint
lint: \
	  black \
    check-manifest \
    doc8 \
    flake8 \
    isort \
    mypy \
    pip-extra-reqs \
    pip-missing-reqs \
    pyroma \
    vulture \
    pylint \
    pydocstyle \

.PHONY: fix-lint
fix-lint: \
    autoflake \
    fix-black \
    fix-isort
