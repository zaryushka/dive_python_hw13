# простой пример с исключениями для тренировки



while True:

    user_input = input("Введите число: ")
    try:
        number = float(user_input)

        if number < 0:
            raise ValueError("Число не может быть отрицательным")
        elif not number.is_integer():
            raise ValueError("Число должно быть целым")
    except ValueError as e:
        print("Вы ввели не корректное значение:", e)
    print(user_input)

