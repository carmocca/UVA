.SILENT:
.ONESHELL:
SHELL := /bin/bash

test:
	find . -name "test.py" | xargs -n1 python3

clean:
	echo Cleaning...
	find . -type d -name "__pycache__" -exec rm -rf {} +
	find . -type d -name ".cache" -exec rm -rf {} +
	find . -type d -name "*.pyc" -exec rm -rf {} +

generate:
	if [ -z $${FILE} ] ; then \
    	echo "Syntax: make generate FILE=<filepath>"
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
