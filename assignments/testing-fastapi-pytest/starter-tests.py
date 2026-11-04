from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path

from fastapi.testclient import TestClient

module_path = Path(__file__).with_name("starter-code.py")
module_spec = spec_from_file_location("starter_code", module_path)
starter_code = module_from_spec(module_spec)
assert module_spec and module_spec.loader
module_spec.loader.exec_module(starter_code)

client = TestClient(starter_code.app)


def test_health_endpoint() -> None:
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


# TODO: Add tests for POST /items and GET /items
# TODO: Add tests for 404 cases in GET /items/{item_id} and DELETE /items/{item_id}
# TODO: Add a test for invalid payload (422) in POST /items
