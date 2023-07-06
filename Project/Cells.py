import numpy as np
class Cell:
    def __init__(self,x,y,cell_type,vegetobDensity):
        self.x = x
        self.y = y
        self.cell_type = cell_type # water or land
        self.vegetobDensity = vegetobDensity # 0-100
        self.herd = np.empty(0,dtype=Erbast)
        self.pride = np.empty(0,dtype=Carviz)

    def __str__(self):
        return f"{self.x},{self.y}-{len(self.herd)}"
    
    def __int__(self):
        return self.vegetobDensity
    
    def Vegetob(self):
        return self.vegetobDensity/100*255
    def Erbast(self):
        return len(self.herd)/10*255
    def Carviz(self):
        return len(self.pride)/10*255
    
    def RGB(self):
        if self.cell_type == "water":
            return [0,0,255]
        else:
            return [self.Carviz(),self.Erbast(),self.Vegetob()]


class Erbast:
    def __init__(self,energy,lifetime,age,socialAttitude):
        self.energy = energy 
        self.lifetime = lifetime 
        self.age = age # 0-lifetime
        self.socialAttitude = socialAttitude # 0-1

class Carviz:
    def __init__(self,energy,lifetime,age,socialAttitude):
        self.energy = energy 
        self.lifetime = lifetime 
        self.socialAttitude = socialAttitude
