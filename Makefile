install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

test:
	python -m pytest test.py

lint:
	pylint --disable=R,C breakfast.py 

all: install lint test
