lint:
	uv run ruff check . --fix --exit-non-zero-on-fix

format:
	uv run ruff format .