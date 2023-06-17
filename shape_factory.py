# shape_factory.py

from shape import Rectangle, Circle

class ShapeFactory:
    def create_shape(self, shape_type):
        if shape_type == "rectangle":
            return Rectangle()
        elif shape_type == "circle":
            return Circle()
        else:
            raise ValueError("Invalid shape type.")
