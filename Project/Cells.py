class Cell:
    def __init__(self,x,y,cell_type,vegetobDensity = 0):
        self.x = x
        self.y = y
        self.cell_type = cell_type # water or land
        self.vegetobDensity = vegetobDensity # 0-100
        self.herd = []
        self.pride = []

class Erbast:
    def __init__(self,energy,lifetime,age,socialAttitude,vegetobDensity = 0):
        self.energy = energy 
        self.lifetime = lifetime 
        self.age = age # 0-lifetime
        self.socialAttitude = socialAttitude # 0-1

class Carviz:
    def __init__(self,energy,lifetime,age,socialAttitude,vegetobDensity = 0):
        self.energy = energy 
        self.lifetime = lifetime 
        self.age = age # 0-lifetime
        self.socialAttitude = socialAttitude # 0-1
