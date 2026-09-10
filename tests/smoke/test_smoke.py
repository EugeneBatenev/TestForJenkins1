"""Ten simple smoke tests instrumented by Allure Framework."""

import allure
import pytest


@allure.feature("Jenkins mock tests")
@allure.story("Smoke suite")
@allure.label("layer", "api")
@allure.title("Smoke mock test #{number}")
@pytest.mark.parametrize("number", range(1, 11), ids=lambda number: f"smoke-{number}")
def test_smoke_check(number: int) -> None:
    with allure.step(f"Run mock smoke check #{number}"):
        actual = "available"
        expected = "available"
        allure.attach(f"Mock smoke check #{number} passed.", "mock log", allure.attachment_type.TEXT)

    with allure.step("Verify mock response"):
        assert actual == expected
