
def ask_data():
    s_name = input('Введите фамилию: ')
    name = input('Введите имя: ')
    m_name = input('Введите отчество: ')
    phone = input('Введите номер телефона: ')

    contact = {'second_name': s_name,
            'first_name': name,
           'midle_name': m_name,
           'phone_number': phone}
    return contact

def add_new_contact():
    
    contact = ask_data()
    with open('phonebook.txt', 'a', encoding='utf-8') as file:
        for value in contact.values():
            file.write(f'{value}; ')
        file.write('\n')
    return True

def open_contact():
    title = ["Фамилия", "Имя", "Отчество", "Телефон"]
    with open('phonebook.txt', 'r', encoding='utf-8') as file:
        print("\t\t".join(title))
        for line in file:
            print("\t\t".join(line.split(';')))

def find_contact():
    title = ["Фамилия", "Имя", "Отчество", "Телефон"]
    s_name = input('Введите Фамилию: ')
    n_line = []
    with open('phonebook.txt', 'r', encoding='utf-8') as file:
        print("\t\t".join(title))
        for counter, line in enumerate(file):
            line = line.split(';')
            if s_name in line[0]:
                n_line.append(counter)
                print("\t\t".join(line))
    return n_line
    
def copy_contact():
    contact = find_contact()
    num = 0
    for i in contact:
        num = num + i
    
    
    file = open('phonebook.txt', 'r', encoding='utf-8')
    clone = open('clone.txt', 'w', encoding='utf-8')
    for i, line in enumerate(file):
        if i == num:
            break
    clone.write(line)
        

def main():
    isStop = None
    
    while isStop !=0:
        print('Выберете действие: \n1 -- ПОИСК\n2 -- ДОБАВИТЬ\n3 -- КОПИРОВАТЬ\n4 -- ОТКРЫТЬ\n0 -- ВЫХОД')
        isStop = int(input('> '))
        if isStop == 1:
            find_contact()
        elif isStop == 2:
            add_new_contact()
        elif isStop == 3:
            copy_contact()
        elif isStop == 4:
            open_contact()
        input('Нажмите enter чтоб продолжить')
        
main()