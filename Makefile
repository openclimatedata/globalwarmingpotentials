all: src/globalwarmingpotentials/__init__.py index.js

src/globalwarmingpotentials/__init__.py index.ts: scripts/generate_modules.py globalwarmingpotentials.csv
	uv run $<
	uvx ruff format

index.js: index.ts tsconfig.json package.json
	@npm install
	@npm run build
	@npm run format

clean:
	rm index.js index.ts src/globalwarmingpotentials/__init__.py

tag:
	./scripts/create_tag.sh

.PHONY: clean
