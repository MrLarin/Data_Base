from push_data import *
from read_data import *
from print_data import *
from search_data import *


def greeting():
    print("Сотрудники компании")

def start():
    print("Доступные операции:\n\
    1 - получить всю информацию о сотрудниках;\n\
    2 - добавить сотрудника;\n\
    3 - поиск сотрудника;\n\
    4 - выход.")
    ch = input("Введите цифру: ")
    while True:
        if ch == '1':
            data = read_data()
            print_data(data)
            start()
        elif ch == '2':
            push_data()
            start()
        elif ch == '3':
            info = input("Введите данные для поиска: ")
            data = read_data()
            item = search_data(info, data)
            if item != None:
                print_data(item, True)
            else:
                print("Данные не обнаружены")                
            start()
        else: 
            if not ch=='4':
                print("Введите корректную цифру!")
                start()
            
        if ch == '4':
            print("Спасибо, до свидания!")
        break
        