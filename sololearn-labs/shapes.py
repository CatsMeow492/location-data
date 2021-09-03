class Shape: 
    def __init__(self, w, h):
        self.width = w
        self.height = h

    def area(self):
        print(self.width*self.height)

class Rectangle(Shape): #Create a rectangle subclass of shape
    def perimeter(self):
        print((self.width*2) + (self.height*2))

    

w = int(input())
h = int(input())

r = Rectangle(w, h)
r.area()
r.perimeter()