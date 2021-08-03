index.js src/globalwarmingpotentials/__init__.py: scripts/generate_modules.py datapackage.json globalwarmingpotentials.csv venv
	@./venv/bin/python $<

venv: scripts/requirements.txt
	[ -d ./venv ] || python3 -m venv venv
	./venv/bin/pip install --upgrade pip
	./venv/bin/pip install -Ur $<
	touch venv

clean-generated-files:
	rm -rf index.js py/globalwarmingpotentials/__init__.py

clean-venv:
	rm -rf venv

clean: clean-generated-files clean-venv

tag:
	./scripts/create_tag.sh

publish-on-pypi:
	./scripts/publish-on-pypi.sh

publish-on-test-pypi:
	./scripts/publish-on-test-pypi.sh

test-pypi-install:
	$(eval TEMPVENV := $(shell mktemp -d))
	python3 -m venv $(TEMPVENV)
	$(TEMPVENV)/bin/pip install pip --upgrade
	$(TEMPVENV)/bin/pip install globalwarmingpotentials
	$(TEMPVENV)/bin/python -c "import sys; sys.path.remove(''); import globalwarmingpotentials; print(globalwarmingpotentials.__version__)"

validate:
	./venv/bin/python scripts/validate.py

.PHONY: clean clean-generated-files clean-venv tag publish-on-pypi publish-on-test-pypi test-pypi-install
