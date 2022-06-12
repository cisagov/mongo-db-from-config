"""This module contains the mongo_db_from_config code."""
# Standard Python Libraries
from typing import Dict

# Third-Party Libraries
from pymongo import MongoClient
from pymongo.database import Database
import yaml


def db_from_config(config_filename: str) -> Database:
    """Given a YAML file, return a corresponding MongoDB connection.

    Sample config file:
    database:
      uri: mongodb://<username>:<password>@<hostname>:<port>/<auth-db-name>
      name: <db-name>

    Parameters
    ----------
    config_filename : str
        The name of the YAML file containing the configuration information

    Returns
    -------
    pymongo.database.Database: A connection to the desired MongoDB database

    Throws
    ------
    FileNotFoundError: If the database configuration file does not exist

    yaml.parser.ParserError, yaml.scanner.ScannerError: If the YAML in the
    database configuration file is invalid

    KeyError: If the YAML in the database configuration file is valid YAML
    but does not contain the expected keys

    """
    with open(config_filename, "r") as stream:
        # The loader must now be explicitly specified to avoid a
        # warning message.  See here for more details:
        # https://github.com/yaml/pyyaml/wiki/PyYAML-yaml.load(input)-Deprecation
        config: Dict[str, Dict[str, str]] = yaml.load(stream, Loader=yaml.SafeLoader)

    db_uri: str = config["database"]["uri"]
    db_name: str = config["database"]["name"]

    db_connection: MongoClient = MongoClient(host=db_uri, tz_aware=True)

    return db_connection[db_name]
