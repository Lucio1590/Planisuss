import numpy as np
import matplotlib.pyplot as plt
# import Cells
import planisuss_constants

class Cell:
    def __init__(self,x,y,cell_type,vegetobDensity):
        self.x = x
        self.y = y
        self.cell_type = cell_type # water or land
        self.vegetobDensity = vegetobDensity # 0-100
        self.herd = np.empty(0,dtype=object)
        self.pride = np.empty(0,dtype=object)
    #when cast to int retun the vegetobDensity
    # def __int__(self):
    #     return np.dstack((self.vegetobDensity,len(self.herd),len(self.pride)))
    
    def __str__(self):
        return f"Cell({self.x},{self.y},{self.cell_type},{self.vegetobDensity})"
    
    def Rgb(self):
        if self.cell_type == "water":
            return [0,0,255]
        else:
            return [len(self.pride),len(self.herd),self.vegetobDensity]

#main 
def main():
    #create a cell grid of NUMCELLS x NUMCELLS using numpy full of cell objects each with a random vegetobDensity using full_like
    cell_grid = np.empty((planisuss_constants.NUMCELLS,planisuss_constants.NUMCELLS),dtype=Cell)

    for i in range(planisuss_constants.NUMCELLS):
        for j in range(planisuss_constants.NUMCELLS):
            #make the border cells water (-1) and the rest land (0-100)
            if i == 0 or i == planisuss_constants.NUMCELLS-1 or j == 0 or j == planisuss_constants.NUMCELLS-1:
                cell_grid[i][j] = Cell(i,j,"water",-1)
            else:
                cell_grid[i][j] = Cell(i,j,"land",np.random.randint(0,100))
            
    #map cell_grid every cell to a rgb value numpy map
    rgb_grid = np.empty((planisuss_constants.NUMCELLS,planisuss_constants.NUMCELLS,3))
    for i in range(planisuss_constants.NUMCELLS):
        for j in range(planisuss_constants.NUMCELLS):
            rgb_grid[i][j] = cell_grid[i][j].Rgb()
    
    plt.imshow(rgb_grid)
    plt.colorbar()

    plt.show()

if __name__ == "__main__":
    main()