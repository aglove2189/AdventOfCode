init:
	python -m venv venv && venv/bin/pip install -r requirements.txt
	venv/bin/pre-commit install
	echo 'PYTHONPATH=src' > .env