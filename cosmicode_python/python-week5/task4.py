class complex:
    def __init__(self,real,imaginary):
        self.real=real
        self.imaginary=imaginary
    def __add__(self,other):
        return complex(self.real+other.real,self.imaginary+other.imaginary)
    def __sub__(self,other):
        return complex(self.real-other.real,self.imaginary-other.imaginary)
    def __mul__(self,other):
        real=(self.real*other.real)-(self.imaginary*other.imaginary)
        imaginary=(self.real*other.imaginary)+(self.imaginary*other.real)
        return complex(real,imaginary)
    def __truediv__(self,other):
        denominator = (other.real ** 2) + (other.imaginary ** 2)
        real_part = (self.real * other.real + self.imaginary * other.imaginary) / denominator
        imag_part = (self.imaginary * other.real - self.real * other.imaginary) / denominator
        return complex(real_part, imag_part)
    def __str__(self):
        return f"{self.real} + {self.imaginary}i"

n1=complex(3,5)
n2=complex(5,6)
print("-----------------------")
print(n1)
print(n2)
print("Addition: ",n1+n2)
print("Subtraction: ",n1-n2)
print("Multiplication: ",n1*n2)
print("Division: ",n1/n2)
print("-----------------------")