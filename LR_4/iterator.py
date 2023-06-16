class Circle:
    def __init__(self, radius):
        self.radius = radius

class Square:
    def __init__(self, side):
        self.side = side

class Triangle:
    def __init__(self, base, height):
        self.base = base
        self.height = height

class ShapeIterator:
    def __init__(self, shapes):
        self.shapes = shapes
        self.index = 0

    def __next__(self):
        if self.index < len(self.shapes):
            shape = self.shapes[self.index]
            self.index += 1
            return shape
        else:
            raise StopIteration
        
class ShapeCollection:
    def __init__(self):
        self.shapes = []

    def add_shape(self, shape):
        self.shapes.append(shape)

    def __iter__(self):
        return ShapeIterator(self.shapes)
    
shapes = ShapeCollection()
shapes.add_shape(Circle(5))
shapes.add_shape(Square(10))
shapes.add_shape(Triangle(6, 8))

for shape in shapes:
    print(shape)