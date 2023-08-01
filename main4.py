# Доработаем задачи 3 и 4. Создайте класс проекта, который имеет следующие методы: 
# загрузка данных (функция из задания 4)
# вход в систему - требует указать имя и id пользователя. Для проверки наличия пользователя в множестве 
# используйте магический метод проверки на равенство пользователей. Если такого пользователя нет, вызывайте исключение доступа. 
# А если пользователь есть, получите его уровень из множества пользователей.
# добавление пользователя. Если уровень пользователя меньше, чем ваш уровень, вызывайте исключение уровня доступа.

import json

class UserError(Exception):
    pass


class UserLvlError(UserError):
    def __str__(self):
        return 'Wrong level'


class UserAccessError(UserError):
    def __str__(self):
        return 'Wrong password or login'


class User:
    def __init__(self, name, id, lvl):
        self.name = name
        self.id = id
        self.lvl = lvl

    def __str__(self):
        return f'{self.name} {self.id} {self.lvl}'

    def __repr__(self):
        return f'User({self.name}, {self.id}, {self.lvl})'

    def __eq__(self, other):
        return self.id == other.id and self.name == other.name

    def __hash__(self):
        return hash((self.name, self.id))
    
class SignIn:
    def __init__(self):
        self.tmp_user = None
        self.set_user = set()

    def coder(self, filename):
        with open(filename, 'r', encoding='utf-8') as file:
            data = json.load(file)
        for lvl, value in data.items():
            for id, name in value.items():
                self.set_user.add(User(name, id, lvl))

        return self.set_user

    def sign_in(self, my_name, my_id):
        new_user = User(my_name, my_id, 0)
        if new_user not in self.set_user:
            raise UserAccessError
        else:
            for user in self.set_user:
                if new_user == user:
                    self.tmp_user = user
                    return self.tmp_user

    def add(self, name, id, lvl):
        if self.tmp_user.lvl > lvl:
            raise UserLvlError
        else:
            new_user = User(name, id, lvl)
            self.set_user.add(new_user)
        return new_user

    def show(self):
        return self.set_user


sign_in1 = SignIn()
sign_in1.coder('data.json')
print(sign_in1.sign_in('a', '01'))
print(sign_in1.add('tumen', 'djf', '2'))
print(sign_in1.show())
print(sign_in1.sign_in('lk', '07'))
# print(sign_in1.add('lk', '07', '10'))

