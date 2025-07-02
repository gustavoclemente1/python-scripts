## This code defines a simple class `Point` with an initializer and a method to get the coordinates. 

class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def get(self):
        return (self.x, self.y)
    
a = Point(1,2)
print(a.get())

        
        