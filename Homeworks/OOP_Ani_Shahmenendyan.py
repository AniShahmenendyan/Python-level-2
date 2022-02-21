import abc
import math
'''Animal'''


class Animal:
    def __init__(self, name, age, color):
        self._name = name
        self._age = age
        self._color = color

    @staticmethod
    def make_noise():
        print('Animal is making noise')

    def walk(self):
        print('Animal is walking')

    def fly(self):
        print('Animal is flying')


class Bird(Animal):
    def __init__(self, name, age, color, can_fly=True):
        super().__init__(name, age, color)
        self._can_fly = can_fly


    def walk(self):
        print('The bird only wants to fly as it is too lazy to walk')

    def fly(self):
        super().fly()


class Feline(Animal):
    def __init__(self, name, age, color, can_fly=False):
        super().__init__(name, age, color)
        self._can_fly = can_fly



    def walk(self):
        super().walk()

    def fly(self):
        print("it can't fly")


dog = Feline('Roy', 10, 'black')
print(dog._name)
dog.fly()
print()
eagle = Bird('Eagle', 3, 'white&black')
print(eagle._name)
eagle.walk()
print('--------------------')

"""Calculator"""


class Calculator:

    def __init__(self, a, b):
        if (type(a) == int or type(a) == float) and (type(b) == int or type(b) == float):
            self._a = a
            self._b = b

        else:
            raise TypeError ('must be an integer or float')

    def add(self):
        return self._a + self._b

    def sub(self):
        return self._a - self._b

    def mult(self):
        return self._a * self._b

    def div(self):
        if self._b != 0:
            return self._a / self._b
        else:
            raise ZeroDivisionError


res = Calculator(10, 5)
res.div()
print(f'Div = {res.div()}')
print('-------------')

"""Shape"""


class Shape():

    def perimetr(self):
        pass


    def area(self):
        pass


class Circle(Shape):

    def __init__(self, radius):
        self._radius = radius

    def area(self):
        return self._radius ** 2 * math.pi

    def perimetr(self):
        return 2 * math.pi * self._radius


class Rectangle(Shape):

    def __init__(self, a, b):
        self._a = a
        self._b = b

    def perimeter(self):
        super().perimetr()
        return 2 * (self._a + self._b)

    def area(self):
        super().area()
        return self._a * self._b


class Triangle(Shape):

    def __init__(self, a, b, c):
        if a + b < c and b + c < a and c + a < b:
            self._a = a
            self._b = b
            self._c = c
        else:
            raise TypeError

    def perimeter(self):
        return self._a + self._b + self._c

    # @staticmethod
    # def check_triangle(a,b,c):
    #     if a + b < c and b + c < a and c + a < b:
    #         return True
    #     else:
    #         return False

    def area(self):
        s = (self._a + self._b + self._c) / 2
        return s * (s - self._a) * (s - self._b) * (s - self._c) ** 0.5


# right_triangle = Triangle(3, 4, 5)
# p = right_triangle.perimeter()
# print(f'Perimeter of triangle = {p}')
# s = right_triangle.area()
# print(f'Area of shape = {s}')
# print('---------------------')

# """Vehicle"""
#
# class Vehicle():
#     def __int__(self,name, mileage = 0, condition, price, max_speed, current_speed, engine_on = False):
#         self._name = name
#         self._mileage = mileage
#         self._condition = condition
#         self._price = price
#         self._max_speed = max_speed
#         self._current_speed = current_speed
#         self._engine_on = engine_on
#
#     def start_engine(self):
#         if self._engine_on is False:
#             self._engine_on = True
#             print('The car is on')
#         else:
#             self._engine_on = False
#             self._current_speed = 0
#             print('The car is stop')
#     def accelerate(self, a):
#         self._a = a
#         if self._max_speed < self._current_speed + a:
#             self._current_speed += a
#
#
#     def stop(self, a):
#         if self._current_speed > 0:
#             self._current_speed -= a
#         if self._current_speed == 0:
#             self._engine_on = False
#
# class ElectricVehicle(Vehicle):
#
#     def __init__(self, name, mileage, condition, price, max_speed, current_speed, engine_on, driving_range, charging_time):
#         super().__init__(name, mileage, condition, price, max_speed, current_speed, engine_on)
#         self._driving_range = driving_range
#         self._charging_time = charging_time
#
#     def start_engine(self):
#         super().start_engine()
#
#     def accelerate(self, a):
#         super().accelerate(a)
#
#     def stop(self, a):
#         super().stop(a)
#
#
# class PetrolVehicle(Vehicle):
#
#     def __init__(self, name, mileage, condition, price, max_speed, current_speed, engine_on, transmission, num_of_gears,current_gear=0):
#         super().__init__(name, mileage, condition, price, max_speed, current_speed, engine_on)
#         self._transmission = transmission
#         self._num_of_gears = num_of_gears
#         self._current_gear = current_gear
#
#     def start_engine(self):
#         super().start_engine()
#
#     def accelerate(self, a):
#         super().accelerate(a)
#
#     def stop(self, a):
#         super().stop(a)
#
#
#
#
#
