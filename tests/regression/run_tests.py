"""Produces a small Allure result for the regression mock suite."""

import json
import os
import time
import uuid
from pathlib import Path


results_dir = Path(os.getenv("ALLURE_RESULTS_DIR", "allure-results"))
results_dir.mkdir(parents=True, exist_ok=True)
test_uuid = str(uuid.uuid4())
started = int(time.time() * 1000)

attachment = "regression-payment-log.txt"
(results_dir / attachment).write_text("Mock regression check: payment response is valid.\n", encoding="utf-8")

result = {
    "uuid": test_uuid,
    "historyId": "mock-regression-payment",
    "testCaseId": "mock-regression-payment",
    "fullName": "regression.MockPaymentTest.test_payment",
    "name": "Mock payment regression test",
    "status": "passed",
    "stage": "finished",
    "start": started,
    "stop": started + 1,
    "attachments": [{"name": "mock log", "source": attachment, "type": "text/plain"}],
}
(results_dir / "regression-payment-result.json").write_text(json.dumps(result), encoding="utf-8")
print("Created regression Allure result")
