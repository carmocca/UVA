test:
	python3 ./N00100/test.py
	python3 ./N10142/test.py
	python3 ./N10189/test.py
	python3 ./N10033/test.py
	python3 ./N10315/test.py
	python3 ./N10050/test.py
	python3 ./N10044/test.py
	python3 ./N00843/test.py
	python3 ./N10010/test.py

clean:
	find . -type d -name "__pycache__" -exec rm -rf {} +
	find . -type d -name ".cache" -exec rm -rf {} +
	find . -type d -name "*.pyc" -exec rm -rf {} +
