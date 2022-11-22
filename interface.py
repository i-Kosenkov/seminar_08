import model


def view_data(data):
    print(data)


def get_menu_value():
    print('''Выберите пункт меню:
    1 - Просмотреть базу данных
    2 - Добавить новую запись
    3 - Удалить запись
    x - выход
    ''')
    return input('->: ').lower()
