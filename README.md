# TestForJenkins1

Набор минимальных мок-тестов для запуска из Jenkins и передачи результатов в Allure TestOps.

## Запуск

Выбор набора выполняется переменной окружения `MOCK_TEST_SUITE`:

```bash
python3 -m pip install -r requirements.txt
MOCK_TEST_SUITE=smoke python3 run_mock_tests.py
MOCK_TEST_SUITE=regression python3 run_mock_tests.py
```

По умолчанию запускается `smoke`. Это pytest-тесты с декораторами и шагами Allure Framework. Результаты Allure сохраняются в `allure-results`; путь можно переопределить через `ALLURE_RESULTS_DIR`.

Наборы расположены отдельно:

- `tests/smoke` — 10 мок-тестов и 10 отдельных Allure-result JSON-файлов;
- `tests/regression` — 5 мок-тестов и 5 отдельных Allure-result JSON-файлов.
