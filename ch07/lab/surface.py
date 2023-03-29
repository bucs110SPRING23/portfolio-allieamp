import rectangle
class Surface: #does the whole class get a docstring or the individual defines
    def __init__(self, filename, x=50, y=50, h=25, w=50): 
        self.rect = rectangle.Rectangle(x,y,h,w)
        self.image = str(filename)
    def getRect(self):
        """
        This  returns the internal Rectangle attribute from surface
        args: self
        return: self.rect as a Rectangle object
        """
        return self.rect
    