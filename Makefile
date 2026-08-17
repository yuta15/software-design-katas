UV := uv
SOURCE := src

.PHONY: sync format lint lint-fix import-lint type-check check pre-commit-install pre-commit-run

sync:
	$(UV) sync --dev

format:
	$(UV) run ruff format $(SOURCE)

lint:
	$(UV) run ruff check $(SOURCE)

lint-fix:
	$(UV) run ruff check --fix $(SOURCE)

import-lint:
	PYTHONPATH=$(SOURCE) $(UV) run lint-imports

type-check:
	$(UV) run pyright

check: lint import-lint type-check

pre-commit-install:
	$(UV) run pre-commit install

pre-commit-run:
	$(UV) run pre-commit run --all-files
