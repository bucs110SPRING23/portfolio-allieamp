class Enemy:
  def __init__(self, size=1, speed=5, health=0):
    """
    """
    self.size = size
    self.speed = speed #start medium speed
    self.health = health # before they get stomped
class Pipe:
    """
    """
    def __init__(self, size=10, color = "green",xtube=50,ytube=50):
        self.reg_size = size #start out standard size
        self.is_open = False #start travleable
        self.color = color # normally green
        self.xtube = xtube
        self.ytube = ytube
class Box:
   def __init__(self, size=10,xbox=50,ybox=50):
        self.size = size
        self.xbox = xbox
        self.ybox = ybox
        self.is_mystery = False
