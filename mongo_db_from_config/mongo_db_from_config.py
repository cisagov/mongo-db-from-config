# third-party libraries (install with pip)
from pymongo import MongoClient
import yaml


def db_from_config(config_filename):
    """Create a MongoClient database connection from a YAML config file.

    Sample config file:
    [production]
    database-uri = mongodb://username:password@localhost:27017/auth-db-name
    database-name = db-name

    Parameters
    ----------
    config_filename : str
        The name of the yaml config file.

    Returns
    -------
    mongokit.database.Database: The Mongo database connection
    """
    db = None

    with open(config_filename, "r") as stream:
        # The loader must now be explicitly specified to avoid a
        # warning message.  See here for more details:
        # https://github.com/yaml/pyyaml/wiki/PyYAML-yaml.load(input)-Deprecation
        config = yaml.load(stream, Loader=yaml.SafeLoader)

    if config is not None:
        try:
            db_uri = config["database"]["uri"]
            db_name = config["database"]["name"]
        except KeyError:
            print("Incorrect database config file format: {}".format(config_filename))

        db_connection = MongoClient(host=db_uri, tz_aware=True)
        db = db_connection[db_name]

    return db
