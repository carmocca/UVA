test:
	python3 ./N00100/test.py
	python3 ./N10142/test.py
	python3 ./N10189/test.py

clean:
	find . -type d -name "__pycache__" -exec rm -rf {} +
	find . -type d -name ".cache" -exec rm -rf {} +
	find . -type d -name "*.pyc" -exec rm -rf {} +
