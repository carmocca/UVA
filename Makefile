init:
	pip install -r requirements.txt

test:
	pytest 10044\ -\ Erdos\ Numbers/test.py

clean:
	find . -type d -name __pycache__ -exec rm -rf {} +