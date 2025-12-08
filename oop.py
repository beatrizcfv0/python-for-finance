# 05/12/2025
# Página 166

class FinancialInstrument(object):
    author = 'Nikolas Tesla'
    def __init__(self, symbol, price):
        self.symbol = symbol
        self.__price = price # Private instance attributes

    def get_price(self):
        return self.__price
    def set_price(self, price):
        self.__price = price
        

class Stock(FinancialInstrument):
    def get_price(self):
        return self.__price
    def set_price(self, price):
        self.__price = price

#########################

class Vector(object):
    def __init__(self, x = 0, y = 0, z = 0):
        self.x = x
        self.y = y
        self.z = z
    def __repr__(self): # allows the definition of custom strings representation
        return 'Vector(%r, %r, %r)' % (self.x, self.y, self.z)
    
    def __abs__(self):
        return (self.x ** 2 + self.y ** 2 + self.z ** 2) ** 0.5
    
    def __bool__(self):
        return bool(abs(self))
    
    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        z = self.z + other.z
        return Vector(x, y, z)
 
    def __mul__(self, scalar):
        return Vector(self.x * scalar,
        self.y * scalar,
        self.z * scalar)
    
    def __len__(self):
        return 3

    def __getitem__(self, i):
        if i in [0, -3]: return self.x
        elif i in [1, -2]: return self.y
        elif i in [2, -1]: return self.z
        else: raise IndexError('Index out of range.')

    def __iter__(self):
        for i in range(len(self)):
            yield self[i]
