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

## Execution flow
The application has two operating threads. One is continuously running and is in charge of processing files, loading them into the database and categorizing the ones it can.

Another that requires user intervention, which allows to visualize the movements pending to be categorized, categorize them manually, etc. This part displays a menu with which the user can interact:

![Menu capture](img/menu.PNG)

## Own categories and subcategories
The categories and subcategories assigned by the bank are not sufficient and are often inaccurate, so there is a table to store the categories themselves and another one for the subcategories. We will have to fill in these two tables based on our own criteria.

### Automatic mapping of categories and subcategories
Once the movement is saved in the database, there is a procedure to establish our own categories and subcategories, to do this as automatically as possible we have created a table that links descriptions of bank movements with a category and subcategory.

The table is called **mappingcategories** with the following structure:
| TEXT TO FIND  | TEXT TO EXCLUDE      | DESTINATION CATEGORY | DESTINATION SUBCATEGORY |
| ------------- | ------------------ | ----------- | -------------- |
| nomina        | traspaso peri??dico | 12          | 3              |
| est. servicio |                    | 15          | 7              |


## Config
Rename **.env.sample** to **.env** and use your own parameters.

## Constants
There is a file with constants [myconstants.py](myconstants.py). The sensitive ones are read from the .env file. Others, such as the expense types, are put in a dictionary that is automatically loaded into the database when the [background_process.py](background_process.py) file is executed.

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
