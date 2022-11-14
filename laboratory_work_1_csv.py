import csv
from random import randint

    # Счетчик записей:

def counter():
    with open('books.csv', 'r') as csv_file:
        file = csv.reader(csv_file, delimiter=' ')
        count = 0
        for string in file:
            count += 1
        return print(f'Общее количество записей: {count}\n')

    # Счетчик записей, у которых в поле название строка больше 30 символов

def smart_counter():
    with open('books.csv', 'r') as csv_file:
        file = csv.reader(csv_file, delimiter=';')
        count = 0
        for string in file:
            if len(string[1]) > 30:
                count += 1
        return print(f'Rоличество записей, у которых в поле строка больше 30 символов: {count}\n')

    # Выдача книг по ФИО автора с ограничением в 150 рублей:

def giver():
    with open('books.csv', 'r') as csv_file:
        file = csv.reader(csv_file, delimiter=';')
        book_author = input('Введите ФИО автора:')
        flag = False
        for string in file:
            if string[7] == 'Цена поступления':
                print('\n\tМы можем выдать Вам следующие книги этого автора: ')
            if string[4] == book_author:
                if float(string[7]) < 150:
                    book_name = string[1]
                    flag = True
                    print(f'"{book_name}"')
        if flag == False:
            print('К сожалению книг данного автора по заданному ограничению нет в нашем каталоге')
    return print('')

    # Генератор библиографических ссылок:

def link_generator():
    with open('books.csv', 'r') as csv_file:
        file = csv.reader(csv_file, delimiter=';')
        link_numbers = [randint(0, 9409) for i in range(20)]
        iteration = 0
        with open('output.txt', 'w+', encoding='utf8') as output:
            for link in file:
                if iteration in link_numbers:
                    output.write(f'<{link[4]}>. <{link[1]}> - <{link[6]}>\n')
                iteration += 1
    return print('')

    # Выдача всех тегов без повторений:

def tag():
    with open('books.csv', 'r') as csv_file:
        file = csv.reader(csv_file, delimiter=';')
        tags = []
        array = []
        for i in file:
            array = i[-1].rsplit(sep='# ')
            for j in range(len(array)):
                if array[j] not in tags:
                    if array[j] == 'Жанр книги':
                        continue
                    else:
                        tags.append(array[j])
    return print(tags)

counter()
smart_counter()
giver()
link_generator()
tag()