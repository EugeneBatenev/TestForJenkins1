"""Five simple regression tests instrumented by Allure Framework."""

import allure
import pytest


@allure.feature("Jenkins mock tests")
@allure.story("Regression suite")
@allure.label("layer", "api")
@allure.title("Regression mock test #{number}")
@pytest.mark.parametrize("number", range(1, 6), ids=lambda number: f"regression-{number}")
def test_regression_check(number: int) -> None:
    with allure.step(f"Run mock regression check #{number}"):
        actual = "valid"
        expected = "valid"
        allure.attach(f"Mock regression check #{number} passed.", "mock log", allure.attachment_type.TEXT)

    with allure.step("Verify mock response"):
        assert actual == expected

@allure.feature("Jenkins mock tests")
@allure.story("Regression suite")
@allure.label("layer", "api")
@allure.title("Regression mock test #{number}")
@pytest.mark.parametrize("number", range(1, 6), ids=lambda number: f"regression-{number}")
def test_regression_check2(number: int) -> None:
    with allure.step(f"Run mock regression check #{number}"):
        actual = "valid"
        expected = "valid"
        allure.attach(f"Mock regression check #{number} passed.", "mock log", allure.attachment_type.TEXT)

    with allure.step("Verify mock response"):
        assert actual == expected

@allure.feature("Jenkins mock tests")
@allure.story("Regression suite")
@allure.label("layer", "api")
@allure.title("Regression mock test #{number}")
@pytest.mark.parametrize("number", range(1, 6), ids=lambda number: f"regression-{number}")
def test_regression_check3(number: int) -> None:
    with allure.step(f"Run mock regression check #{number}"):
        actual = "valid"
        expected = "valid"
        allure.attach(f"Mock regression check #{number} passed.", "mock log", allure.attachment_type.TEXT)

    with allure.step("Verify mock response"):
        assert actual == expected
