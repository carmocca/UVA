init:
	pip install -r requirements.txt

test:
	pytest ./N00100/test.py

clean:
	find . -type d -name __pycache__ -exec rm -rf {} +