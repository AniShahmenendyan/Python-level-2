"""Integer class"""


class Integer:
    def __init__(self, n):
        if type(n) != int:
            raise TypeError ('instances must be int')
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
            return Inf()

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
        return True if self._n != 0 else False




class Inf(int):
    def __init__(self, m = 0):
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
            self.red = r
            self.green = g
            self.blue = b
        else:
            raise ValueError

    @property
    def r(self):
        return self.red

    @property
    def g(self):
        return self.green

    @property
    def b(self):
        return self.blue

    @r.setter
    def r(self, r):
        self.__red = self.color_range(r)
        raise TypeError

    @g.setter
    def g(self, g):
        self.__green = self.color_range()
        raise ValueError

    @b.setter
    def b(self, b):
        self.__blue = self.color_range(b)

    @staticmethod
    def color_range(v):
        return max(0, min(v, 255))

    def __add__(self, other): # սա չի աշխատում
        if type(other) == Colors:
            return Colors(self.r + other.r, self.g + other.g, self.b + other.b)

    def rgb_to_hex(self):
        return '#{:02x}{:02x}{:02x}'.format(self.r, self.g, self.b)

    def __str__(self):
        return f'Red is: {self.red} \nGreen is: {self.green} \nBlue is: {self.blue}'

    # def show_my_color(self):
    #     return color_front(f'This is my color: {self.__red}, {self.__green}, {self.__blue})

clr = Colors(0, 220, 1)
clr2 = Colors(50, 0, 20)

new_clr = clr + clr2
print(new_clr)
print(clr)
# print(clr.rgb_to_hex())
print ('-----------')
print(new_clr)
print('----------------')
