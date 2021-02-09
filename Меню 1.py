import mymodule
def menu():
    print('\n1.Создать')
    print('2.Контакты')
    print('3.Найти')
    print('4.Редактировать')
    print('5.Удалить')
    print('6.Выйти')

    selection = int(input('\nВыберите номер '))

    if selection == 1:
        print('Раздела не существует')
    elif selection == 2:
        print('Раздела не существует')
    elif selection == 3:
        print('Раздела не существует')
    elif selection == 4:
        print('Раздела не существует')
    elif selection == 5:
        print('Раздела не существует')
    elif selection == 6:
        mymodule.Exit()
    else:
        print('Раздела не существует')

    menu()
    selection = int(input("Choose: "))

menu()
