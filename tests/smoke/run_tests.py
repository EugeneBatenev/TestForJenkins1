"""Produces a small Allure result for the smoke mock suite."""

import json
import os
import time
import uuid
from pathlib import Path


results_dir = Path(os.getenv("ALLURE_RESULTS_DIR", "allure-results"))
results_dir.mkdir(parents=True, exist_ok=True)
test_uuid = str(uuid.uuid4())
started = int(time.time() * 1000)

attachment = "smoke-login-log.txt"
(results_dir / attachment).write_text("Mock smoke check: login endpoint is available.\n", encoding="utf-8")

result = {
    "uuid": test_uuid,
    "historyId": "mock-smoke-login",
    "testCaseId": "mock-smoke-login",
    "fullName": "smoke.MockLoginTest.test_login",
    "name": "Mock login smoke test",
    "status": "passed",
    "stage": "finished",
    "start": started,
    "stop": started + 1,
    "attachments": [{"name": "mock log", "source": attachment, "type": "text/plain"}],
}
(results_dir / "smoke-login-result.json").write_text(json.dumps(result), encoding="utf-8")
print("Created smoke Allure result")
