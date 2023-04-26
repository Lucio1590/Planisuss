import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation    
from utils import normalize_matrix
import planisuss_constants

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
        return f"Cell({self.x},{self.y},{self.cell_type},{self.vegetobDensity})"
    
    def __int__(self):
        return self.vegetobDensity

    def RGB(self):
        if self.cell_type == "water":
            return [0,0,255]
        else:
            return [len(self.pride)/10*255,len(self.herd)/10*255,self.vegetobDensity/100*255]

def main():
    cell_grid = np.empty((planisuss_constants.NUMCELLS,planisuss_constants.NUMCELLS),dtype=Cell)

    for i in range(planisuss_constants.NUMCELLS):
        for j in range(planisuss_constants.NUMCELLS):
            if i == 0 or i == planisuss_constants.NUMCELLS-1 or j == 0 or j == planisuss_constants.NUMCELLS-1:
                cell_grid[i][j] = Cell(i,j,"water",-1)
            else:
                cell_grid[i][j] = Cell(i,j,"land",np.random.randint(0,100),np.random.randint(0,10),np.random.randint(0,10))
    

    for i in range(planisuss_constants.NUMCELLS):
        for j in range(planisuss_constants.NUMCELLS):
            cell_grid[i][j].vegetobDensity += planisuss_constants.GROWING
            if cell_grid[i][j].vegetobDensity > 100:
                cell_grid[i][j].vegetobDensity = 100
    
    def update(frame):
        for i in range(planisuss_constants.NUMCELLS):
            for j in range(planisuss_constants.NUMCELLS):
                cell_grid[i][j].vegetobDensity = np.random.randint(0,100)
                cell_grid[i][j].herd = np.empty(np.random.randint(0,10),dtype=object)
                cell_grid[i][j].pride = np.empty(np.random.randint(0,10),dtype=object)        
        im.set_data(np.array([[cell_grid[i][j].RGB() for j in range(planisuss_constants.NUMCELLS)] for i in range(planisuss_constants.NUMCELLS)]).astype(np.uint8))
        return [im]

    rgb_grid = np.array([[cell_grid[i][j].RGB() for j in range(planisuss_constants.NUMCELLS)] for i in range(planisuss_constants.NUMCELLS)])
    fig, ax = plt.subplots()
    im = ax.imshow(rgb_grid)
    animation.FuncAnimation(fig, update, frames=100, interval=100, blit=True)
    plt.show()
   
if __name__ == "__main__":
    main()