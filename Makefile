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
	python3 ./N00850/test.py
	python3 ./N00120/test.py
	python3 ./N10152/test.py
	python3 ./N10138/test.py
	python3 ./N10037/test.py
	python3 ./N10026/test.py
	python3 ./N10127/test.py
	python3 ./N00847/test.py
	python3 ./N10213/test.py
	python3 ./N10198/test.py
	python3 ./N10049/test.py
	python3 ./N00846/test.py
	python3 ./N10110/test.py

clean:
	find . -type d -name "__pycache__" -exec rm -rf {} +
	find . -type d -name ".cache" -exec rm -rf {} +
	find . -type d -name "*.pyc" -exec rm -rf {} +
