# mongo-db-from-config ⚙️ #

[![GitHub Build Status](https://github.com/cisagov/mongo-db-from-config/workflows/build/badge.svg)](https://github.com/cisagov/mongo-db-from-config/actions)
[![CodeQL](https://github.com/cisagov/mongo-db-from-config/workflows/CodeQL/badge.svg)](https://github.com/cisagov/mongo-db-from-config/actions/workflows/codeql-analysis.yml)
[![Coverage Status](https://coveralls.io/repos/github/cisagov/mongo-db-from-config/badge.svg?branch=develop)](https://coveralls.io/github/cisagov/mongo-db-from-config?branch=develop)
[![Known Vulnerabilities](https://snyk.io/test/github/cisagov/mongo-db-from-config/develop/badge.svg)](https://snyk.io/test/github/cisagov/mongo-db-from-config)

This is a small utility library that can be used to easily create a MongoDB
connection based on the data in a simple YAML configuration file.

## Installation ##

Run the following `pip` command to install this package:

```console
pip install https://github.com/cisagov/mongo-db-from-config/tarball/develop
```

## Usage ##

To use this package, first create a YAML configuration file that contains
the information needed to connect to your Mongo database.
Here is a sample configuration file:

```yaml
database:
  uri: mongodb://username:password@localhost:27017/auth-db-name
  name: db-name
```

Here is an example of how to use this package in your Python code:

```python
from mongo_db_from_config import db_from_config

db = db_from_config("my_db_config.yml")
```

## Contributing ##

We welcome contributions!  Please see [`CONTRIBUTING.md`](CONTRIBUTING.md) for
details.

## License ##

This project is in the worldwide [public domain](LICENSE).

This project is in the public domain within the United States, and
copyright and related rights in the work worldwide are waived through
the [CC0 1.0 Universal public domain
dedication](https://creativecommons.org/publicdomain/zero/1.0/).

All contributions to this project will be released under the CC0
dedication. By submitting a pull request, you are agreeing to comply
with this waiver of copyright interest.
