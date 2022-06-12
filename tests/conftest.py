"""pytest plugin configuration.

https://docs.pytest.org/en/latest/writing_plugins.html#conftest-py-plugins
"""
# Standard Python Libraries
import copy
import os

# Third-Party Libraries
import pytest
import yaml

TEST_CONFIGURATION = "files/test_configuration.yml"


def pytest_addoption(parser):
    """Add new commandline options to pytest."""
    parser.addoption(
        "--runslow", action="store_true", default=False, help="run slow tests"
    )


def pytest_configure(config):
    """Register new markers."""
    config.addinivalue_line("markers", "slow: mark test as slow")


def pytest_collection_modifyitems(config, items):
    """Modify collected tests based on custom marks and commandline options."""
    if config.getoption("--runslow"):
        # --runslow given in cli: do not skip slow tests
        return
    skip_slow = pytest.mark.skip(reason="need --runslow option to run")
    for item in items:
        if "slow" in item.keywords:
            item.add_marker(skip_slow)


@pytest.fixture(autouse=True)
def test_fs(request, fs):
    """Set up the contents of the fake fillesystem."""
    fs.add_real_file(
        os.path.join(request.fspath.dirname, TEST_CONFIGURATION),
        target_path="good_configuration.yml",
    )
    with open("good_configuration.yml", "r") as good_config:
        base_config = yaml.load(good_config, Loader=yaml.SafeLoader)

    no_database_entry_config = copy.deepcopy(base_config)
    del no_database_entry_config["database"]
    fs.create_file(
        "no_database_configuration.yml",
        contents=yaml.dump(no_database_entry_config, explicit_start=True),
    )

    no_database_uri_entry_config = copy.deepcopy(base_config)
    del no_database_uri_entry_config["database"]["uri"]
    fs.create_file(
        "no_database_uri_configuration.yml",
        contents=yaml.dump(no_database_uri_entry_config, explicit_start=True),
    )

    no_database_name_entry_config = copy.deepcopy(base_config)
    del no_database_name_entry_config["database"]["name"]
    fs.create_file(
        "no_database_name_configuration.yml",
        contents=yaml.dump(no_database_name_entry_config, explicit_start=True),
    )
