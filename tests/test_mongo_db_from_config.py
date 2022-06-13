#!/usr/bin/env pytest -vs
"""Tests for mongo_db_from_config."""
# Standard Python Libraries
import os

# Third-Party Libraries
import mongomock
import pytest

# cisagov Libraries
import mongo_db_from_config

# define sources of version strings
RELEASE_TAG = os.getenv("RELEASE_TAG")
PROJECT_VERSION = mongo_db_from_config.__version__


@pytest.mark.skipif(
    RELEASE_TAG in [None, ""], reason="this is not a release (RELEASE_TAG not set)"
)
def test_release_version():
    """Verify that release tag version agrees with the module version."""
    assert (
        RELEASE_TAG == f"v{PROJECT_VERSION}"
    ), "RELEASE_TAG does not match the project version"


def test_db_from_config_bad_yaml_no_database_entry():
    """Test that YAML parsing fails due to a missing database entry."""
    with pytest.raises(KeyError) as e_info:
        db_connection = mongo_db_from_config.db_from_config(
            "no_database_configuration.yml"
        )
        assert (
            db_connection.list_collection_names() == []
        ), "Testing database should have no collections"
    assert e_info.value.args[0] == "database", "Expected a missing 'database' key"


def test_db_from_config_bad_yaml_no_db_uri():
    """Test that YAML parsing fails due to a missing database URI entry."""
    with pytest.raises(KeyError) as e_info:
        db_connection = mongo_db_from_config.db_from_config(
            "no_database_uri_configuration.yml"
        )
        assert (
            db_connection.list_collection_names() == []
        ), "Testing database should have no collections"
    assert e_info.value.args[0] == "uri", "Expected a missing 'uri' key"


def test_db_from_config_bad_yaml_no_db_name():
    """Test that YAML parsing fails due to a missing database name entry."""
    with pytest.raises(KeyError) as e_info:
        db_connection = mongo_db_from_config.db_from_config(
            "no_database_name_configuration.yml"
        )
        assert (
            db_connection.list_collection_names() == []
        ), "Testing database should have no collections"
    assert e_info.value.args[0] == "name", "Expected a missing 'name' key"


@mongomock.patch(servers=(("server.cisa.gov", 8421),))
def test_db_from_config_successful_connection():
    """Test that a MongoDB database connection is successfully created."""
    db_connection = mongo_db_from_config.db_from_config("good_configuration.yml")
    assert (
        db_connection.list_collection_names() == []
    ), "Testing database should have no collections"


@mongomock.patch()
def test_db_from_config_failed_connection():
    """Test that a MongoDB database connection fails to be created."""
    with pytest.raises(ValueError) as e_info:
        db_connection = mongo_db_from_config.db_from_config("good_configuration.yml")
        assert (
            db_connection.list_collection_names() == []
        ), "Testing database should have no collections"
    assert (
        "MongoDB server server.cisa.gov:8421 does not exist." in e_info.value.args[0]
    ), "Unexpected exception was thrown"
