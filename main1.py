# Создайте функцию, которая запрашивает числовые данные от
# пользователя до тех пор, пока он не введёт целое или
# вещественное число.
# Обрабатывайте не числовые данные как исключения.

def get():
    while True:
        num = input('введите число: ')
        try:
            num = float(num)
            break
        except ValueError as e:
            print(f'вы ввели не корректные данные: {e}')
    try:
        num = int(num)
    except ValueError as e:
        print(f'вы ввели не целое число: {e}')

    
    
get()

