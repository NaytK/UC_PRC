import string
import time


def excess_characters(f):
    data_to_extract = open(f'{f}.txt', 'r', encoding='utf-8').read()
    data = data_to_extract.split()
    data_words = [word.strip(string.punctuation) for word in data if word[0] in cyrillic and word != '']
    data_words = [word.replace(string.punctuation, '') for word in data_words]
    data_digits = [int(digit) for digit in data if digit[0] in string.digits]
    return data_words, data_digits, data_to_extract

cyrillic = [chr(letter) for letter in range(ord('А'), ord('я') + 1)]
cyrillic_lower = [chr(letter) for letter in range(ord('а'), ord('я') + 1)]
cyrillic_upper = [chr(letter) for letter in range(ord('А'), ord('Я') + 1)]


try:
    name = input('Введите путь к файлу:')
    list_of_words, list_of_digits, text = excess_characters(name)
except FileNotFoundError:
    print('Файла не существует.')