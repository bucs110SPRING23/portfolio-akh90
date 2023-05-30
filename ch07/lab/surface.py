from rectangle import Rectangle

class Surface:
    """
    A class that represents an object's appearance and location in space.
    """
    def __init__(self, filename, x, y, h, w):
        """
        Initializes a Surface object with the given filename, x, y, height, and width.
        Creates a Rectangle object stored in self.rect.
        """
        self.image = filename
        self.rect = Rectangle(x, y, h, w)

    def getRect(self):
        """
        Returns the Rectangle object stored in self.rect.
        """
        return self.rect
