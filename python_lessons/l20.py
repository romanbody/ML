import math

class Complex(object):
    def __init__(self, real=0, imaginary=0):
        self.real = real
        self.imaginary = imaginary  
    def __add__(self, no):
        res = Complex()
        res.real = self.real + no.real;
        res.imaginary = self.imaginary + no.imaginary;
        return(res)
    def __sub__(self, no):
        res = Complex()
        res.real = self.real - no.real;
        res.imaginary = self.imaginary - no.imaginary;
        return(res)
        
    def __mul__(self, no):
        res = Complex()
        res.real = self.real*no.real - self.imaginary*no.imaginary;
        res.imaginary = self.real*no.imaginary + no.real*self.imaginary;
        return(res)

    def __truediv__(self, no):
        res = Complex()
        res.real = (self.real*no.real + self.imaginary*no.imaginary)/(no.real**2+no.imaginary**2);
        res.imaginary = (self.imaginary*no.real - self.real*no.imaginary)/(no.real**2+no.imaginary**2);
        return(res)

    def mod(self):
        res = Complex()
        res.real = math.sqrt(self.real**2+self.imaginary**2);
        res.imaginary = 0;
        return(res)

    def __str__(self):
        if self.imaginary == 0:
            result = "%.2f+0.00i" % (self.real)
        elif self.real == 0:
            if self.imaginary >= 0:
                result = "0.00+%.2fi" % (self.imaginary)
            else:
                result = "0.00-%.2fi" % (abs(self.imaginary))
        elif self.imaginary > 0:
            result = "%.2f+%.2fi" % (self.real, self.imaginary)
        else:
            result = "%.2f-%.2fi" % (self.real, abs(self.imaginary))
        return result


if __name__ == '__main__':
    c = map(float, input().split())
    d = map(float, input().split())
    x = Complex(*c)
    y = Complex(*d)
    z = x + y
    print(*map(str, [x+y, x-y, x*y, x/y, x.mod(), y.mod()]), sep='\n')