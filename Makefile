index.js src/globalwarmingpotentials/__init__.py: scripts/generate_modules.py globalwarmingpotentials.csv venv
	@./venv/bin/python $<
	@./venv/bin/black src/globalwarmingpotentials/*.py

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

.PHONY: clean clean-generated-files clean-venv tag publish-on-pypi publish-on-test-pypi test-pypi-install
