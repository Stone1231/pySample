
class Dog(): 
    """Represent a dog.""" 
    def __init__(self, name, heigh, weight): 
        """Initialize dog object.""" 
        self.name = name 
        self.heigh = heigh
        self.weight = weight
        self.persion = Persion('stone')
    def sit(self): 
        """Simulate sitting.""" 
        print(self.persion.name + "'s " + self.name + " is sitting.") 


class Persion():
    def __init__(self, name):
        self.name =name
  
class Master():
    def __init__(self, name):
        self.name =name
        self.dogs = [Dog('', 0, 0)]