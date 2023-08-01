# Возьмите 1-3 задачи из тех, что были на прошлых
# семинарах или в домашних заданиях. Напишите к ним
# классы исключения с выводом подробной информации.
# Поднимайте исключения внутри основного кода. 

# задача с банкоматом

def bancomat():
    balance = 0
    operation = 0
    list_operations = []

    while True:
        print('1. Пополнить')
        print('2. Снять')
        print('3. Показать историю операций')
        print('4. Выйти')
        choice = input('Выберите действие (1-4): ')

        try:
            choice = int(choice)
            if choice == 1:
                amount = int(input('Введите сумму пополнения: '))
                if amount <= 0:
                    raise ValueError('Сумма пополнения должна быть положительным числом.')
                if amount % 50 != 0:
                    raise ValueError('Сумма пополнения должна быть кратна 50 у.е.')
                balance += amount
                operation += 1
                if operation % 3 == 0:
                    bonus = balance * 0.03
                    balance += bonus
                if balance > 500000:
                    nalog = balance * 0.1
                    balance -= nalog
                list_operations.append(f'Пополнение: {round(amount, 2)}')
            elif choice == 2:
                amount = int(input('Введите сумму снятия: '))
                if amount <= 0:
                    raise ValueError('Сумма снятия должна быть положительным числом.')
                if amount % 50 != 0:
                    raise ValueError('Сумма снятия должна быть кратна 50 у.е.')
                if amount > balance:
                    raise ValueError('Недостаточно средств.')
                balance -= amount
                operation += 1
                gaz = amount * 0.015
                gaz = min(max(gaz, 30), 600)
                balance -= gaz
                if operation % 3 == 0:
                    bonus = balance * 0.03
                    balance += bonus
                if balance > 500000:
                    nalog = balance * 0.1
                    balance -= nalog
                list_operations.append(f'Снятие: {round(amount, 2)}')
            elif choice == 3:
                print(list_operations)
            elif choice == 4:
                break
            else:
                print('Выберите действие из предложенных вариантов.')

            print(f'Баланс: {round(balance, 2)} у.е.')
        except ValueError as e:
            print(f'Ошибка: {e}. Попробуйте снова.')

bancomat()
