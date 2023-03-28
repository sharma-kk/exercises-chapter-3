from numbers import Number
from numbers import Integral


class Polynomial:

    def __init__(self, coefs):
        self.coefficients = coefs

    def degree(self):
        return len(self.coefficients) - 1

    def __str__(self):
        coefs = self.coefficients
        terms = []

        if coefs[0]:
            terms.append(str(coefs[0]))
        if self.degree() and coefs[1]:
            terms.append(f"{'' if coefs[1] == 1 else coefs[1]}x")

        terms += [f"{'' if c == 1 else c}x^{d}"
                  for d, c in enumerate(coefs[2:], start=2) if c]

        return " + ".join(reversed(terms)) or "0"

    def __repr__(self):
        return self.__class__.__name__ + "(" + repr(self.coefficients) + ")"

    def __eq__(self, other):

        return isinstance(other, Polynomial) and\
             self.coefficients == other.coefficients

    def __add__(self, other):

        if isinstance(other, Polynomial):
            common = min(self.degree(), other.degree()) + 1
            coefs = tuple(a + b for a, b in zip(self.coefficients,
                                                other.coefficients))
            coefs += self.coefficients[common:] + other.coefficients[common:]

            return Polynomial(coefs)

        elif isinstance(other, Number):
            return Polynomial((self.coefficients[0] + other,)
                              + self.coefficients[1:])

        else:
            return NotImplemented

    def __radd__(self, other):
        return self + other

    def __sub__(self, other):

        if isinstance(other, Polynomial):
            coefs = tuple(-a for a in other.coefficients)
            return self + Polynomial(coefs)

        elif isinstance(other, Number):
            return Polynomial((self.coefficients[0] - other,)
                              + self.coefficients[1:])

        else:
            return NotImplemented

    def __rsub__(self, other):
        coefs = tuple(-a for a in self.coefficients)
        return other + Polynomial(coefs)
    

    def __mul__(self, other):
        
        mul = []
        if isinstance(other, Number):
            for i in self.coefficients:
                mul.append(other*i)
            return Polynomial(tuple(mul))
        
        if isinstance(other, Polynomial):
            Pol = Polynomial((0,))
            for i, j in enumerate(other.coefficients):
                Pol+= Polynomial(i*(0,) + self.coefficients)*j
            return Pol 

    def __rmul__(self, other):
        return self*other    
    
    def __pow__(self, other):
         
        expo = Polynomial((1,))

        if isinstance(other, Integral):
            for i in range(other):
                expo *= self
            return expo
        else: 
            return NotImplemented

    def __call__(self, other):
        fval = 0
        if isinstance(other, Number):
            for i, j in enumerate(self.coefficients):
                fval += j*other**i
            return fval
        else:
            return NotImplemented
        
    def dx(self):

        if self.degree() == 0:
            return Polynomial((0,))
        else:
             deriv = []
             ncoef = self.coefficients[1:]

             for i, j in enumerate(ncoef, start=1):
                 deriv.append(i*j)
             return Polynomial(tuple(deriv))

def derivative(poly):
    
    return poly.dx()
