DEV_API_VERSION=latest

DOCKERCMD=docker

DOCKERBUILD=$(DOCKERCMD) build

DOCKERRUN=${DOCKERCMD} run

DOCKERSTOP=${DOCKERCMD} stop

DOCKER_RM=${DOCKERCMD} rm

DOCKERFILE=Dockerfile

DOCKER_IMAGE=summarization

.PHONY: build-docker
build-docker:
	$(DOCKERBUILD) -t ${DOCKER_IMAGE} -f ${DOCKERFILE} . 
.PHONY: run-docker
run-docker:
	$(DOCKERRUN) -p 8000:8000 ${DOCKER_IMAGE}

# .PHONY: coverage
# coverage:  ## Run tests with coverage
# 	coverage erase
# 	coverage run --include=podsearch/* -m pytest -ra
# 	coverage report -m

# .PHONY: deps
# deps: 
# 	pip install black coverage flake8 mypy pylint pytest tox

# .PHONY: lint
# lint:  ## Lint and static-check
# 	deps
# 	flake8 podsearch
# 	pylint podsearch
# 	mypy podsearch

.PHONY: summarize-up
summarize-up: build-docker run-docker

.PHONY: summarize-down
summarize-down: $(DOCKERSTOP) ${DOCKER_IMAGE}; $(DOCKER_RM) ${DOCKER_IMAGE}