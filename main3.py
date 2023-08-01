# Создайте класс с базовым исключением и дочерние классы-исключения: 
# ошибка уровня, 
# ошибка доступа.

# Вспоминаем задачу из семинара 8 про сериализацию данных, где в бесконечном цикле запрашивали имя, личный 
# идентификатор и уровень доступа (от 1 до 7) сохраняя информацию в JSON файл. 
# Напишите класс пользователя, который хранит эти данные в свойствах экземпляра. 
# Отдельно напишите функцию, которая считывает информацию из JSON файла и формирует множество пользователей.


import json

class UserError(Exception):
    pass


class UserLvlError(UserError):
    pass


class UserAccessError(UserError):
    pass


class User:
    def __init__(self, name, id, lvl):
        self.name = name
        self.id = id
        self.lvl = lvl

    def __str__(self):
        return f'{self.name} {self.id} {self.lvl}'

    def __repr__(self):
        return f'User({self.name}, {self.id}, {self.lvl})'


def coder(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        data = json.load(file)

    set_user = set()
    for lvl, value in data.items():
        for id, name in value.items():
            set_user.add(User(name, id, lvl))

    return set_user


print(coder('data.json'))

for el in coder('data.json'):
    print(el.__repr__())