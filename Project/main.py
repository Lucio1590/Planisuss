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
                cell_grid[i][j] = Cell(i,j,"land",np.random.randint(0,100),np.random.randint(0,10),np.random.randint(0,10))
            
    #map cell_grid every cell to a rgb value numpy map
    # rgb_grid = np.empty((planisuss_constants.NUMCELLS,planisuss_constants.NUMCELLS,3))
    # for i in range(planisuss_constants.NUMCELLS):
    #     for j in range(planisuss_constants.NUMCELLS):
    #         rgb_grid[i][j] = cell_grid[i][j].Rgb()
    
    
    # rgb_grid = np.array([[cell_grid[i][j].RGB() for j in range(planisuss_constants.NUMCELLS)] for i in range(planisuss_constants.NUMCELLS)])

    # plt.imshow(rgb_grid.astype(np.uint8))
    # plt.colorbar()
 
    # plt.show()

    #update the vegetobDensity of each cell
    for i in range(planisuss_constants.NUMCELLS):
        for j in range(planisuss_constants.NUMCELLS):
            cell_grid[i][j].vegetobDensity += planisuss_constants.GROWING
            if cell_grid[i][j].vegetobDensity > 100:
                cell_grid[i][j].vegetobDensity = 100
    
    
    # def update_plot():
    #     for i in range(planisuss_constants.NUMCELLS):
    #         for j in range(planisuss_constants.NUMCELLS):
    #             cell_grid[i][j].vegetobDensity += planisuss_constants.GROWING
    #             if cell_grid[i][j].vegetobDensity > 100:
    #                 cell_grid[i][j].vegetobDensity = 100
    #     im.set_data(np.array([[cell_grid[i][j].RGB() for j in range(planisuss_constants.NUMCELLS)] for i in range(planisuss_constants.NUMCELLS)]))
    #     return im
    
    def update(frame):
        for i in range(planisuss_constants.NUMCELLS):
            for j in range(planisuss_constants.NUMCELLS):
                cell_grid[i][j].vegetobDensity += planisuss_constants.GROWING
                if cell_grid[i][j].vegetobDensity > 100:
                    cell_grid[i][j].vegetobDensity = 100
        im.set_data(np.array([[cell_grid[i][j].RGB() for j in range(planisuss_constants.NUMCELLS)] for i in range(planisuss_constants.NUMCELLS)]).astype(np.uint8))
        return [im]

    rgb_grid = np.array([[cell_grid[i][j].RGB() for j in range(planisuss_constants.NUMCELLS)] for i in range(planisuss_constants.NUMCELLS)])
    #animate plot
    # plt.imshow(updated_rgb_grid.astype(np.uint8))
    fig, ax = plt.subplots()

# Display the matrix as an image
    im = ax.imshow(rgb_grid)


    anim = animation.FuncAnimation(fig, update, frames=100, interval=10, blit=True)

    plt.show()
   

        

if __name__ == "__main__":
    main()