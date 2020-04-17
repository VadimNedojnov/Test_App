# Test App

## Requirements

 - Installed [Git](https://git-scm.com/)
 - Installed [Docker](https://docs.docker.com/install/)
 - Installed [Docker Compose](https://docs.docker.com/compose/install/)
 - Installed [PostgreSQL](https://www.digitalocean.com/community/tutorials/how-to-install-and-use-postgresql-on-ubuntu-18-04-ru/)

### Development tools

 - IDE: PyCharm Community Edition

## Installation

#### Clone the project
Add ssh key to git repository
```bash
  git clone git@github.com:VadimNedojnov/Test_App.git
```

#### Build docker images:
```bash
  docker-compose -f dc.yml up -d --build
```

#### Application migrations:

```bash
  docker exec -it backend_test_app python ./src/manage.py makemigrations                                    --- makemigration in docker
  docker exec -it backend_test_app python ./src/manage.py migrate
```

## How to run web interface and tests

#### Directory structure
 - `src/test-app`: Main project files. Configuration files.
 - `src/account`: Application for managing users accounts.
 - `src/logger`: Application for collecting logs and metrics.
 - `tests`: Project tests.

#### How to run web interface

To run web interface you need to open the browser, type `http://127.0.0.1:8000/` in the address line and press Enter.

#### How to run tests

To run tests you need to open bash in the Test_App directory and enter the command:
```bash
  docker exec -it backend_test_app pytest --cov=./src ./src -s --cov-config .coveragerc --cov-report html
```

#### How to stop docker containers when you don't need them anymore
```bash
docker-compose down
```

## Troubleshooting


## Links

