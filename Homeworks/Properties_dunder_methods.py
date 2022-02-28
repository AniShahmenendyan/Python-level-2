class UnknownAtom(Exception):
    def __init__(self, message='There is no atom type'):
        super().__init__()
        self.message = message

    def __str__(self):
        return self.message


class Atom:
    __atoms = {'C': 'carbon', 'N': 'nitrogen', 'H': 'hydrogen', 'O': 'oxygen', 'P': 'phosphorus'}

    def __init__(self, name):
        if name in self.__atoms.keys():
            self.__name = name
        else:
            raise UnknownAtom

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, val):
        raise ValueError


    def __add__(self, other):
        if type(other) == Atom:
            return Molecule([self.name, other.name])
        else:
            raise UnknownAtom


    def __str__(self):
        return f'Atom: {self.name}'


class Molecule:
    def __init__(self, atoms):
        if type(atoms) != list or len(atoms) <= 1:
            raise TypeError
        else:
            self.atoms = atoms

    def __add__(self, other):
        if type(other) == Atom:
            self.atoms.append(other.name)
            return self
        elif type(other) == Molecule:
            return Molecule(self.atoms + other.atoms)

    def __str__(self):
        return 'Molecule: ' + '-'.join(self.atoms)


atom1 = Atom('H')
atom2 = Atom('H')
atom3 = Atom('O')
print(atom1)
print(atom2)

m = atom1 + atom2
print(m)

m2 = m + atom3
print(m2)

print('____________________')


# Lenght

class Length:
    __conversion = {'m': 1, 'km': 1000, 'yard': 1.094, 'mile': 1609.34}

    def __init__(self, l, u ='m'):
        if type(l) == int or type(l) == float:
            self.unit = u
            self.length = l

    def __add__(self, other):
        if type(other) != Length:
            raise TypeError
        if self.unit == other.unit:
            return Length(self.length + other.length, self.unit)
        else:
            return Length(self.get_meter(self) + Length.get_meter(other))

    @staticmethod
    def get_meter(x):
        return Length.__conversion[x.unit] * x.length

    def __repr__(self):
        return f'{self.length} {self.unit}'

    def __str__(self):
        return f'{Length.get_meter(self)} m'

    def convert(self, unit):
        if unit not in Length.__conversion.keys():
            raise TypeError
        meter = Length.get_meter(self)
        with_unit_lenght = meter / Length.__conversion[unit]
        self.unit = unit
        self.length = with_unit_lenght
        return self




l1 = Length(100)
l2 = Length(200)
print(l1)
print(l1 + l2)
l3 = Length(1, 'mile')
l3.convert('km')
print(repr(l3))
# print(l3 + l1)

"""Player"""

class Song:
    def __init__(self, name, artist, album, year):
        self.name = name
        self.artist = artist
        self.album = album
        self.year = year


    def __str__(self):
        return f'Name: {self.name}\nArtist:{self.artist}\nAlbum: {self.album}\nYear: {self.year}'

class Playlist:

    def __init__(self, songlist = []):
        self.songlist = songlist

    def load_songs(self, filepath):
        with open(filepath, 'r') as file:
            for line in file.readlines():
                artist, album, year, name = line.split('\t')
                self.songlist.append(Song(name, artist, album, year))


    def __len__(self):
        return len(self.songlist)

class Player:
    def __init__(self, playlist, current_index = 0):
        if type(playlist) != Playlist:
            raise  TypeError
        if current_index < 0 or current_index > len(playlist) - 1:
            self.playlist = playlist
            self.is_playing = False
            self.current_index = current_index

    def play(self):
        if self.is_playing == True:
            print('Player is already playing')
        else:
            self.is_playing = True
            print('Start playin')

    def start(self):
        pass


    def stop(self):
        self.is_playing = False
        print('Stop playing')


    def  next(self):
        if self.current_index == len(self.playlist) - 1:
            print('End of playlist')
        else:
            self.current_index += 1
            self.current_song()

    def prev(self):
        pass

    def current_song(self):
        pass


playlist = Playlist()
playlist.load_songs('albums.txt')

print()