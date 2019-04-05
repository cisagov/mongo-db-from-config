# mongo-db-from-config ⚙️ #

[![Build Status](https://travis-ci.com/cisagov/mongo-db-from-config.svg?branch=develop)](https://travis-ci.com/cisagov/mongo-db-from-config)
[![Total alerts](https://img.shields.io/lgtm/alerts/g/cisagov/mongo-db-from-config.svg?logo=lgtm&logoWidth=18)](https://lgtm.com/projects/g/cisagov/mongo-db-from-config/alerts/)
[![Language grade: Python](https://img.shields.io/lgtm/grade/python/g/cisagov/mongo-db-from-config.svg?logo=lgtm&logoWidth=18)](https://lgtm.com/projects/g/cisagov/mongo-db-from-config/context:python)

This is a small utility library that can be used to easily create a MongoDB
connection based on the data in a simple YAML configuration file.

## Installation ##

Run the following `pip` command to install this package:

```bash
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

We welcome contributions!  Please see [here](CONTRIBUTING.md) for
details.

## License ##

This project is in the worldwide [public domain](LICENSE.md).

This project is in the public domain within the United States, and
copyright and related rights in the work worldwide are waived through
the [CC0 1.0 Universal public domain
dedication](https://creativecommons.org/publicdomain/zero/1.0/).

All contributions to this project will be released under the CC0
dedication. By submitting a pull request, you are agreeing to comply
with this waiver of copyright interest.
