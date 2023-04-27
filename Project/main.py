# Import the necessary libraries
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation
import planisuss_constants
from Cells import Cell
from matplotlib.widgets import Button
from perlin_noise import PerlinNoise


# Create the cell grid
cell_grid = np.empty((planisuss_constants.NUMCELLS,planisuss_constants.NUMCELLS),dtype=Cell)
noise = PerlinNoise(octaves=planisuss_constants.NUMCELLS/10, seed=np.random.randint(0,100))
pix = planisuss_constants.NUMCELLS
noise_map = [[int((noise([i/pix, j/pix])+1)*25) for j in range(pix)] for i in range(pix)]
# Populate the cell grid with cells
for i in range(planisuss_constants.NUMCELLS):
    for j in range(planisuss_constants.NUMCELLS):
        if i == 0 or i == planisuss_constants.NUMCELLS-1 or j == 0 or j == planisuss_constants.NUMCELLS-1:
            cell_grid[i][j] = None
        else:
            cell_grid[i][j] = Cell(i,j,"land",noise_map[i][j],np.random.randint(0,10),np.random.randint(0,10))

# Initialise the animal populations
for i in range(planisuss_constants.NUMCELLS):
    for j in range(planisuss_constants.NUMCELLS):
        if cell_grid[i][j] is not None: # check only land cells
            cell_grid[i][j].vegetobDensity += planisuss_constants.GROWING
            if cell_grid[i][j].vegetobDensity > 100:
                cell_grid[i][j].vegetobDensity = 100
        
def gridToRgbArrey(grid):
    return np.array([[grid[i][j].RGB() if grid[i][j] is not None else [0,0,0] for j in range(planisuss_constants.NUMCELLS)] for i in range(planisuss_constants.NUMCELLS)]).astype(np.uint8)


# Create the function that will be called to update the display
def update(frame):
    # Update the animal populations
    print(frame)
    for i in range(planisuss_constants.NUMCELLS):
        for j in range(planisuss_constants.NUMCELLS):
            if cell_grid[i][j] is not None: # check only land cells
                # Update the vegetob density
                cell = cell_grid[i][j]
                cell.vegetobDensity += planisuss_constants.GROWING
                if cell.vegetobDensity > 100:
                    cell.vegetobDensity = 100
                cell.vegetobDensity -= len(cell_grid[i][j].herd)
                if cell.vegetobDensity < 0:
                    cell.vegetobDensity = 0
                    cell.herd = np.empty(0,dtype=object) # kill all the animals in the cell
                    cell.pride = np.empty(0,dtype=object) # kill all the animals in the cell

                
                cell.herd = np.empty(np.random.randint(0,10),dtype=object)
                cell.pride = np.empty(np.random.randint(0,10),dtype=object)
                # check cell neighbours
                # print(i,j)
                # print("------------------------------------------------------------------------------------")
                # neighbours = cell_grid[i-1:i+2,j-1:j+2] # get neighbours
                # neighbours = neighbours[neighbours != cell] # remove self
                # # remove water cells
                # neighbours = neighbours[np.vectorize(lambda x: x != None)(neighbours)]
                # for n in neighbours:
                #     print(n)
                # print("------------------------------------------------------------------------------------")
           
    # Update the display
    im.set_data(gridToRgbArrey(cell_grid))
    return [im]

# Create the display

#rgb_grid = np.array([[cell_grid[i][j].RGB() for j in range(planisuss_constants.NUMCELLS)] for i in range(planisuss_constants.NUMCELLS)]) # get the RGB values for each cell in the grid and store them in a numpy array


# get the RGB values for each cell in the grid and store them in a numpy array and convert the empty cells to black
rgb_grid = gridToRgbArrey(cell_grid)

fig, ax = plt.subplots()
im = ax.imshow(rgb_grid)

anim = animation.FuncAnimation(fig, update, frames=1, interval=1000, blit=True)



ax_pause = plt.axes([0.8, 0, 0.20, 0.085]) # type: ignore
bpause = Button(ax_pause, 'Stop')

def pause(event):
    anim.pause()
        

bpause.on_clicked(pause)

plt.show()
