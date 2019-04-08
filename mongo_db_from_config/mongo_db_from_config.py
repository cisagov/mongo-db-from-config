def db_from_config(config_filename):
    """Given the name of the YAML file containing the configuration
    information, return a corresponding MongoDB connection.

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
    # third-party libraries (install with pip)
    from pymongo import MongoClient
    import yaml

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
