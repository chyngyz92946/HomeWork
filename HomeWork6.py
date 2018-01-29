import random

alphabet = 'abcdefghijklmnopqrstuvwxyz'



def generate_word(n, min_n=0):
    '''
    Функция составляет слово из 26 букв
    '''
    word = ""
    for i in range(random.randrange(min_n, n)):
        word += alphabet[random.randrange(26)]
    return word


def generate_word_list(max_length, max_count_word, min_count_word=0):
    '''
    Функция принимает максимальную длину, максимальное количество букв и минимальное количество слов
    '''
    words = list()
    for i in range(random.randrange(min_count_word, max_count_word)):
        words.append(generate_word(max_length))

    return words

print(generate_word_list(10, 15, 3))
