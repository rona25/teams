PROJECT_NAME=SRE Teams
PYTHON_ENV?=venv
TMP_DIR=tmp
PACKAGE_NAME=web/teams
IN_ENV=. $(PYTHON_ENV)/bin/activate
SERVICE_SCRIPT=bin/team_service.sh


.PHONY: help
help:
	@echo "###########################################################"
	@echo "# $(PROJECT_NAME) Actions"
	@echo "###########################################################"
	@echo ""
	@grep -E -h '^[a-zA-Z0-9_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-40s\033[0m %s\n", $$1, $$2}' | sort
	@echo ""
	@echo "    (use 'make <target> -n' to show the commands)"
	@echo ""


.PHONY: clean
clean:  ## Removes the virtualenv and temp files
	@find . \
		-name *.pyc \
		-exec rm -f {} \
		\;
	@rm -rf $(PYTHON_ENV)
	@rm -rf $(TMP_DIR)


.PHONY: env
env:  ## Creates the python virtualenv
	@virtualenv --no-site-packages --prompt='($(PROJECT_NAME)) ' $(PYTHON_ENV)
	@$(IN_ENV); pip install --upgrade pip distribute setuptools markerlib
	@$(IN_ENV); pip install --upgrade pyOpenSSL ndg-httpsclient pyasn1
	@$(IN_ENV); pip install -r requirements-dev.txt


.PHONY: lint
lint:  ## Runs the linter over the codebase
	@$(IN_ENV); \
		flake8 \
		$(PACKAGE_NAME) \
		--config=conf/flake8.cfg \
		&& echo 'Lint Success'


.PHONY: test
test: lint  ## Runs the tests
	@$(IN_ENV); \
		APP_CONFIG_FILE=tests.py \
		nose2 \
		-c conf/nose2.cfg


.PHONY: service-help
service-help:  ## Shows the team service options
	@$(SERVICE_SCRIPT) -h


.PHONY: service-start
service-start:  ## Launches the teams service
	@$(SERVICE_SCRIPT)


.PHONY: service-status
service-status:  ## Gets the status of the teams service
	@$(IN_ENV) ; \
		supervisorctl -c conf/supervisord.conf status
