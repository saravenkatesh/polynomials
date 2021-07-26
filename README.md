# Polynomials

Polynomials is a package implementing the Buchberger algorithm for polynomials in 3 variables with fractional coefficients.


## Setup
To install, run 
```bash
$ pip install polynomials
```

## Usage
```python
import polynomials

#Instantiate the polynomial '2xyz^2 + 1/2x'
Poly = polynomials.polynomial.Polynomial({1, 1, 2}:2, {1, 0, 0}: Fraction(1, 2))

#Find a Grobner basis for a list of polynomials
G = polynomials.buchberger.buchberger([Poly_1, Poly_2])

#Check ideal membership 
polynomials.ideal_membership.ideal_membership(Poly, [Poly_1, Poly_2])
```