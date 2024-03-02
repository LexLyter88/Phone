""" 
Создать телефонный справочник с возможностью импорта и экспорта данных в формате .txt. Фамилия, имя, отчество, номер
телефона - данные, которые должны находиться в файле.
1. Программа должна выводить данные
2. Программа должна сохранять данные в текстовом файле
3. Пользователь может ввести одну из характеристик для поиска определенной записи(Например имя или фамилию человека)
4. Использование функций. Ваша программа не должна быть линейной 
5. Дополнить справочник возможностью копирования данных из одного файла в другой. 
Пользователь вводит номер строки, которую необходимо перенести из одного файла в другой.
"""

import os
import re

def read_sprav():
    sprav = []
    file_path = 'sprav.txt'
    if not os.path.isfile(file_path):
        print(f"Создан файл справочника {file_path}")
        my_file = open("sprav.txt", "w+", encoding='utf-8')
        my_file.close()
    tel_sprav = open(file_path, 'r', encoding='utf-8')
    for line in tel_sprav:
        n = line.split()
        # print (n)
        if n != "\n":
            dict_ = {
                "first_name": n[0],
                "second_name": n[1],
                "last_name": n[2],
                "tel": n[3],
            }
            sprav.append(dict_)

    """Альтернативный вариант"""
    # headers = ['last_name', 'first_name', 'second_name', 'tel']
    # for line in tel_sprav:
    #     line = line.strip().split()
    #     sprav.append(dict(zip(headers, line)))
    tel_sprav.close()
    return sprav


def print_sprav(tel_sprav):
    if len(tel_sprav) > 0:
        for item in tel_sprav:
            #print(*(f"{k}: {v}" for k, v in item.items()))
            print(*(f"{v}" for v in item.values()))
            # print(item['last_name'], item['first_name'], item['second_name'], item['tel'])
    else:
        print("Нет контактов в справочнике")
    return None


def titlecase(s):
    return re.sub(r"[A-Za-z]+('[A-Za-z]+)?",
                  lambda mo: mo.group(0).capitalize(),
                  s)

def add_contact():
    tel_sprav = open('sprav.txt', 'a', encoding='utf-8')
    s = input("Введите ФИО, тел, резделенные пробелами: ").title()
    tel_sprav.write(f'{s}\n')
    tel_sprav.close()


def find_last_name(last_name: str, my_sprav: list[dict[str, str]]=None):
   for item in my_sprav:
       if item["last_name"] == last_name.capitalize():
           print(item)

def copy_line(my_sprav):
    file_path = input("Ведите название файла в который будет скопирован контакт (*.txt) -> ")
    if not os.path.isfile(file_path):
        print(f"Создан файл справочника {file_path}")
        my_file = open(f"{file_path}", "w+", encoding='utf-8')
        my_file.close()
    while True:    
        num_line = int(input("Введите номер строки (первая строка = 1) -> "))
        if num_line != 0 :
            break
    count = 1
    line_copy = ""
    for item in my_sprav:
        if num_line == count:
            for v in item.values():
                line_copy += v + " "
        count += 1
    if len(line_copy) > 0:
        line_copy += "\n"
        my_file = open(f"{file_path}", "a", encoding="utf-8")
        my_file.write(f"{line_copy}")
        my_file.close()
        print(f"Номер  строки {num_line}, скопирован в {file_path} успешно")
    else:
        print(f"Номера строки {num_line} не существует")

def main():
    # переменная = open ('название файла', 'режим работы', encoding='кодировка')
    while True:
        print("Нажмите соотвествующую кнопку для входа в меню:")
        print("1: Вывести данные")
        print("2: Записать новый контакт")
        print("3: Найти контакт по фамилии")
        print("4: Копировать контакт в другой файл по номеру строки")
        print("0: Выйти")

        x = input()
        tel_sprav = read_sprav()
        if x == "1":
            print_sprav(tel_sprav)
        elif x == "2":
            add_contact()
        elif x == "3":
            find_last_name(input("Введите фамилию: "), my_sprav=tel_sprav)
        elif x == "4":
            copy_line(my_sprav=tel_sprav)
        elif x == "0":
            break
        else:
            print("неверная команда")


if __name__ == "__main__":
    main()