# montagu-py

[![Build Status](https://travis-ci.com/vimc/montagu-py.svg?branch=master)](https://travis-ci.com/vimc/montagu-py)
[![codecov.io](https://codecov.io/github/vimc/montagu-py/coverage.svg?branch=master)](https://codecov.io/github/vimc/montagu-py?branch=master)

Python client for [Montagu API](https://github.com/vimc/montagu-api). 

Initial use case is for authentication only.

## Usage

The client currently supports authenticating with Montagu, and a single example endpoint.

To authenticate, instantiate the `MontaguAPI` class, providing base url, username and password as parameters:

```
api = MontaguAPI('http://localhost:8080', 'test.user@example.com', 'password')
```

The Montagu authentication token can be accessed on the api object: 
```
token = api.token
```

The example endpoint returns a list of all diseases:
```
diseases = api.diseases()
```

## Development

Clone the repo anywhere and install dependencies with (from the repo root):

```
pip3 install --user -r requirements.txt
```

Run dependencies (a local copy of Montagu API and database) with `scripts/run-dev-dependencies.sh`. This will also
add a test user to Montagu.

## Testing

Run dependencies as described above, then run `pytest`

## Publishing

This repository is published to [PyPI](https://pypi.org/project/montagu). 

Building and publishing is done manually, with local sources. 

Publishing configuration can be found in `setup.py`, and any classes, methods etc which should be accessible to users of the package
must be added to `montagu/__init__.py`. 
Remember to increment `version` in `setup.py` before publishing a new build.

To publish:
1. Delete the following folders: `.eggs`, `build`, `dist`, `montagu.egg-info`. 
1. Build the package with: `python3 setup.py sdist bdist_wheel`
1. Publish with: `python3 -m twine upload dist/*`

To use the MontaguAPI class as a client of the package, include `montagu` in your `requirements.txt`. Import with
`import montagu`, and instantiate the API class with `montagu.MontaguAPI(url, username, password)`

See general instructions for publishing Python packages [here](https://packaging.python.org/tutorials/packaging-projects/).

Some troubleshooting tips for publishing Python packages can be found in the 
[consellations repo](https://github.com/reside-ic/constellation/blob/master/publish.md).

