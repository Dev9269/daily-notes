lint:
	python -m compileall scripts

test:
	python -m pytest --tb=short

.PHONY: lint test
