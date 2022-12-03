# модуль экспорта данных 

def read_data():
    lst_name = []
    with open('name.csv', 'r') as file:
        for line in file:
            temp = line.strip().split(';')
            lst_name.append(temp)
        print(lst_name)
    lst_adress = []
    with open('adress.csv', 'r') as file:
        for line in file:
            temp = line.strip().split(';')
            lst_adress.append(temp)
        print(lst_adress)

    lst_employees = []
    with open('employees.csv', 'r') as file:
        for line in file:
            temp = line.strip().split(';')
            lst_employees.append(temp)
        print(lst_employees)

    lst_tel = []
    with open('tel.csv', 'r') as file:
        for line in file:
            temp = line.strip().split(';')
            lst_tel.append(temp)
        print(lst_tel)


    lst = []
    for i in range(len(lst_name)):
        lst.append( [lst_name[i][0], lst_name[i][1], lst_name[i][2], lst_name[i][3], lst_name[i][4], \
                    lst_employees[i][0], lst_employees[i][1], lst_employees[i][2], lst_employees[i][3], \
                    lst_adress[i][0], lst_adress[i][1], lst_adress[i][2], lst_adress[i][3], lst_adress[i][4], \
                    lst_adress[i][5], lst_adress[i][6], lst_adress[i][7], lst_adress[i][8], lst_adress[i][9], \
                    lst_tel[i][0], lst_tel[i][1], lst_tel[i][2], lst_tel[i][3], lst_tel[i][4], lst_tel[i][5]]   )   
    return lst

    