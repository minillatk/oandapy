clean: clean-eggs clean-build
	@find . -iname '*.pyc' -delete
	@find . -iname '*.pyo' -delete
	@find . -iname '*~' -delete
	@find . -iname '*.swp' -delete
	@find . -iname '*ropeproject' -delete
	@find . -iname '__pycache__' -delete

clean-eggs:
	@find . -name '*.egg' -print0|xargs -0 rm -rf --
	@rm -rf .eggs/

clean-build:
	@rm -fr build/
	@rm -fr dist/
	@rm -fr *.egg-info

lint:
	pre-commit run -av

pip-install:
	pip install -r requirements-dev.txt

pip-upgrade:
	pip install --upgrade -r requirements-dev.txt

coverage:
	coverage run --source=oandapy make test

cov-report:
	py.test -vv --cov-report=html tests

test: pip-install
	py.test -vv -s

find_todo:
	@grep --color=always -PnRe "(#|\"|\').*TODO" oandapy || true

find_fixme:
	@grep --color=always -nRe "#.*FIXME" oandapy || true

count:
	@find . -type f \( -name "*.py" -o -name "*.rst" \) | xargs wc -l

build: test
	python setup.py sdist
	python setup.py bdist_wheel

release: clean build
	git tag `python setup.py -q version`
	git push origin `python setup.py -q version`
	twine upload dist/*

generate_docs:
	@sphinx-apidoc -f -o docs/source oandapy
