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
        if type(other) == Integer:
            return Integer(self._n + other.get_n())


    def __sub__(self, other):
        if type(other) == Integer:
            return Integer(self._n - other.get_n())


    def __mul__(self, other):
        if type(other) == Integer:
            return Integer(self._n * other.get_n())


    def __truediv__(self, other):
        if type(other) == Integer and other.get_n() != 0:
            return self._n / other.get_n()
        else:
            return Inf

    def __eq__(self, other):
        return self._n == other._n

    def __ne__(self, other):
        return not self == other

    def __lt__(self, other):
        return self._n < other._n

    def __le__(self, other):
        return self._n <= other._n

    def __gt__(self, other):
        return self._n > other._n

    def __ge__(self, other):
        return self._n >= other._n

    def __str__(self):
        return f'{self._n}'

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
print(a * b)
print(a / b)
print(a == b)
print(a < b)
print(a <= b)
print(a > b)
print(a >= b)
print(bool(a))
print('------------------')

class Colors:
    def __init__(self, r, g, b):
        if r in range(256) and g in range(256) and b in range(256):
            self.__red = r
            self.__green = g
            self.__blue = b
        else:
            raise ValueError

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
        if  type(r) == Colors and r in range(0, 256):
            self.__red = r
        raise TypeError

    @g.setter
    def g(self, g):
        if type(g) == Colors and g in range(0, 256):
            self.__green = g
        raise TypeError

    @b.setter
    def b(self, b):
        if type(b) == Colors and b in range(0, 256):
            self.__blue = b
        raise TypeError

    # def __add__(self, other): # սա չի աշխատում
    #     if type(other) == Colors:
    #         return Colors(self.__red + other.r(), self.__green + other.g(), self.__blue + other.b())

    def rgb_to_hex(self):
        return f'Red is:{hex(self.__red)},Green is: {hex(self.__green)},Blue is: {self.__blue}'

    def __str__(self):
        return f'Red is: {self.__red} \nGreen is: {self.__green} \nBlue is: {self.__blue}'

    # def show_my_color(self):
    #     return color_front(f'This is my color: {self.__red}, {self.__green}, {self.__blue})

clr = Colors(0, 220, 1)
clr2 = Colors(50,0,20)

# new_clr = Colors(clr + clr2)

print(clr)
print ('-----------')
# print(new_clr)
print('----------------')
