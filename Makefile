.PHONY: install
install:
	pipenv install -d

.PHONY: test
test:
	pipenv run pytest

.PHONY: lint
lint:
	pipenv run mypy --ignore-missing-imports ./aoc
