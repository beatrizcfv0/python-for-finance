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
        

class FinancialInstrument(FinancialInstrument):
    def get_price(self):
        return self.price
    def set_prince(self, price):
        self.price = price

#########################

class Vector(object):
    def __init__(self, x = 0, y = 0, z = 0):
        self.x = x
        self.y = y
        self.z = z


class Vector(Vector):
    def __repr__(self): # allows the definition of custom strings representation
        return 'Vector(%r, %r, %r)' % (self.x, self.y, self.z)
    
    def __abs__(self):
        return (self.x ** 2 + self.y ** 2)

v = Vector(2, 2, 3)
print(v)