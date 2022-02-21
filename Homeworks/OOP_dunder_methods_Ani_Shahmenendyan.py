"""Integer class"""


class Integer:
    def __init__(self, n):
        if type(n) == int:
            self._n = n

    def get_n(self):
        return self._n

    def set_n(self, n):
        if type(n) == int:
            return self._n

    def __add__(self, other):
        return Integer(self._n + other.get_n())

    def __sub__(self, other):
        return Integer(self._n - other.get_n())

    def __mul__(self, other):
        return Integer(self._n * other.get_n())

    def __truediv__(self, other):
        if other.get_n != 0:
            return Integer(self._n / other.get_n())
        return Inf(self._n / other.get_n())

    def __eq__(self, other):
        return self._n == other.get_n()

    def __ne__(self, other):
        return not self == other

    def __lt__(self, other):
        return self._n < other.get_n()

    def __le__(self, other):
        return self._n <= other.get_n()

    def __gt__(self, other):
        return self._n > other.get_n()

    def __ge__(self, other):
        return self._n >= other.get_n()

    # def __str__(self):
    #     return f'{self._n}'

    def __bool__(self):
        if self._n != 0:
            return True
        else:
            return False


class Inf(int):
    def __init__(self, m):
        super().__init__(m)


a = Integer(10)
b = Integer(2)

print(a + b)
print(a - b)
# print(a * b)
# print(a / b)
# print(a == b)
# print(a < b)
# print(a <= b)
# print(a > b)
# print(a >= b)
print(bool(a))
print('------------------')


class Colors:
    def __init__(self, r, g, b):
        self.__red = r
        self.__green = g
        self.__blue = b

    @property
    def r(self):
        return self.__red

    @property
    def g(self):
        return self.__green

    @property
    def b(self):
        return self.__blue

    @r.setter
    def r(self, r):
        if r in range(0, 256):
            self.__red = r
        else:
            raise ValueError

    @g.setter
    def g(self, g):
        if g in range(0, 256):
            self.__green = g
        else:
            raise ValueError

    @b.setter
    def b(self, b):
        if b in range(0, 256):
            self.__blue = b
        else:
            raise ValueError

    def __add__(self, other):
        return Colors(self.__red + other.r(), self.__green + other.g(), self.__blue + other.b())

    def rgb_to_hex(self):
        return f'Red is:{hex(self.__red)},Green is: {hex(self.__green)},Blue is: {self.__blue}'

    def __str__(self):
        return f'Red is: {self.__red} \nBlue is: {self.__blue} \nGreen is: {self.__green}'


clr = Colors(0, 260, 1)
new_clr = Colors(20, -50, 200)

print(clr)
# print(clr + new_clr) #  սա չի աշխատում
print('----------------')
