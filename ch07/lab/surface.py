import rectangle
class Surface:
    def __init__(self, filename, x=50, y=50, h=25, w=50): 
        self.rect = rectangle.Rectangle(x,y,h,w)
        self.image = str(filename)
    def getRect(self):
        """
        This  returns the internal Rectangle attribute from surface
        args: self as surface class
        return: self.rect as a Rectangle object
        """
        return self.rect
    