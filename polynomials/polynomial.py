NUM_VARIABLES = 3

#TODO: implement error handing for invalid polynomial representations.
class Polynomial:
    """A class representing a polynomial.
    
    Arguments
    polynomial_data -- a dictionary representing a polynomial.  Each key is
        a tuple of length NUM_VARIABLES of non-negative integers.  Each value
        is a non-zero Fraction instance.

        Each key / value pair represents a monomial term.  For example,
        (1, 2, 3) : Fraction(4, 1) representions the monomial 4xy^2z^3 and the
        dictionary {(1, 2, 3) : Fraction(4, 1), (1, 0, 0): Fraction(1/2)}
        represents the polynomial 4*xy^2z^3 + 1/2*x.
        
        The zero polynomial is represented by the empty dictionary {}.
        
    Attributes
    data -- a dictionary representing the polynomial, as with polynomial_data.    
    
    Properties
    leading_term-- The maximum over all terms, according to lexicographic order.
    leading_coeff -- The coeff of leading_monomial.
    leading_monomial -- The leading_term divided by the leading_coeff.
    is_zero -- True if the polynomial is 0, False otherwise.
    
    Methods
    additive_inverse -- Returns the additive inverse.
    get_monomials -- Returns a list of all terms in the polynomial."""

    def __init__(self, polynomial_data):
        self.data = polynomial_data

    def __str__(self):
        return str(self.data)

    @property
    def leading_monomial(self):
        return max(self.data) if not self.is_zero else ()

    @property
    def leading_coeff(self):
        return self.data[self.leading_monomial] if not self.is_zero else 0

    @property
    def leading_term(self):
        if len(self.leading_monomial)==0:
            return Polynomial({})
        return Polynomial({self.leading_monomial: self.leading_coeff})

    @property
    def is_zero(self):
        return self.data=={}

    def additive_inverse(self):
        return Polynomial({k:-v for k,v in self.data.items()})

    def get_monomials(self):
        return list(self.data)
