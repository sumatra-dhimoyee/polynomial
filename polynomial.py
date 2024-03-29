class X:
    def __init__(self):
        pass

    def __repr__(self):
        return "X"

class Int:
    def __init__(self, i):
        self.i = i
    
    def __repr__(self):
        return str(self.i)

class Add:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
    
    def __repr__(self):
        return repr(self.p1) + " + " + repr(self.p2)
    
class Sub:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
    
    def __repr__(self):
        return repr(self.p1) + " - " + repr(self.p2)

class Mul:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
    
    def __repr__(self):
        if isinstance(self.p1, Add):
            if isinstance(self.p2, Add):
                 return "( " + repr(self.p1) + " ) * ( " + repr(self.p2) + " )"
            return "( " + repr(self.p1) + " ) * " + repr(self.p2)
        if isinstance(self.p2, Add):
            return repr(self.p1) + " * ( " + repr(self.p2) + " )"

        if isinstance(self.p1, Sub):
            if isinstance(self.p2, Sub):
                 return "( " + repr(self.p1) + " ) * ( " + repr(self.p2) + " )"
            return "( " + repr(self.p1) + " ) * " + repr(self.p2)
        if isinstance(self.p2, Sub):
            return repr(self.p1) + " * ( " + repr(self.p2) + " )"

        if isinstance(self.p1, Div):
            if isinstance(self.p2, Div):
                 return "( " + repr(self.p1) + " ) * ( " + repr(self.p2) + " )"
            return "( " + repr(self.p1) + " ) * " + repr(self.p2)
        if isinstance(self.p2, Div):
            return repr(self.p1) + " * ( " + repr(self.p2) + " )"

        return repr(self.p1) + " * " + repr(self.p2)
    
class Div:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
    
    def __repr__(self):
        if isinstance(self.p1, Add):
            if isinstance(self.p2, Add):
                 return "( " + repr(self.p1) + " ) / ( " + repr(self.p2) + " )"
            return "( " + repr(self.p1) + " ) / " + repr(self.p2)
        if isinstance(self.p2, Add):
            return repr(self.p1) + " / ( " + repr(self.p2) + " )"

        if isinstance(self.p1, Sub):
            if isinstance(self.p2, Sub):
                 return "( " + repr(self.p1) + " ) / ( " + repr(self.p2) + " )"
            return "( " + repr(self.p1) + " ) / " + repr(self.p2)
        if isinstance(self.p2, Sub):
            return repr(self.p1) + " / ( " + repr(self.p2) + " )"

        if isinstance(self.p1, Mul):
            if isinstance(self.p2, Mul):
                 return "( " + repr(self.p1) + " ) / ( " + repr(self.p2) + " )"
            return "( " + repr(self.p1) + " ) / " + repr(self.p2)
        if isinstance(self.p2, Mul):
            return repr(self.p1) + " / ( " + repr(self.p2) + " )"

        return repr(self.p1) + " / " + repr(self.p2)


poly = Add( Add( Int(4), Int(3)), Add( X(), Mul( Int(1), Add( Mul(X(), X()), Int(1)))))
print(poly)

#x^2+1/x+x^3+3x-2
poly1= Add(Add(Add(Mul(X(), X()), Div(Int(1), X())), Mul(Mul(X(), X()), X())),Sub(Mul(Int(3), X()), Int(2)))
print(poly1)

#1/(x^2)+2/(x^3)-x^3
poly2= Sub(Add(Div(Int(1), Mul(X(), X())), Div(Int(2), Mul(X(), Mul(X(), X())))), Mul(X(), Mul(X(), X())))
print(poly2)

#x^3/x +1
poly3= Add(Div(Mul(Mul(X(), X()), X()), X()), Int(1))
print(poly3)

#x^3/x^2 +16
poly4= Add(Div(Mul(Mul(X(), X()), X()), Mul(X(), X())), Int(16))
print(poly4)
class X:
    def __init__(self):
        pass

    def __repr__(self):
        return "X"
    
    def evaluate(self, x):
        return x

class Int:
    def __init__(self, i):
        self.i = i
    
    def __repr__(self):
        return str(self.i)
    
    def evaluate(self, x):
        return self.i

class Add:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
    
    def __repr__(self):
        return repr(self.p1) + " + " + repr(self.p2)
    
    def evaluate(self, x):
        return self.p1.evaluate(x) + self.p2.evaluate(x)
    
class Sub:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
    
    def __repr__(self):
        return repr(self.p1) + " - " + repr(self.p2)
    
    def evaluate(self, x):
        return self.p1.evaluate(x) - self.p2.evaluate(x)

class Mul:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
    
    def __repr__(self):
        if isinstance(self.p1, Add):
            if isinstance(self.p2, Add):
                 return "( " + repr(self.p1) + " ) * ( " + repr(self.p2) + " )"
            return "( " + repr(self.p1) + " ) * " + repr(self.p2)
        if isinstance(self.p2, Add):
            return repr(self.p1) + " * ( " + repr(self.p2) + " )"

        if isinstance(self.p1, Sub):
            if isinstance(self.p2, Sub):
                 return "( " + repr(self.p1) + " ) * ( " + repr(self.p2) + " )"
            return "( " + repr(self.p1) + " ) * " + repr(self.p2)
        if isinstance(self.p2, Sub):
            return repr(self.p1) + " * ( " + repr(self.p2) + " )"

        if isinstance(self.p1, Div):
            if isinstance(self.p2, Div):
                 return "( " + repr(self.p1) + " ) * ( " + repr(self.p2) + " )"
            return "( " + repr(self.p1) + " ) * " + repr(self.p2)
        if isinstance(self.p2, Div):
            return repr(self.p1) + " * ( " + repr(self.p2) + " )"

        return repr(self.p1) + " * " + repr(self.p2)

    def evaluate(self, x):
        return self.p1.evaluate(x) * self.p2.evaluate(x)
    
class Div:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
    
    def __repr__(self):
        if isinstance(self.p1, Add):
            if isinstance(self.p2, Add):
                 return "( " + repr(self.p1) + " ) / ( " + repr(self.p2) + " )"
            return "( " + repr(self.p1) + " ) / " + repr(self.p2)
        if isinstance(self.p2, Add):
            return repr(self.p1) + " / ( " + repr(self.p2) + " )"

        if isinstance(self.p1, Sub):
            if isinstance(self.p2, Sub):
                 return "( " + repr(self.p1) + " ) / ( " + repr(self.p2) + " )"
            return "( " + repr(self.p1) + " ) / " + repr(self.p2)
        if isinstance(self.p2, Sub):
            return repr(self.p1) + " / ( " + repr(self.p2) + " )"

        if isinstance(self.p1, Mul):
            if isinstance(self.p2, Mul):
                 return "( " + repr(self.p1) + " ) / ( " + repr(self.p2) + " )"
            return "( " + repr(self.p1) + " ) / " + repr(self.p2)
        if isinstance(self.p2, Mul):
            return repr(self.p1) + " / ( " + repr(self.p2) + " )"

        return repr(self.p1) + " / " + repr(self.p2)
    
    def evaluate(self, x):
        return self.p1.evaluate(x) / self.p2.evaluate(x)


poly = Add( Add( Int(4), Int(3)), Add( X(), Mul( Int(1), Add( Mul(X(), X()), Int(1)))))
print(poly)
print(poly.evaluate(-1))  

#x^2+1/x+x^3+3x-2
poly1= Add(Add(Add(Mul(X(), X()), Div(Int(1), X())), Mul(Mul(X(), X()), X())),Sub(Mul(Int(3), X()), Int(2)))
print(poly1)
print(poly1.evaluate(2))

#1/(x^2)+2/(x^3)-x^3
poly2= Sub(Add(Div(Int(1), Mul(X(), X())), Div(Int(2), Mul(X(), Mul(X(), X())))), Mul(X(), Mul(X(), X())))
print(poly2)
print(poly2.evaluate(3))

#x^3/x +1
poly3= Add(Div(Mul(Mul(X(), X()), X()), X()), Int(1))
print(poly3)
print(poly3.evaluate(4))

#x^3/x^2 +16
poly4= Add(Div(Mul(Mul(X(), X()), X()), Mul(X(), X())), Int(16))
print(poly4)
print(poly4.evaluate(5)) 