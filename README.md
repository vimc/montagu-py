# montagu-py

[![Build Status](https://travis-ci.org/vimc/montagu-py.svg?branch=vimc-4028)](https://travis-ci.org/mrc-ide/hint-deploy)
[![codecov.io](https://codecov.io/github/vimc/montagu-py/coverage.svg?branch=vimc-4028)](https://codecov.io/github/mrc-ide/hint-deploy?branch=master)

Python client for [Montagu API](https://github.com/vimc/montagu-api). 

Initial use case is for authentication only.

## Development

Clone the repo anywhere and install dependencies with (from the repo root):

```
pip3 install --user -r requirements.txt
```

Run dependencies (a local copy of Montagu API and database) with `scripts/run-dev-dependencies.sh`. This will also
add a test user to Montagu.

## Testing

Run dependencies as described above, then run `pytest`