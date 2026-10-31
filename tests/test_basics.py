import pytest

# Наша функция, которую мы "тестируем" (проверяем, что она работает правильно)
def is_adult(age):
    return age >= 18

# @pytest.mark.parametrize позволяет запустить один тест с разными данными
@pytest.mark.parametrize("age, expected_result", [
    (20, True),   # Позитивный тест (взрослый)
    (15, False),  # Негативный тест (ребенок)
    (18, True),   # Граничное значение (ровно 18)
    (0, False),   # Нулевой возраст
])
def test_is_adult(age, expected_result):
    # assert - это проверка. Если условие False, тест падает.
    assert is_adult(age) == expected_result