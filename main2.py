# Создайте функцию аналог get для словаря. 
# Помимо самого словаря функция принимает ключ и значение по умолчанию. 
# При обращении к несуществующему ключу функция должна возвращать дефолтное значение. 
# Реализуйте работу через обработку исключений.

def get(my_dict, key, value=None):
    try:
        return my_dict[key]
    except KeyError as e:
        print(f'not in dict, {e}')
        return value


dict1 = {'sobaka': 42}
print(get(dict1, 'sobaka', 1))