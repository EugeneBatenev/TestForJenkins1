"""Produces five Allure results for the regression mock suite."""

import json
import os
import time
import uuid
from pathlib import Path


results_dir = Path(os.getenv("ALLURE_RESULTS_DIR", "allure-results"))
results_dir.mkdir(parents=True, exist_ok=True)
started = int(time.time() * 1000)

for number in range(1, 6):
    attachment = f"regression-{number}-log.txt"
    (results_dir / attachment).write_text(f"Mock regression check #{number} passed.\n", encoding="utf-8")
    result = {
        "uuid": str(uuid.uuid4()),
        "historyId": f"mock-regression-{number}",
        "testCaseId": f"mock-regression-{number}",
        "fullName": f"regression.MockRegressionTest.test_check_{number}",
        "name": f"Mock regression test #{number}",
        "status": "passed",
        "stage": "finished",
        "start": started + number,
        "stop": started + number + 1,
        "attachments": [{"name": "mock log", "source": attachment, "type": "text/plain"}],
    }
    (results_dir / f"regression-{number}-result.json").write_text(json.dumps(result), encoding="utf-8")

print("Created 5 regression Allure results")
