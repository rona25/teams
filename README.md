# Notes / Assumptions

* Some of the files/patterns in this project were based on boilerplate templates/patterns that I have accumulated as "best practices" in my opinion
* There is no "real/functional" implementation of the business logic for the admin interface endpoints (`/health`, `/abortabortabort`, `/quitquitquit`)
  * These endpoints are merely implemented as stubs and always return `200`


# Dependencies

The following tools are required to execute the code:

* `python2.7`
* `python-virtualenv`
* `make`

### Ubuntu
```
$ sudo apt-get install python-dev python-virtualenv build-essential
```

# Execution

### TL;DR

```
$ make env
$ make service-start
$ curl "http://localhost:8080/teams"
$ curl "http://localhost:8080/teams/us-presidents"
$ curl "http://localhost:8080/membership?username=tjefferson"
$ curl "http://localhost:8081/health"
$ curl -X POST "http://localhost:8081/abortabortabort"
$ curl -X POST "http://localhost:8081/quitquitquit"
```

### Available Commands

* You can list all of the available `make` targets (with descriptions) by running `make`:

```
$ make
###########################################################
# SRE Teams Actions
###########################################################

clean                                    Removes the virtualenv and temp files
env                                      Creates the python virtualenv
lint                                     Runs the linter over the codebase
service-help                             Shows the team service options
service-start                            Launches the teams service
service-status                           Gets the status of the teams service
test                                     Runs the tests

    (use 'make <target> -n' to show the commands)
```

### Setup / Create Environment

* Prepare the virtual environment by running `make env`:

```
$ make env
New python executable in venv/bin/python2.7
Also creating executable in venv/bin/python
...
Successfully installed ...
```


### Run Tests

* To run the tests, run `make test`:

```
$ make test
Lint Success
...
----------------------------------------------------------------------
Ran 3 tests in 0.000s

OK
```

### Run Web Service

* To run the web services on the default ports (API: port 8080; Admin: Port 8081):

```
$ make service-start
2017-11-02 23:40:26,794 INFO RPC interface 'supervisor' initialized
2017-11-02 23:40:26,794 CRIT Server 'unix_http_server' running without any HTTP authentication checking
2017-11-02 23:40:26,794 INFO supervisord started with pid 18929
2017-11-02 23:40:27,802 INFO spawned: 'teams-svc' with pid 18932
2017-11-02 23:40:27,805 INFO spawned: 'teams-admin' with pid 18933
2017-11-02 23:40:29,026 INFO success: teams-svc entered RUNNING state, process has stayed up for > than 1 seconds (startsecs)
2017-11-02 23:40:29,026 INFO success: teams-admin entered RUNNING state, process has stayed up for > than 1 seconds (startsecs)

```

#### Log Files

When the web service is run, the log files are stored in `tmp/logs/*`

### Display Web Service Options

* To run the web services on non-default ports, see how to run the services manually:


```
$ make service-help
Usage: bin/team_service.sh <HOST> <API PORT> <ADMIN PORT>
```
