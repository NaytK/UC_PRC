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