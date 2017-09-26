.PHONY: help
help:
	@echo "    all"
	@echo "        Install and run project."
	@echo "    install"
	@echo "        Install project."
	@echo "    run"
	@echo "        Run project."
	@echo "    develop"
	@echo "        Install project in develop mode."
	@echo "    test"
	@echo "        Install project in develop mode and run tests."
	@echo "    clean-pyc"
	@echo "        Remove python artifacts."
	@echo "    clean-build"
	@echo "        Remove build artifacts."
	@echo "    clean"
	@echo "        Remove all artifacts."
	@echo "    docker-image"
	@echo "        Create docker image."
	@echo "    docker-run"
	@echo "        Remove docker container and create."
	@echo "    docker-logs"
	@echo "        Show docker logs."
	@echo "    docker"
	@echo "        Create docker image and remove and create docker container."

.PHONY: all
all: clean install run

.PHONY: install
install:
	pip install .

.PHONY: run
run:
	iris -c ./etc/config.ini -l ./logs/iris.log -d -v

.PHONY: develop
develop:
	pip install -e .

.PHONY: test
test: develop
	python setup.py pytest

.PHONY: clean-pyc
clean-pyc:
	find . -name '__pycache__' -exec rm -rf {} +

.PHONY: clean-build
clean-build:
	find . -name '.eggs' -exec rm -rf {} +
	find . -name '*.egg-info' -exec rm -rf {} +

.PHONY: clean
clean: clean-build clean-pyc

.PHONY: docker-build
docker-build:
	docker build -t ${USER}-ml-iris .

.PHONY: docker-run
docker-run:
	docker rm -f ${USER}-ml-iri; echo
	docker run --name ${USER}-ml-iri -dt ${USER}-ml-iri

.PHONY: docker-logs
docker-logs:
	docker logs -f ${USER}-ml-iri

.PHONY: docker
docker: docker-build docker-run docker-logs
