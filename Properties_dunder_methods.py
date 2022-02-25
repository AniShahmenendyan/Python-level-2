class Atom:
    mlc = ['C_carbon', 'N_nitrogen', 'H_hydrogen', 'O_oxygen', 'P_phosphorus']

    def __init__(self, name):
        if name in mlc:
            self.name = name

    def __add__(self, other):
        if check_molecule(mlc, [self, other]):
            return Molecule([self, other])
        raise UnknownAtom('New object must be ')

    @staticmethod
    def check_molecule(l, vol):
        for i in range(len(l)):
            if l[i] == vol:
                return True
        return False


class Molecule:
    def __init__(self, atoms):
        if type(atoms) is list:
            self.atoms = atoms

    def __add__(self, other):
        if tyoe(other) == Atom:
            return Molecule()


# PLenght

class Lenght:
    main_unit = 'm'
    units = {'m': 1, 'km': 1000, 'yard': 1.094, 'mile': 1609.34}

    def __init__(self, u, l):
        if type(l) == int or type(l) == float:
            self.unit = u
            self.lenght = l

    def u_get(self):
        return self.unit

    def l_get(self):
        return self.lenght

    def u_set(self):
        self.unit = u

    def l_set(self):
        self.lenght = l

    def __add__(self, other):
        chek_unit(self.unit)
        chek_unit(other.u_get())
        return Lenght(self.lenght + other.u_get(), self.unit)

    @staticmethod
    def chek_unit(vol):
        units = {'m': 1, 'km': 1000, 'yard': 1.094, 'mile': 1609.34}
        for k, v in units:
            if vol == v:
                vol = k * vol

        return vol
