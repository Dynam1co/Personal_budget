[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![pre-commit.ci status](https://results.pre-commit.ci/badge/github/pre-commit/pre-commit-hooks/master.svg)](https://results.pre-commit.ci/latest/github/pre-commit/pre-commit-hooks/master)
![example workflow](https://github.com/Dynam1co/Personal_budget/actions/workflows/main.yml/badge.svg)

# Personal budget
Controlling my personal expenses in Python.

The idea is to have a global vision of my expenses, categorize them according to my own criteria and analyze them to try to minimize them.

Another function will be to set up alerts for fixed expenses according to their periodicity. These alerts will be sent via Telegram.

In the future, having a large database already well categorized, I would like to have the bank movements automatically categorized using some artificial intelligence algorithm.

## How it works
The program will be continuously reading a folder where I will store the excels that I download manually from the bank and that contain the movements in the account.

The system will automatically load them to the database and move them to a "processed files" path.

The transactions must be correctly categorized for the analysis to be good. A series of reports will be generated and sent via Telegram.

## Config
Rename **.env.sample** to **.env** and use your own parameters.

## Constants
There is a file with constants [myconstants.py](myconstants.py). The sensitive ones are read from the .env file. Others, such as the expense types, are put in a dictionary that is automatically loaded into the database when the [main.py](main.py) file is executed.

These expense types are necessary to be able to configure alerts for periodic payments.

## Database
Dockerized PostgreSQL database.

### Create volume:
```bash
$ docker volume create --name=postgresql-volume
```

### Run containers
```bash
docker-compose up --build
```

### Stop containers
```bash
docker-compose down
```

### Restart containers
```bash
docker-compose restart
```

### Docker volume path:
```
\\wsl$\docker-desktop-data\version-pack-data\community\docker\volumes
```
