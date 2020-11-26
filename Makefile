API_PORT := 8000
PROJECT_NAME := pokemon-api
FILE := data/pokemon.csv
REQUIREMENTS_FILE := requirements.txt
SOURCE_PATH := ./src
COMMAND_RUN := python3 ./src/main.py $(FILE) --port $(API_PORT)
COMMAND_TEST := python3 -m pytest -vv
VENV_PATH := .venv

default:
	make run

dev: install/dev
	nodemon --exec $(COMMAND_RUN)

install:
	pip3 install -r $(SOURCE_PATH)/$(REQUIREMENTS_FILE)

.PHONY: install/dev
install/dev:
	npm i

.PHONY: build/requirements
build/requirements:
	pip3 freeze > ./src/$(REQUIREMENTS_FILE)

docker:
	make docker/run

.PHONY: docker/build
docker/build:
	docker build --rm -t "$(PROJECT_NAME)" .

.PHONY: docker/run
docker/run:
	docker run --net=host --rm --env-file .env --name $(PROJECT_NAME) -it $(PROJECT_NAME)

env:
	echo run "source $(VENV_PATH)/bin/activate" in your terminal

.PHONY: env/create
env/create:
	python3 -m venv $(VENV_PATH)

.PHONY: env/file
env/file:
	cp .env.example .env

run:
	$(COMMAND_RUN)

.PHONY: tests
tests:
	$(COMMAND_TEST)


.PHONY: test/watch
tests/watch:
	$(COMMAND_TEST)
	watchmedo shell-command \
 	--patterns="*.py" \
	--recursive \
 	--command="clear; $(COMMAND_TEST)" \
 	.