from {{cookiecutter.project_name}} import app  # noqa
from fastapi.testclient import TestClient

import pytest

client = TestClient(app)


@pytest.fixture(scope="session")
def test_client():
    yield test_client
