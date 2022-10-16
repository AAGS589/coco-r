from enum import Enum
from dataclasses import dataclass


#-------- clases usadas

class Element:
    def __init__(self, ident, value):
        self.ident = ident
        self.value = value

    def __repr__(self):
        return f'{self.ident} = {self.value}'

class Character(Element):
    def __init__(self, ident, value):
        super().__init__(ident, value)

class Keyword(Element):
    def __init__(self, ident, value):
        super().__init__(ident, value)        


class Token(Element):
    def __init__(self, ident, value, context=None):
        super().__init__(ident,value)
        self.context = context

    def __repr__(self):
        if self.context != None:
            return f'{self.ident} = {self.value} {self.context}'
        return f'{self.ident} = {self.value}' 


# ------------------ Los diferentes symbolos que podrá recibir

class VarType(Enum):
    ident = 0
    string = 0
    char = 0
    number = 0
    union = 0
    difference = 0
    range = 0
    append = 0
    lkleene = 0
    rkleene = 0
    lpar = 0
    rpar = 0
    lbracket = 0       
    rbracket = 0
    OR = 0

@dataclass
class Variable:
    type: VarType
    value: any = None
    ident: str = None

    def __repr__(self):
        if self.name:
            return f'{self.type.name}: {self.name}'
        return self.type.name + (f'{self.value}' if self.value != None else '')

#------------------ Tipos de nodos ----------
class Kleene:
    def __init__(self, a):
        self.a = a

    def __repr__(self):
        return '{ ' + f'{self.a}' + '}'   


class Bracket:
    def __init__(self, a):
        self.a = a

    def __repr__(self):
        return f'[ {self.a} ]'

class Or:
    def __init__(self, a ,b):
        self.a = a
        self.b = b

    def __repr__(self):
        return f'({self.a} | {self.b})'

class append:
    def __init__(self, a , b):
        self.a = a
        self.b = b

    def __repr__(self):
        return f'{self.a} . {self.b}'

class Symbol:
    def __init__(self, value, type_=None, ident_name = None):
        self.value = value
        self.type = type_         
        self.ident_name = ident_name

    def __repr__(self):
        if self.ident_name:
            return f'{self.ident_name}'
        return f'{self.value}'                          