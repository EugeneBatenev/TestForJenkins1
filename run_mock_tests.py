"""Entry point used by Jenkins to select one mock test suite."""

import os
import subprocess
import sys
from pathlib import Path


SUITES = {
    "smoke": "tests/smoke/run_tests.py",
    "regression": "tests/regression/run_tests.py",
}


def main() -> int:
    suite = os.getenv("MOCK_TEST_SUITE", "smoke")
    script = SUITES.get(suite)
    if script is None:
        print(f"Unknown MOCK_TEST_SUITE: {suite}. Allowed values: {', '.join(SUITES)}")
        return 2

    print(f"Running mock suite: {suite}")
    return subprocess.call([sys.executable, str(Path(__file__).parent / script)])


if __name__ == "__main__":
    raise SystemExit(main())
