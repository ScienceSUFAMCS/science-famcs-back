import os
import sys
import pytest
from fastapi.testclient import TestClient

test_dir = os.path.dirname(__file__)
module_dir = os.path.join(test_dir, "../..")
sys.path.append(module_dir)

from app.main import app


client = TestClient(app)


@pytest.mark.asyncio
async def test_health_endpoint():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {}
