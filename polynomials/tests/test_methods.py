from fractions import Fraction

from polynomials.polynomial import Polynomial
from polynomials.buchberger import buchberger
from polynomials.ideal_membership import ideal_membership
from polynomials.poly_methods import *

"""Testing just to check whether I get the expected results on a few examples,
not actually asserting robust correct behavior or checking for edge cases.

Remember to run pytest with the -s flag to view print statements."""

Poly0 = Polynomial({})
Poly1 = Polynomial({(1, 2, 3):Fraction(-5, 1), (3, 1, 5): Fraction(-7, 8)})
Poly2 = Polynomial({(1, 2, 3):Fraction(5, 1), (2, 1, 1):Fraction(1, 1)})
Poly3 = Polynomial({(2, 2, 7): Fraction(5, 1)})
Poly4 = Polynomial({(1, 1, 0):1, (0, 3, 0): 2, (0, 0, 0): -1})
Poly5 = Polynomial({(2, 0, 0):1, (1, 2, 0): 2})
Poly6 = Polynomial({(0, 0, 0): Fraction(1, 2), (0, 3, 0): Fraction(2, 1)})
Poly7 = poly_mul(Poly1, Poly4)
Poly10 = poly_add(Poly7, Poly5)

Poly8 = Polynomial({(5, 0, 0): -1, (0, 0, 1): 1})
Poly9 = Polynomial({(3, 0, 0): -1, (0, 1, 0): 1})
Poly11 = Polynomial({(0, 0, 1): 1})

def test_methods():
    print(poly_add(Poly1, Poly2))
    print(poly_subtract(Poly1, Poly2))
    print(poly_mul(Poly1, Poly2))
    print(poly_div(Poly1, Poly2))
    print(poly_div(Poly5, Poly4))
    print(reduction(Poly4, [Poly4, Poly5, Poly6]))
    print(reduction(Poly0, [Poly4, Poly5, Poly6]))

def test_buchberger():
    Polys = buchberger([Poly4, Poly5])
    for poly in Polys:
        print(poly.data)

def test_ideal_mem():
    assert ideal_membership(Poly0, [Poly4, Poly5])
    assert ideal_membership(Poly4, [Poly4, Poly5])
    assert ideal_membership(Poly7, [Poly4, Poly5])
    assert ideal_membership(Poly10, [Poly4, Poly5])
    assert not ideal_membership(Poly11, [Poly4, Poly5])

    assert ideal_membership(Poly1, [Poly1, Poly4, Poly5]) 
    assert ideal_membership(Poly10, [Poly1, Poly4, Poly5]) 
