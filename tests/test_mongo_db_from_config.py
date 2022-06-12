#!/usr/bin/env pytest -vs
"""Tests for mongo_db_from_config."""

# Standard Python Libraries
import os

# Third-Party Libraries
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
