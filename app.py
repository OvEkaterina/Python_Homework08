# Создать телефонный справочник с возможностью импорта и экспорта данных в формате .txt.
# Фамилия, имя, отчество, номер телефона - данные, которые должны находиться в файле.
# Программа должна выводить данные
# Программа должна сохранять данные в текстовом файле
# Пользователь может ввести одну из характеристик для поиска определенной 
# записи(Например имя или фамилию человека)
# Использование функций. Ваша программа не должна быть линейной




def show_book()-> str:
    with open ('data.txt','r',encoding='utf-8') as file :
        book = file.read()
    return book
def input_data()-> str:
    with open ('data.txt','a',encoding='utf-8') as file :
        file.write( f'{input("Введите данные нового абонента : ")  }\n')
def search_data(book, searching_data):
    with open ('data.txt','r',encoding='utf-8') as file :
        book = file.read().split('\n')
        search_book = list()
    for el in book:
        if searching_data in el:
           search_book.append(el)
    if len(search_book) == 0 :
            return("Абонент не найден")
    return('\n'.join(str(value) for value in search_book))
def del_contact():
    with open('data.txt', 'r', encoding='utf-8') as file:
        book = file.read().split('\n')
        find = input('Введите данные абонента который хотите удалить: ')
        index = 0
        temp = list()
        for i in book:
            if find.lower() in i.lower():
                print(f'Ведитете "{index}" чтобы удалить абонента "{i}"')
                temp.append(i)
            index +=1
        if bool(temp):
            del_index = int(input(""))
            book.pop(del_index)    
            with open('data.txt', 'w', encoding='utf-8') as file:
                for i in book:
                    file.writelines(f'{str(i)}\n')
        else:
            print('Нет такого контакта!')   
def edit_data():
    with open('data.txt', 'r', encoding='utf-8') as file:
        book = file.read().split('\n')
        find = input('Введите данные абонента который хотите изменить: ')
        index = 0
        temp = list()
        for i in book:
            if find.lower() in i.lower():
                print(f'Ведитете "{index}" чтобы изменить абонента "{i}"')
                temp.append(i)
            index +=1
        if bool(temp):
            del_index = int(input(""))
            book.pop(del_index)    
            with open('data.txt', 'w', encoding='utf-8') as file:
                for i in book:
                    file.writelines(f'{str(i)}\n')
        else:
            print('Нет такого абонента!')   
    with open ('data.txt','a',encoding='utf-8') as file :
        file.write( f'{input("Введите данные нового абонента : ")  }\n')


print('Режимы работы\n 1 - Запись нового абонента \n 2 - Поиск абонента \n 3 - Показать справочник  \n 4 - Удалить контакт из справочника \n 5 - Изменить контакт из справочника \n 0 - Выход' )

while True:
    mode = input('Выбор режима работы: ')
    if mode == '1' :
         input_data()   
    elif mode == '2':
        print(search_data(show_book(),input('Введите данные для поиска: ')))
    elif mode == '3':
        print(show_book())
    elif mode == '4':
        del_contact()
    elif mode == '5':
        edit_data()
    elif mode == '0':
        break
    else:
        print('Неверное значение')
