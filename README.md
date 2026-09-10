# TestForJenkins1

Набор минимальных мок-тестов для запуска из Jenkins и передачи результатов в Allure TestOps.

## Запуск

Выбор набора выполняется переменной окружения `MOCK_TEST_SUITE`:

```bash
MOCK_TEST_SUITE=smoke python3 run_mock_tests.py
MOCK_TEST_SUITE=regression python3 run_mock_tests.py
```

По умолчанию запускается `smoke`. Результаты Allure сохраняются в `allure-results`; путь можно переопределить через `ALLURE_RESULTS_DIR`.

Наборы расположены отдельно:

- `tests/smoke` — создаёт `smoke-login-result.json` и `smoke-login-log.txt`;
- `tests/regression` — создаёт `regression-payment-result.json` и `regression-payment-log.txt`.
