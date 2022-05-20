# Индивидуальное задание по учебной практике. ГУАП. Весна 2022.
___
## Алгоритм сортировки текстового файла.
### Используемый метод сортировки - Сортировка Пузырьком.
___
## Задача:
Целью выполняемой работы является реализация и анализ эффективности одного из способов сортировки текста (прим. Сортировка Пузырьком). Пузырьковая сортировка относится к классу обменных сортировок, т.е. к классу сортировок методом обмена. Ее алгоритм содержит повторяющиеся сравнения (т.е. многократные сравнения одних и тех же элементов) и, при необходимости, обмен соседних элементов. Элементы ведут себя подобно пузырькам воздуха в воде — каждый из них поднимается на свой уровень.

В сортировке методом пузырька количество итераций внешнего цикла определяется длинной списка “минус единица”, так как, когда второй элемент становится на свое место, то первый уже однозначно минимальный и находится на своем месте. Количество итераций внутреннего цикла зависит от номера итерации внешнего цикла, так как конец списка уже отсортирован, и выполнять проход по этим элементам смысла нет.

Полученные результаты сортировки необходимо записать в результирующий и анализирующий файлы.
___
### Реализация программы проходит в три этапа.
___
#### Первый этап:
*Программа получает обычный текстовый файл на кириллице:*
![image](https://user-images.githubusercontent.com/105930384/169568857-3e4a1ba7-e904-400a-8ff5-6bbfacc0bde9.png)

Далее необходимо изабвиться от знаков пунктуации, разделить слова и цифры и записать их в отдельные массивы.

Для использования кириллицы при решениии поставленной задачи используются массивы с буквами в верхнем и нижнем регистре:
```python
cyrillic = [chr(letter) for letter in range(ord('А'), ord('я') + 1)]  # массив с буквами кириллического алфавита
cyrillic_lower = [chr(letter) for letter in range(ord('а'), ord('я') + 1)]  # массив с буквами в нижнем регистре
cyrillic_upper = [chr(letter) for letter in range(ord('А'), ord('Я') + 1)]  # массив с буквами в верхнем регистре
```

Удаляем знаки пунктуации, делим слова и цифры и записываем их в массивы:
```python
def excess_characters(f):  # функция для удаления знаков пунктуации, разделения слов и чисел и записи их в массивы
    data_to_extract = open(f'{f}.txt', 'r', encoding='utf-8').read()  # подключение файла
    data = data_to_extract.split()  # разделение всех элементов текста по пробелу
    data_words = [word.strip(string.punctuation) for word in data if word[0] in cyrillic and word != '']  # запись слов в массив
    data_words = [word.replace(string.punctuation, '') for word in data_words]  # проверка на присутствие знаков пунктуации по бокам слов или чисел
    data_digits = [int(digit) for digit in data if digit[0] in string.digits]  # запись чисел в массив
    return data_words, data_digits, data_to_extract  # возврат функцией исходного текста и массивов со словами и числами
```
___
#### Второй этап:
Алгоритм для сортировки массивов.
```python
def bubble_sort(words, digits):  # функция для сортировки слов и чисел
    for i in range(len(words)):  # цикл, который идёт по словам
        for j in range(len(words)):  # цикл, который идёт по первому элементу слова
            if words[i][0] <= words[j][0]:  # сравнение элемента с последующим
                temp1 = words[i]  # запись слова в первую ячейку памяти
                temp2 = words[j]  # запись последующего слова во вторую ячейку памяти
                words[j] = temp1  # замена местами элементов
                words[i] = temp2  # замена местами элементов
    for i in range(len(digits)):  # цикл, который идёт по числам
        for j in range(len(digits)):  # цикл, который идёт по первому элементу числа
            if digits[i] <= digits[j]:  # сравнение элемента с последующим
                temp1 = digits[i]  # запись числа в первую ячейку памяти
                temp2 = digits[j]  # запись последующего числа во вторую ячейку памяти
                digits[j] = temp1  # замена местами элементов
                digits[i] = temp2  # замена местами элементов
    return words, digits  # возврат функцией отсортированных массивов со словами и числами
``` 
___
#### Третий этап:
    
Запись полученных результатов в результирующий и анализирующий файлы.
```python
def to_file(original_text, words, digits, time):  # функция сортировки пузырьком
    result = open('C:\\Users\\User\\Documents\\SUAI\\ОП\\Учебная Практика\\Text\\10. Result.txt', 'w', encoding='utf-8')  # открытие результирующего файла
    for letter in cyrillic_upper:  # цикл, который идёт по буквам, содержащихся в массиве высокого регистра
        flag = 0  # флаг (реагирование)
        for word in words:  # цикл, который идёт по словам в массиве
            if word[0] == letter or word[0] == letter.lower():  # проверка условия
                result.write(word + ' ')  # запись в результирующий файл
                flag = 1  # срабатывание флага (реагирование)
        if flag == 1:  # проверка срабатывания флага
            result.write('\n')  # если срабатывает флаг, то программа переходит на новую строчку
    for digit in digits:  # цикл, который идёт по числам
        result.write(str(digit))  # запись чисел в результирующий файл
        result.write('\n')  # переход на новую строчку
    result.close()  # закрытие результирующего файла
    analysis = open('C:\\Users\\User\\Documents\\SUAI\\ОП\\Учебная Практика\\Text\\10. Analysis.txt', 'w', encoding='utf-8')  # открытие анализирующего файла
    analysis.write(f"""Введенный текст: \n
{original_text} \n
Вариант 1: кириллица, по алфавиту, по возрастанию, учитывать числа, сортировка пузырьком. \n
Количество слов: {len(words)} \n
Время сортировки: {round(time, 4)} сек \n
Статистика:\n""")  # запись всей статистики в анализирующий файл
    for letter in cyrillic_lower:  # цикл, который идёт по буквам, содержащихся в массиве нижнего регистра 
        count = 0
        for word in words:
            if word.startswith(letter) or word.startswith(letter.upper()):  # проверка условия
                count += 1
        analysis.write(f'{letter} - {count}\n')  # запись в анализирующий файл

    for digit in digits:
        analysis.write(str(digit) + "\n")  # запись в анализирующий файл
```
*Результирующий файл:*
![image](https://user-images.githubusercontent.com/105930384/169568361-90aba267-86d2-42a4-a4e9-f66bdb97a56e.png)

*Анализирующий файл:*
![image](https://user-images.githubusercontent.com/105930384/169568825-89f8631e-2530-4f66-820f-3267a84f6430.png)
___
Подключение файла и вызов все задействованных функций.
```python
try:
    name = input('Введите путь к файлу:')  # абсолютный путь к файлу
    time_to_start = time.time()  # начало отсчёта времени, за которое сортируется файл
    list_of_words, list_of_digits, text = excess_characters(name)  # переменные для слов, чисел и исходного текста
    sorted_words, sorted_digits = bubble_sort(list_of_words, list_of_digits)  # переменные для сортированных слов и чисел
    time_to_finish = time.time()  # конец отсчёта времени, за которое отсортировался файл
    search_time = time_to_finish - time_to_start  # высчет искомого времени сортировки
    to_file(text, sorted_words, sorted_digits, search_time)  # запись результатов в результирующий и анализирующий файлы
except FileNotFoundError:
    print('Файла не существует.')
```
___
### Исходный код программы:
```python
import string
import time


def excess_characters(f):
    data_to_extract = open(f'{f}.txt', 'r', encoding='utf-8').read()
    data = data_to_extract.split()
    data_words = [word.strip(string.punctuation) for word in data if word[0] in cyrillic and word != '']
    data_words = [word.replace(string.punctuation, '') for word in data_words]
    data_digits = [int(digit) for digit in data if digit[0] in string.digits]
    return data_words, data_digits, data_to_extract


def bubble_sort(words, digits):
    for i in range(len(words)):
        for j in range(len(words)):
            if words[i][0] <= words[j][0]:
                temp1 = words[i]
                temp2 = words[j]
                words[j] = temp1
                words[i] = temp2
    for i in range(len(digits)):
        for j in range(len(digits)):
            if digits[i] <= digits[j]:
                temp1 = digits[i]
                temp2 = digits[j]
                digits[j] = temp1
                digits[i] = temp2
    return words, digits


def to_file(original_text, words, digits, time):
    result = open('C:\\Users\\User\\Documents\\SUAI\\ОП\\Учебная Практика\\Text\\10. Result.txt', 'w', encoding='utf-8')
    for letter in cyrillic_upper:
        flag = 0
        for word in words:
            if word[0] == letter or word[0] == letter.lower():
                result.write(word + ' ')
                flag = 1
        if flag == 1:
            result.write('\n')
    for digit in digits:
        result.write(str(digit))
        result.write('\n')
    result.close()
    analysis = open('C:\\Users\\User\\Documents\\SUAI\\ОП\\Учебная Практика\\Text\\10. Analysis.txt', 'w', encoding='utf-8')
    analysis.write(f"""Введенный текст: \n
{original_text} \n
Вариант 1: кириллица, по алфавиту, по возрастанию, учитывать числа, сортировка пузырьком. \n
Количество слов: {len(words)} \n
Время сортировки: {round(time, 4)} сек \n
Статистика:\n""")
    for letter in cyrillic_lower:
        count = 0
        for word in words:
            if word.startswith(letter) or word.startswith(letter.upper()):
                count += 1
        analysis.write(f'{letter} - {count}\n')

    for digit in digits:
        analysis.write(str(digit) + "\n")


cyrillic = [chr(letter) for letter in range(ord('А'), ord('я') + 1)]
cyrillic_lower = [chr(letter) for letter in range(ord('а'), ord('я') + 1)]
cyrillic_upper = [chr(letter) for letter in range(ord('А'), ord('Я') + 1)]


try:
    name = input('Введите путь к файлу:')
    time_to_start = time.time()
    list_of_words, list_of_digits, text = excess_characters(name)
    sorted_words, sorted_digits = bubble_sort(list_of_words, list_of_digits)
    time_to_finish = time.time()
    search_time = time_to_finish - time_to_start
    to_file(text, sorted_words, sorted_digits, search_time)
except FileNotFoundError:
    print('Файла не существует.')

```
___
## Проблемы, с которыми пришлось столкнуться.
По началу сортировка проходила некорректно. Буквы в верхнем и нижнем регистре считывались программой как разные элементы.
Для этого пришлось создать два массива, один с буквами в нижнем регистре, другой - в высоком регистре.
___
## Клёвая фишка, которая упростила жизнь.
В великолепной беблиотеке ***string*** существует метод ***string.punctuation***, с помощью которого было очень просто удалить знаки пункутации из исходного текста.
Не потребовалось создавать отдельный массив со всеми элементами пунктуации.
___
## Установка проекта
Для реализаций программы необходимо установить на ПК среду разработки PyCharm, выбрать текст, которые нужно отсортировать, подключить файл с текстом и запустить программу.
