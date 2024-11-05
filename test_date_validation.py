import unittest
from main import is_leap_year, validate_date  

class TestDateValidation(unittest.TestCase):

    def test_is_leap_year(self):
        # Тесты для високосного года
        self.assertTrue(is_leap_year(2000))  # кратно 400
        self.assertTrue(is_leap_year(2024))  # кратно 4, не кратно 100
        self.assertFalse(is_leap_year(1900))  # кратно 100, но не 400
        self.assertFalse(is_leap_year(2023))  # не кратно 4

    def test_validate_date_valid_dates(self):
        # Проверка валидных дат
        self.assertEqual(validate_date("29.02.2024"), 1)  # високосный год
        self.assertEqual(validate_date("31.01.2023"), 1)  # Январь 31 день
        self.assertEqual(validate_date("30.04.2023"), 1)  # Апрель 30 дней

    def test_validate_date_invalid_dates(self):
        # Проверка невалидных дат
        self.assertEqual(validate_date("30.02.2023"), 0)  # Не високосный год
        self.assertEqual(validate_date("32.01.2023"), 0)  # Январь не имеет 32 дня
        self.assertEqual(validate_date("31.04.2023"), 0)  # Апрель не имеет 31 дня
        self.assertEqual(validate_date("15.13.2023"), 0)  # Неверный месяц
        self.assertEqual(validate_date("00.01.2023"), 0)  # День не может быть 0

if __name__ == "__main__":
    unittest.main()
