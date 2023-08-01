# Возьмите 1-3 задачи из тех, что были на прошлых
# семинарах или в домашних заданиях. Напишите к ним
# классы исключения с выводом подробной информации.
# Поднимайте исключения внутри основного кода. 

# нельзя создавать прямоугольник со сторонами
# отрицательной длины.

class CalcError(Exception):
    pass

class NegativeValueError(CalcError):
    def __str__(self):
        return f'Вы ввели отрицательное значение. Невозможно получить прямоугольник с сторонами отрицательной длины.'


class Rectangle:
    def __init__(self, length, width=None):
        if not width:
            self.width = length
        else:
            self.width = width
        self.length = length
        if self.width < 0 or self.length < 0:
            raise NegativeValueError

    def get_perimetr(self):
        return 2 * self.length + 2 * self.width

    def get_area(self):
        return self.length * self.width

    def __add__(self, other):
        width = self.width
        perimetr = self.get_perimetr() + other.get_perimetr()
        length = (perimetr - 2 * width) / 2
        return Rectangle(width, length)

    def __sub__(self, other):
        # width = min(self.width, self.length, other.width, other.length)
        perimetr = abs(self.get_perimetr() - other.get_perimetr())
        length = int(perimetr / 4)
        width = perimetr / 2
        return Rectangle(length, width)

    


rect1 = Rectangle(30, -5)
rect2 = Rectangle(26, 6)
rect3 = rect1 - rect2
print(rect3.get_perimetr())
print(rect3.length)
print(rect3.width)