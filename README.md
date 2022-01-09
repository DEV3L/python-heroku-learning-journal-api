[![Build Status](https://travis-ci.org/DEV3L/python-heroku-learning-journal-api.svg?branch=master)](https://travis-ci.org/DEV3L/python-heroku-learning-journal-api)
[![Maintainability](https://api.codeclimate.com/v1/badges/9d81f4a4e4735be1cf16/maintainability)](https://codeclimate.com/github/DEV3L/python-heroku-learning-journal-api/maintainability)
[![Coverage Status](https://coveralls.io/repos/github/DEV3L/python-heroku-learning-journal-api/badge.svg?branch=master)](https://coveralls.io/github/DEV3L/python-heroku-learning-journal-api?branch=master)

# Python Flask Heroku Learning Journal API

Social learning journal.

Articles written on Dev.to detailing project purpose, setup, and execution:<br />
[Social Learning Journal - Parsing Audiobooks](https://dev.to/dev3l/social-learning-journal-parsing-audiobooks-2428)<br />
[Social Learning Journal - Classification](https://dev.to/dev3l/social-learning-journal-classification-28gf)<br />
[Social Learning Journal - Density](https://dev.to/dev3l/social-learning-journal-density-opb)<br />
[Social Learning Journal - Mediums](https://dev.to/dev3l/social-learning-journal-mediums-43ei)<br />
[Social Learning Journal - Persistence](https://dev.to/dev3l/social-learning-journal-persistence-3og8)<br />
[Social Learning Journal - React](https://dev.to/dev3l/social-learning-journal-react-5494)<br />
[Social Learning Journal - Walking Skeleton](https://dev.to/dev3l/social-learning-journal-walking-skeleton-1o3l)<br />

## Prerequisites

- Python 3x
- MongoDB

### Recommendations

- PyCharm
- MongoDB Compass
- Docker

## Environment Variables

Copy the contents of .env.local into a new file named .env

```
cp .env.local .env
```

## Running Locally

1. Setup MongoDb

`docker-compose up -d`

2. Install Python Dependencies

```
~ python3 -m venv venv
~ source venv/bin/activate
(venv) ~ python setup.py develop
```

3. Run Tests

`(python-flask-heroku-learning-journal) ~ pytest`

4. Run Application for Development

`(python-flask-heroku-learning-journal) ~ python app.py runserver`


#### PyCharm

Dependency management and interactive debugging are available using PyCharm.

The [Configure a virtual environment](https://www.jetbrains.com/help/pycharm/creating-virtual-environment.html)
can help with questions on how to do this.

## Components

#### Flask

#### MongoDb

#### Logging

`logs` directory - Rotating 10mb

#### Swagger

http://localhost:5000/swagger

#### Scripts
