help:
	@echo "Usage:"
	@echo "    make help       show this message"
	@echo "    make test       run the test suite"
	@echo "    make black      format code using black"

black:
	black .

test:
	python -m pytest tests

docs:
	sphinx-apidoc -M -f --no-toc --implicit-namespaces -o docs enviropy
	cd docs && make html
	@echo "\033[95m\nBuild successful! View the docs at docs/_build/html/index.html.\n\033[0m"

.PHONY: docs