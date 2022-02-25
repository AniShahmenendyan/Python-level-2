class UnknownAtom(Exception):
    def __init__(self, message='There is no atom type'):
        self.message = message

    def __str__(self):
        return self.message


class Atom:
    mlc = {'C': 'carbon', 'N': 'nitrogen', 'H': 'hydrogen', 'O': 'oxygen', 'P': 'phosphorus'}

    def __init__(self, name):
        if name in self.mlc.keys():
            self.name = name
        else:
            raise UnknownAtom

    def __add__(self, other):
        if type(other) == Atom:
            return Molecule([self.name, other.name])

    def __str__(self):
        return f'Atom: {self.name}'


class Molecule:
    def __init__(self, atoms):
        if type(atoms) is list:
            self.atoms = atoms

    def __add__(self, other):
        if type(other) == Atom:
            self.atoms.append(other.name)
            return self

    def __str__(self):
        return 'Molecule: ' + '-'.join(self.atoms)


# atom1 = Atom('H')
# atom2 = Atom('H')
# atom3 = Atom('O')
# print(atom1)
# print(atom2)
#
# m = atom1 + atom2
# print(m)
#
# m2 = m + atom3
# print(m2)


# PLenght

class Length:
    units = {'m': 1, 'km': 1000, 'yard': 1.094, 'mile': 1609.34}

    def __init__(self, l, u='m'):
        if type(l) == int or type(l) == float:
            self.unit = u
            self.length = l

    def __add__(self, other):
        if type(other) != Length:
            raise TypeError
        if self.unit == other.unit:
            return Length(self.length + other.length, self.unit)
        else:
            return Length(self.length * Length.units[self.unit] + other.length * Length.units[other.unit])

    def __str__(self):
        return f'{self.length} {self.unit}'


l1 = Length(100)
l2 = Length(200)
print(l1)
print(l1 + l2)
l3 = Length(10, 'km')
print(l3)
print(l3 + l1)
