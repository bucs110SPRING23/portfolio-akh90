

class Rectangle:
    """
    A class that represents a rectangle with a position and size
    """
    def __init__(self, x, y, h, w):
        """
        Initializes a Rectangle object with the given x, y, height, and width.
        If any of the values are less than zero, sets them to their absolute value.
        """
        self.x = abs(x)
        self.y = abs(y)
        self.height = abs(h)
        self.width = abs(w)

    def __str__(self):
        """
        Returns a string representation of the Rectangle object.
        """
        
        return f"(x: {self.x}, y: {self.y}) width: {self.width}, height: {self.height}"

