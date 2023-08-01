# Возьмите 1-3 задачи из тех, что были на прошлых
# семинарах или в домашних заданиях. Напишите к ним
# классы исключения с выводом подробной информации.
# Поднимайте исключения внутри основного кода. Например
# нельзя создавать прямоугольник со сторонами
# отрицательной длины.

# калькулятор
# исключения: нельзя делить на 0, квадратный корень из отрицательного числа, логарифм отрицательного числа

import math

class CalcError(Exception):
    pass
    
class ZeroDivisionError(CalcError):
    def __str__(self):
        return f'Division by zero is not possible.'

class NegativeValueError(CalcError):
    def __str__(self):
        return f'You entered a negative number. It is impossible to get the square root or logarithm.'


class Calculator:
    def __init__(self):
        pass

    def calc(self):
        
        while True:
            # получаем выбор пользователя
            operation = input("Выберите операцию: +, -, *, /, sin, cos, tan, log, sqrt, quit: ").lower()

            if operation == 'quit':
                # выходим из цикла, если пользователь выбрал quit
                break

            if operation in ['sin', 'cos', 'tan', 'log', 'sqrt']:
                # если пользователь выбрал научную функцию
                num = float(input("Введите число: "))
                result = None

                if operation == 'sin':
                    result = math.sin(num)
                elif operation == 'cos':
                    result = math.cos(num)
                elif operation == 'tan':
                    result = math.tan(num)
                elif operation == 'log':
                    if num < 0:
                        raise NegativeValueError
                    result = math.log(num)
                elif operation == 'sqrt':
                    if num < 0:
                        raise NegativeValueError
                    result = math.sqrt(num)

                print('Результат:', result)


            else:
                # если пользователь выбрал арифметическую операцию
                num1 = float(input("Введите первое число: "))
                num2 = float(input("Введите второе число: "))
                result = None

                if operation == '+':
                    result = num1 + num2
                elif operation == '-':
                    result = num1 - num2
                elif operation == '*':
                    result = num1 * num2
                elif operation == '/':
                    if num2 == 0:
                        raise ZeroDivisionError
                    result = num1 / num2

                print('Результат:', result)

my_calc = Calculator()
my_calc.calc()
