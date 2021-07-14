# Defines the default target that `make` will to try to make, or in the case of a phony target, execute the specified commands
# This target is executed whenever we just type `make`
.DEFAULT_GOAL = help

# The @ makes sure that the command itself isn't echoed in the terminal
help:
	@echo "---------------HELP-----------------"
	@echo "To install dependenceis: make install"
	@echo "To run the project: make run"
	@echo "To run background tasks: make tasks"
	@echo "To test: make test"
	@echo "To lint with flake8: make flake"
	@echo "To run the formatter make black"
	@echo "------------------------------------"

install:
	pip install -r requirements.txt

test:
	pytest tests.py

tasks:
	python background_process.py

run:
	python main.py

flake:
	flake8 --exclude=env,__pycache__,.vscode --ignore=E501,E402

black:
	black .

ps:
	docker-compose ps

restart:
	docker-compose restart

runcontainers:
	docker-compose up --build

stopcontainers:
	docker-compose down
