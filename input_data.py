from write_data import count_data

def input_data():
    dct = dict()
    Id = count_data("name.csv") 
    dct["id"] = Id     
    dct["surname"] = input('Введите Фамилию: ')
    dct["name"] = input('Введите Имя: ')
    dct["patronymic"] = input('Введите Отчество: ')
    dct["date_of_birth"] = input('Введите дату рождения: ')
    dct["department"] = input('Введите подразделение: ')
    dct["profession"] = input('Введите должность: ')
    dct["education"] = input('Введите образование: ')
    dct["status"] = input('Введите работает/не работает сотрудник в настоящее время: ')
    dct["tel_number1"] = input('Введите номер телефона1: ')
    dct["commentary1"] = input('Введите комментарий: ')
    dct["tel_number2"] = input('Введите номер телефона2: ')
    dct["commentary2"] = input('Введите комментарий: ')
    dct["tel_number3"] = input('Введите номер телефона3: ')
    dct["commentary3"] = input('Введите комментарий: ')
    dct["reg_city"] = input('Введите адрес по прописке Город: ')
    dct["reg_street"] = input('Введите адрес по прописке Улица: ')
    dct["reg_house"] = input('Введите адрес по прописке Дом: ')
    dct["reg_apartament"] = input('Введите адрес по прописке Квартира: ')
    dct["reg_other"] = input('Введите адрес по прописке Примечание: ')
    dct["actual_city"] = input('Введите адрес фактического проживания Город: ')
    dct["actual_street"] = input('Введите адрес фактического проживания Улица: ')
    dct["actual_house"] = input('Введите адрес фактического проживания Дом: ')
    dct["actual_apartament"] = input('Введите адрес фактического проживания Квартира: ')
    dct["actual_other"] = input('Введите адрес фактического проживания Примечание: ')   
    return dct





