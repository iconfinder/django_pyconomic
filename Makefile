install:
	python setup.py install

test:
	@pep8 django_pyconomic setup.py
	@pyflakes django_pyconomic setup.py

clean:
	@rm -rf build dist *.egg*

publish:
	@python setup.py sdist upload

.PHONY: install test clean publish
