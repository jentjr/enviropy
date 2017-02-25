.PHONY: docs

docs:
	sphinx-apidoc -M -f --no-toc --implicit-namespaces -o docs enviropy
	cd docs && make html
	@echo "\033[95m\nBuild successful! View the docs at docs/_build/html/index.html.\n\033[0m"
