import re
import requests
from bs4 import BeautifulSoup

# Функция для проверки високосного года
def is_leap_year(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

# Основная функция для проверки даты с учетом високосных годов
def validate_date(date):
    # Проверка формата
    match = re.match(pattern, date)
    if not match:
        return 0
    
    # Извлечение дня, месяца и года
    day, month, year = int(date[:2]), int(date[3:5]), int(date[6:])
    
    # Проверка допустимого количества дней в каждом месяце
    if month in {1, 3, 5, 7, 8, 10, 12}:
        max_days = 31
    elif month in {4, 6, 9, 11}:
        max_days = 30
    elif month == 2:
        max_days = 29 if is_leap_year(year) else 28
    else:
        return 0
    
    # Финальная проверка дня
    if 1 <= day <= max_days:
        return 1
    else:
        return 0

    

def menu():
    print("1)Проверить дату", 
          "2)Найти все даты в файле",
          "3)Найти даты на сайте по URL", 
          "4)Выйти из программы", sep="\n")
    
    user_choice = input()
    if not user_choice.isdigit(): # Проверяем на то, что это число
        print("Ошибочный ввод данных, попробуйте еще раз!")
        menu()
    user_choice = int(user_choice)

    if user_choice == 1: # 1
        print("Введите строку:")
        user_input = input()

        matches = re.findall(pattern, user_input)
        if matches:
            # Преобразуем найденные группы в формат дат
            print("Найденные даты:", [".".join(match[:3]) for match in matches])
        else:
            print("Совпадений не найдено!")
        menu()

    elif user_choice == 2: # 2
        filename = "Text.txt" # https://www.polovinka.org/goroskop_po_date_rozhdenija/8-01-2006/
        try:
            with open(filename, 'r', encoding='utf-8') as file:
                content = file.read()
                matches = re.findall(pattern, content)
                if matches:
                    print("Всего совпадений: ", len(matches))
                    print("Найденные даты:", [".".join(match[:3]) for match in matches])
                else:
                    print("Совпадений не найдено в файле!")
        except FileNotFoundError:
            print("Файл не найден. Проверьте путь и попробуйте снова.")
        menu()
    elif user_choice == 3: # 3
        print("Введите URL страницы:")
        url = input()
        try:
            response = requests.get(url) # Загружают HTML-код страницы.
            response.raise_for_status() # Проверяют, успешна ли загрузка.
            soup = BeautifulSoup(response.text, 'html.parser') # Создают объект для удобного парсинга HTML.
            page_text = soup.get_text() # Извлекают чистый текст из HTML-кода, чтобы его можно было проанализировать на наличие нужной информации.

            matches = re.findall(pattern, page_text)
            if matches:
                print("Всего совпадений:", len(matches))
                print("Найденные даты:", [".".join(match[:3]) for match in matches])
            else:
                print("Совпадений не найдено на странице!")
        except requests.exceptions.RequestException as e:
            print("Ошибка при загрузке страницы:", e)
        menu()

    elif user_choice == 4: # 4
        return 0
    
    else:
        print("Неправильный ввод. Попробуйте еще раз\n")
        menu()

    


def main():
    global pattern
    # Регулярное выражение для формата ДД.ММ.ГГГГ до 2024 включительно
    pattern = r'(0[1-9]|[12][0-9]|3[01])\.(0[1-9]|1[0-2])\.(19\d{2}|20(0\d|1\d|2[0-4]))'
    menu()
    return 0


if __name__ == "__main__":
    main()