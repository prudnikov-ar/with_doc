"""
Вариант 20
"""
from pickle import dump, load
from fnmatch import fnmatch
from pprint import pprint

def update(base: dict) -> None:
    """
    Записывает данные в бинарный файл.
    
    Аргументы:
    - base (dict): Словарь с данными для сохранения.
    
    Возвращаемое значение:
    - None
    
    Возможные исключения:
    - IOError: ошибка записи файла.
    
    Пример использования:
    update(my_base)
    """
    with open("op3.bin", "wb") as file:
        dump(base, file=file)

def check() -> dict:
    """
    Загружает и возвращает данные из бинарного файла.
    
    Возвращаемое значение:
    - dict: Словарь загруженных данных.
    
    Возможные исключения:
    - IOError: ошибка чтения файла.
    - EOFError: ошибка при чтении данных, если файл пуст.
    
    Пример использования:
    data = check()
    """
    with open("op3.bin", "rb") as file:
        return load(file)

def search(found: str, base: dict) -> None:
    """
    Поиск данных по фамилии в базе данных.
    
    Аргументы:
    - found (str): Фамилия для поиска.
    - base (dict): Словарь с данными базы.
    
    Возвращаемое значение:
    - None
    
    Сторонние эффекты:
    - Вывод данных пользователя или сообщения о его отсутствии в консоль.
    
    Пример использования:
    search("Иванов", my_base)
    """
    flag = True
    for key in base:
        if base[key]["фамилия"] == found:
            flag = False
            print()
            print(base[key])
    if flag:
        print()
        print("Такого пользователя нет")

def top_stud(count: int, base: dict) -> None:
    """
    Отображает сортированный список студентов по убыванию среднего балла.
    
    Аргументы:
    - count (int): Количество топ студентов для вывода.
    - base (dict): Словарь с данными о студентах.
    
    Возвращаемое значение:
    - None
    
    Сторонние эффекты:
    - Вывод сортированного списка студентов в консоль.
    
    Пример использования:
    top_stud(5, my_base)
    """
    list_cort = sorted(base.keys(), key=lambda x: base[x]['средний балл'], reverse=True)

    print("Номера зачёток представлены в порядке убывания средних баллов студента", end="\n\n")
    for i in range(count):
        print(base[list_cort[i]])
        print(list_cort[i])

def app(new: list, base: dict) -> None:
    """
    Добавление нового пользователя в базу данных.
    
    Аргументы:
    - new (list): Список информации о новом пользователе.
    - base (dict): База данных, куда будет добавлен новый пользователь.
    
    Возвращаемое значение:
    - None
    
    Возможные исключения:
    - IndexError: Если в списке 'new' недостаточно элементов.
    
    Пример использования:
    new_user_info = ["12345", "Иванов", "Иван", "Иванович", "01.01.99", 5]
    app(new_user_info, my_base)
    """
    base[new[0]] = {}
    base[new[0]]["фамилия"] = new[1]
    base[new[0]]["имя"] = new[2]
    base[new[0]]["отчество"] = new[3]
    base[new[0]]["дата рождения"] = new[4]
    base[new[0]]["средний балл"] = new[5]

    update(base)

def new_person() -> list:
    """
    Ввод данных нового пользователя с валидацией.
    
    Возвращаемое значение:
    - list: Список с данными нового пользователя или -1 в случае некорректного ввода.
    
    Сторонние эффекты:
    - Вывод подсказки и получение ввода через консоль.
    
    Пример использования:
    new_user_data = new_person()
    if new_user_data != -1:
        app(new_user_data, my_base)
    """
    person = []
    print()
    print("Введите номер зачётки")
    recbook = input().strip()
    if " " not in recbook and recbook.isdigit():
        person.append(recbook)
    else:
        print()
        print("Некорректный ввод")
        return -1
    print("Введите фамилию")
    lastn = input().strip()
    if " " not in lastn and not lastn.isdigit():
        person.append(lastn)
    else:
        print()
        print("Error. На вход принимается одно слово")
        return -1
    print("Введите имя")
    name = input().strip()
    person.append(name)
    print("Введите отчество")
    thrn = input().strip()
    if " " not in thrn and not thrn.isdigit():
        person.append(thrn)
    else:
        print()
        print("Error. На вход принимается одно слово")
        return -1
    print("Введите дату рождения ДД.ММ.ГГ")
    date = input().strip()
    if " " not in date and fnmatch(date, "??.??.??"):
        person.append(date)
    else:
        print()
        print("На вход принимается формат ДД.ММ.ГГ")
        return -1
    print("Введите средний балл")
    rate = input().strip()
    if " " not in rate and rate.isdigit():
        person.append(rate)
    else:
        print()
        print("На вход принимается одно число")
        return -1

    return person
    
def check_number(dig, base: dict) -> None:
    """
    Проверка числа и вывод топ студентов, если число допустимо.
    
    Аргументы:
    - dig (str): Строка, представляющая число топ студентов для вывода.
    - base (dict): База данных о студентах.
    
    Возвращаемое значение:
    - None или -1 в случае невозможности преобразования 'dig' в int.
    
    Возможные исключения:
    - ValueError: если 'dig' не может быть преобразован в int.
    
    Пример использования:
    check_number('5', my_base)
    """
    try:
        dig = int(dig)
    except ValueError:
        print()
        print("Некорректный ввод")
        return -1
    if len(base) >= dig > 0:
        top_stud(dig, base)
    else:
        print()
        print("В БД всего", len(base), "пользователей")
    return None

def rem() -> None:
    """
    Удаление пользователя из базы данных по номеру зачетной книжки.
    
    Возвращаемое значение:
    - None
    
    Сторонние эффекты:
    - Запрашивает номер зачетной книжки через консоль.
    - Выводит данные удаленного пользователя или ошибку в консоль.
    - Обновляет базу данных, сохраняя ее в файл после удаления пользователя.
    
    Пример использования:
    rem()
    """
    base = check()
    if len(base) > 0:
        print()
        pprint(base)
        print()
        print("Введите номер зачётной книжки студента, которого хотите удалить")
        number_book = input()
        if " " not in number_book and number_book in base:
            print()
            print("Был удалён:", base.pop(number_book))
            update(base)
        else:
            print()
            print("Такого пользователя не существует или вы ввели данные некорректно")
    else:
        print()
        print("БД пуста")

def main():
    """Меню"""
    data = {}
    while True:

        print()
        print("Меню")
        print("Введите 1 чтобы записать нового пользователя")
        print("Введите 2 чтобы вывести студентов с высоким баллом")
        print("Введите 3 чтобы вывести всю базу данных")
        print("Введите 4 чтобы удалить студента")
        print("Введиет 5 чтобы найти данные пользователя по фамилии")
        print("Введите 6 чтобы завершить программу")

        ans = input()
        if ans == "1":
            new_data = new_person()
            if new_data == -1:
                continue
            app(new_data, data)
            print()
            print("Данные успешно добавлены в БД!")
            print()
        elif ans == "2":
            data = check()
            if len(data) > 0:
                print()
                print("Введите число лучших студентов")
                number = input()
                if check_number(number, data) == -1:
                    continue
            else:
                print()
                print("БД пуста")
        elif ans == "3":
            data = check()
            pprint(data)
        elif ans == "4":
            rem()
        elif ans == "5":
            data = check()
            print()
            print("Введите фамилию пользователя")
            family = input()
            search(family, data)
        elif ans == "6":
            print()
            print("Программа завершена")
            break
        else:
            print()
            print("Такой команды нет")


main()