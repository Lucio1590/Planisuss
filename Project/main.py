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
        self.herd = []
        self.pride = []
    #when cast to int retun the vegetobDensity
    def __int__(self):
        return self.vegetobDensity
    

#main 
def main():
    #create a cell grid of NUMCELLS x NUMCELLS using numpy full of cell objects each with a random vegetobDensity using full_like
    cell_grid = np.empty((planisuss_constants.NUMCELLS,planisuss_constants.NUMCELLS),dtype=Cell)

    for i in range(planisuss_constants.NUMCELLS):
        for j in range(planisuss_constants.NUMCELLS):
            cell_grid[i][j] = Cell(i,j,"land",np.random.randint(0,100))
    
    
    #print(cell_grid.astype(int))
    plt.imshow(cell_grid.astype(int))
    # # plt.yticks(np.arange(0, planisuss_constants.NUMCELLS, 1))
    plt.colorbar()
    plt.show()

if __name__ == "__main__":
    main()