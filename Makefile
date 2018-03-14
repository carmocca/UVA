.SILENT:
.ONESHELL:
SHELL := /bin/bash

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
	python3 ./N10104/test.py
	python3 ./N00861/test.py
	python3 ./N10128/test.py
	python3 ./N10034/test.py

clean:
	echo Cleaning...
	find . -type d -name "__pycache__" -exec rm -rf {} +
	find . -type d -name ".cache" -exec rm -rf {} +
	find . -type d -name "*.pyc" -exec rm -rf {} +

generate:
	if [ -z $${FILE} ] ; then \
    	echo "Syntax: make output FILE=<filepath>"
		exit
	fi

	if [ ! -f $$FILE ]; then \
    	echo "File not found"
		exit
	fi

	# Remove initial "./" if neccessary
	if [[ $$FILE == ./* ]] ; then \
		FILE=$${FILE:2}
	fi

	# Clean junk
	find . -type d -name "__pycache__" -exec rm -rf {} +
	find . -type d -name ".cache" -exec rm -rf {} +
	find . -type d -name "*.pyc" -exec rm -rf {} +

	# Create the auxiliary __main__ wrapper
	touch __main__.py

	IFS= # To keep line breaks
	MAIN=$$(sed -ne '/__name__/,$$p' $$FILE)

	DIR=$$(dirname $$FILE)
	DOT_PATH=$$(dirname $$FILE | tr / .)
	BASE=$$(basename $$FILE .py)

	# Write the correct main entrypoint
	echo "import sys" >> __main__.py
	echo -e "from $$DOT_PATH.$$BASE import $$BASE\n" >> __main__.py
	echo $$MAIN >> __main__.py

	echo -e "Generated wrapper:"
	echo "==================="
	cat __main__.py

	# Bundle everything into a zip
	zip -rq output __main__.py lib $$DIR

	# Remove the wrapper
	rm __main__.py

