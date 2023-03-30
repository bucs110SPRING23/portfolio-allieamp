class Rectangle:
    def __init__(self, x=100, y=100, h=50, w=100):
        self.x = abs(x)
        self.y = abs(y)
        self.height = abs(h)
        self.width = abs(w)
    def __str__(self):
        """
        This returns a string containing the x, y, width, and height of the rectangle
        args: self as Rectangle class
        return: ((x,y),height,width) as a string
        """
        return ((self.x,self.y), self.height,self.width)