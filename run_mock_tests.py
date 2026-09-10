"""Entry point used by Jenkins to select one pytest + Allure test suite."""

import os
import subprocess
import sys
from pathlib import Path


SUITES = {
    "smoke": "tests/smoke",
    "regression": "tests/regression",
}


def main() -> int:
    suite = os.getenv("MOCK_TEST_SUITE", "smoke")
    tests_dir = SUITES.get(suite)
    if tests_dir is None:
        print(f"Unknown MOCK_TEST_SUITE: {suite}. Allowed values: {', '.join(SUITES)}")
        return 2

    print(f"Running mock suite: {suite}")
    results_dir = os.getenv("ALLURE_RESULTS_DIR", "allure-results")
    return subprocess.call(
        [sys.executable, "-m", "pytest", str(Path(__file__).parent / tests_dir), f"--alluredir={results_dir}"]
    )


if __name__ == "__main__":
    raise SystemExit(main())
