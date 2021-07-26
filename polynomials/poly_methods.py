from fractions import Fraction
from polynomials.polynomial import Polynomial

def poly_add(Poly_1, Poly_2):
    """Adds two polynomials together.
    
    Arguments:
    Poly_1, Poly_2 -- instances of Polynomial.
    
    Returns:
    Poly_1 + Poly_2 -- An instance of Polynomial."""

    all_keys = set(Poly_1.get_monomials() + Poly_2.get_monomials())

    return Polynomial({
        key: Poly_1.data.get(key, 0)+Poly_2.data.get(key, 0) \
        for key in all_keys \
        if Poly_1.data.get(key, 0)+Poly_2.data.get(key, 0) != 0
    })

def poly_subtract(Poly_1, Poly_2):
    """Subtracts one polynomial from another.
    
    Arguments:
    Poly_1, Poly_2 -- instances of Polynomial.
    
    Returns:
    Poly_1 - Poly_2 -- An instance of Polynomial."""

    return poly_add(Poly_1, Poly_2.additive_inverse())

def poly_mul(Poly_1, Poly_2):
    """Multiplies two polynomials together.
    
    Arguments:
    Poly_1, Poly_2 -- instances of Polynomial.
    
    Returns:
    Poly_1*Poly_2 -- An instance of Polynomial."""    

    multiplied_poly = {}
    
    for i, key1 in enumerate(Poly_1.data):
        for j, key2 in enumerate(Poly_2.data):
            
            new_key = tuple([sum(term) for term in zip(key1, key2)])
            new_coeff = Poly_1.data[key1]*Poly_2.data[key2]

            if new_key not in multiplied_poly:
                multiplied_poly[new_key] = new_coeff
            else:
                multiplied_poly[new_key] += new_coeff

    return Polynomial({k: v for k, v in multiplied_poly.items() if v != 0})

def poly_div(Poly_1, Poly_2):
    """Computes the remainder of a polynomial division.
    
    Arguments:
    Poly_1, Poly_2 -- instances of Polynomial.
    
    Returns:
    Poly_1 - Poly_K*Poly_2 -- an instance of Polynomial,
        where Poly_K is chosen to cancel the leading term of Poly_1.
    
    Raises:
    DivisionByZeroError -- If Poly_2 is 0."""  

    if Poly_2.is_zero:
        raise ZeroDivisionError("Can't divide by the zero polynomial.")

    if Poly_1.is_zero:
        return Poly_1

    #Define Poly_K and check that Poly_K is not a Laurent polynomial.
    K_coeff = Fraction(Poly_1.leading_coeff, Poly_2.leading_coeff)
    K_term = tuple([
        exp1 - exp2 \
        for exp1, exp2 in zip(Poly_1.leading_monomial, Poly_2.leading_monomial)
    ])
    if any([exp < 0 for exp in K_term]):
        return Poly_1
    K_Poly = Polynomial({K_term: K_coeff})

    return poly_add(Poly_1, poly_mul(K_Poly, Poly_2).additive_inverse())

def reduction(Poly, Poly_set):
    """Computes the reduction of a polynomial by a set of polynomials.
    
    Arguments:
    Poly -- instance of Polynomial.
    Poly_set -- a list of Polynomial instances.
    
    Returns:
    Reduced_poly -- the reduction of Poly by Poly_set, defined as the
        remainder of polynomial division when Poly is iteratively divided
        by elements of Poly_set, in order of decreasing array index."""  

    Reduced_poly = Polynomial(Poly.data)
    Poly_set_copy = Poly_set[:]

    while Poly_set_copy:
        Reduced_poly = poly_div(Reduced_poly, Poly_set_copy[-1])
        Poly_set_copy.pop()

    if Reduced_poly.data != Poly.data:
        return reduction(Reduced_poly, Poly_set)
    else:
        return Reduced_poly

def poly_sort(Poly_set):
    """Returns a sorted list of polynomials.
    
    Arguments:
    Poly_set -- a list of Polynomial instances.
    
    Returns:
    Poly_set -- sorted by lexicographic ordering."""

    Poly_set.sort(key=lambda x: x.leading_monomial)