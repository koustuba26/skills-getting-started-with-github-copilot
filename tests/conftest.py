from fastapi.testclient import TestClient
import copy
import pytest

from src import app as _app

# Snapshot original activities for resetting between tests
_original_activities = copy.deepcopy(_app.activities)


@pytest.fixture
def client():
    _app.activities.clear()
    _app.activities.update(copy.deepcopy(_original_activities))
    with TestClient(_app.app) as c:
        yield c
