from itertools import zip_longest

class Polynome:
    
    def __init__(self, *coefficients):
            """ input: coefficients are in the form a_n, ...a_1, a_0 
            """
            self.coefficients = list(coefficients) # tuple is turned into a list
    
    def __repr__(self):
        """
        method to return the canonical string representation 
        of a polynomial.
   
        """
        return "Polynome" + str(self.coefficients)
    
    def __str__(self):
        
        def x_expr(degree):
            if degree == 0:
                res = ""
            elif degree == 1:
                res = "x"
            else:
                res = "x^"+str(degree)
            return res

        degree = len(self.coefficients) - 1
        res = ""

        for i in range(0, degree+1):
            coeff = self.coefficients[i]
            # nothing has to be done if coeff is 0:
            if abs(coeff) == 1 and i < degree:
                res += f"{'+' if coeff>0 else '-'}{x_expr(degree-i)}"  
            elif coeff != 0:
                res += f"{coeff:+g}{x_expr(degree-i)}" 

        return res.lstrip('+')    
    
    def degree(self):
        if self.coefficients[0] == 0:
            return len(self.coefficients) - 1
        return len(self.coefficients)  
    
    def __add__(self, other):
        assert type(other) is Polynome, "Vous ne pouvez ajouter que deux polynomes"
        c1 = self.coefficients[::-1]
        c2 = other.coefficients[::-1]
        res = [sum(t) for t in zip_longest(c1, c2, fillvalue=0)]
        return Polynomial(*res[::-1])
    
    def __sub__(self, other):
        c1 = self.coefficients[::-1]
        c2 = other.coefficients[::-1]
        
        res = [t1-t2 for t1, t2 in zip_longest(c1, c2, fillvalue=0)]
        return Polynomial(*res[::-1])
    
    def __pos__(self):
        return self
    
    def __neg__(self):
        neg_coeffs = ()
        for i in self.coefficients:
            neg_coeffs.append(-i)
        return Polynome(neg_coeffs)
