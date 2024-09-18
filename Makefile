install:
	pip install -r requirements.txt
lint:
	#ruff src/ tests/
	ruff check src/*.py tests/*.py *.ipynb
format:
	black src/ tests/
test:
	pytest --nbval tests/test_script.py
	pytest --nbval tests/test_lib.py
	pytest --nbval *.ipynb