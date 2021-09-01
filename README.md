# python-url-shortener

This is a sample project of a Python URL Shortner REST API. Time spent: ~1 hour

## Table of Contents

* [Requirements](#requirements)
* [Installation](#installation)
* [Usage](#usage)
* [Contributing](#contributing))
* [Resources](#resources)

## Requirements

* [Python](https://www.python.org/)
* [Pipenv](https://pipenv.pypa.io/en/latest/)
* [Flask](https://flask.palletsprojects.com/en/2.0.x/)
* [Flask-sqlalchemy](https://flask-sqlalchemy.palletsprojects.com/en/2.x/)
* [Flask-restx](https://flask-restx.readthedocs.io/en/latest/)
* [Hashids](https://hashids.org/)

## Installation

```bash
$ git clone https://github.com/nathanurwin/python-url-shortener
$ cd python-url-shortener
$ pipenv install
```

## Usage

```bash
$ cd python-url-shortener
$ pipenv run flask run
```

```bash
$ curl -H "Content-Type: application/json" http://127.0.0.1:5000/urls -d '{"url":"http://google.com"}'
{"url": "http://127.0.0.1:5000/R4dR"}

$ curl http://127.0.0.1:5000/R4dR                                                                     
{"url": "http://google.com"}

$ curl http://127.0.0.1:5000/test
{"message": "Not Found"}

$ rm -f src/test.db
$ curl http://127.0.0.1:5000/R4dR
{"message": "Internal Server Error"}

```

## Contributing

```
$ cd python-url-shortener
$ pipenv install -d
$ pipenv run pytest
```

## Resources

* [How To Make a URL Shortener with Flask and SQLite](https://www.digitalocean.com/community/tutorials/how-to-make-a-url-shortener-with-flask-and-sqlite)
* [How to Build a REST API with Flask and SQLAlchemy](https://rahmanfadhil.com/flask-rest-api/)
* [Flask-RESTX API as a Python Package Cookie](https://github.com/alvarobartt/restx-cookie)
* [Flask-RESTX Boilerplate](https://github.com/X1Zeth2X/flask-restx-boilerplate)
