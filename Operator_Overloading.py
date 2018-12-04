##Using the concept of operator overloading in Python,
##change the behavior of the multiplication operator in a way that
##multiplication operator behaves like an addition operator.


class Number:
 
    def __init__(self,x):
        self.x = x
 
    def __mul__(self, other):
        x = self.x + other.x
        return x
 
a = Number(3)
 
b = Number(4)
 
print(a * b)


print('----------------------')

# Normal Addition

class Number:
 
    def __init__(self,x,y):
        self.x = x
        self.y = y
 
    def __mul__(self):
        total = self.x + self.y
        return total
 
a = Number(3,4)
 
print(a.__mul__())
