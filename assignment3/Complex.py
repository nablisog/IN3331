class Complex():
    """
    This programm calculates complex numbers without the use of python module

    """

    def __init__(self, real, imag):
         self.real = real
         self.imag = imag


    def __str__(self):
          return "%.f %+ .fj" % (self.real, self.mag)


    def conjugate(self):
          x= self.imag*(-1)
          y=self.real
          return Complex(y, x)



    def modulus(self):
         return Complex(math.sqrt(self.real**2 + self.imag**2))



    def __add__(self, other):
         return Complex(self.real + other.real, self.imag + other.imag)



    def __sub__(self, other):
         return Complex(self.real - other.real, self.imag - other.imag)



    def __mul__(self,other):
          return Complex(self.real * other.real - self.imag * other.imag,
                         self.imag * other.real + self.real * other.imag)



    def __eq__(self, other):
        return self.real == other.real and self.imag == other.imag



    def __radd__(self, other):
          if isinstance(other, (int,float)):
            other= Complex(other)
          else:
               return self.__add__(other)


    def __rsub__(self,other):
        if isinstance(other, (int,float)):
            other= Complex(other)
        else:
            return self.__sub__(other)



    def __rmul__(self, other):
          return self.__mul__(other)
