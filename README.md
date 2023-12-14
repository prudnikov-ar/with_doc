# Документация к программе
## Цель
**Изучить принципы работы с документацией программиста и оформление README файла. _Научиться оформлять комментарии_ в коде и README файл.**
  *В README.md файле должны быть использованы следующие пункты:
- маркированный список
- список с чек-боксами
- примеры кода
- формула
- заголовки
- текст полужирный и написанный курсивом
- ссылки
- изображения.

Уже выполнено:
- [x] маркированный список
- [x] список с чек-боксами
- [ ] примеры кода
- [ ] формула
- [x] заголовки
- [x] текст полужирный и написанный курсивом
- [ ] ссылки
- [ ] изображения.

Пример использования формул:

Когда $D > 0$, уравнение $(ax^2 + bx + c = 0)$ имеет два корня, которые можно найти следующим образом:

$$ x_{1}, x_{2} = {-b \pm \sqrt{D} \over 2a} $$

$$ D = b^2 - 4ac $$


Вот отрывок кода из моей программы с документацией:
```python
def update(base: dict) -> None:
    """
    Записывает данные в бинарный файл.
    
    Аргументы:
    - base (dict): Словарь с данными для сохранения.
    
    Возможные исключения:
    - IOError: ошибка записи файла.
    
    Пример использования:
    update(my_base)
    """
    with open("op3.bin", "wb") as file:
        dump(base, file=file)
```



