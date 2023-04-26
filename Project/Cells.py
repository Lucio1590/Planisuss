import numpy as np
class Cell:
    def __init__(self,x,y,cell_type,vegetobDensity,herdDimension=0,prideDimension=0):
        self.x = x
        self.y = y
        self.cell_type = cell_type # water or land
        self.vegetobDensity = vegetobDensity # 0-100
        self.herd = np.empty(herdDimension,dtype=object)
        self.pride = np.empty(prideDimension,dtype=object)
    #when cast to int retun the vegetobDensity
    # def __int__(self):
    #     return np.dstack((self.vegetobDensity,len(self.herd),len(self.pride)))
    
    def __str__(self):
        return f"Cell({self.x},{self.y},herd:{len(self.herd)}, pride:{len(self.pride)} ,{self.vegetobDensity})"
    
    def __int__(self):
        return self.vegetobDensity

    def RGB(self):
        if self.cell_type == "water":
            return [0,0,255]
        else:
            return [len(self.pride)/10*255,len(self.herd)/10*255,self.vegetobDensity/100*255]
        
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
