# Clinical Data Storage System


[![Build Status](https://travis-ci.org/joemccann/dillinger.svg?branch=master)](https://travis-ci.org/joemccann/dillinger)

It is a system where hospitals store their clinical data.

## Features

- Superuser/ staff can add data such as create hospital, doctor and establish relationship

- Doctor can fetch patient medical history by aadhaar number.

- Doctor can create mediacl records for patients.

- Audit api will provide all the data to authenticated users.


## Tech
- Python 3.8
- Django 2.2
- django rest framework 2.8

## Postman Collection
- Find the **Postman** collection for the apis [Here](https://www.getpostman.com/collections/63e9f35287d844bb4263)

## Running the project
Create  and activate virtual environment with python 3.8
```sh
virtualenv -p python3 env
source env/bin/activate
```

Install requirements.txt
```sh
pip install -r requirements.txt
```

Run server
```sh
./manage.py runserver
```

