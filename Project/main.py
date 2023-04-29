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
noise_map = [[int((noise([i/pix, j/pix])+1)*50) for j in range(pix)] for i in range(pix)]
# Populate the cell grid with cells
for i in range(planisuss_constants.NUMCELLS):
    for j in range(planisuss_constants.NUMCELLS):
        if i == 0 or i == planisuss_constants.NUMCELLS-1 or j == 0 or j == planisuss_constants.NUMCELLS-1:
            cell_grid[i][j] = None
        else:
            cell_grid[i][j] = Cell(i,j,"land",noise_map[i][j],np.random.randint(0,10),np.random.randint(0,10))

# # Initialise the animal populations
# for i in range(planisuss_constants.NUMCELLS):
#     for j in range(planisuss_constants.NUMCELLS):
#         if cell_grid[i][j] is not None: # check only land cells
#             cell_grid[i][j].vegetobDensity += planisuss_constants.GROWING
#             if cell_grid[i][j].vegetobDensity > 100:
#                 cell_grid[i][j].vegetobDensity = 100
        
def gridToRgbArrey(grid):
    return np.array([[grid[i][j].RGB() if grid[i][j] is not None else [0,0,0] for j in range(planisuss_constants.NUMCELLS)] for i in range(planisuss_constants.NUMCELLS)]).astype(np.uint8)

def gridToVegetobArrey(grid):
    return np.array([[grid[i][j].vegetobDensity if grid[i][j] is not None else 0 for j in range(planisuss_constants.NUMCELLS)] for i in range(planisuss_constants.NUMCELLS)])

# Create the function that will be called to update the display
def update(frame):
    # Update the animal populations
    for i in range(planisuss_constants.NUMCELLS):
        for j in range(planisuss_constants.NUMCELLS):
            if cell_grid[i][j] is not None: # check only land cells
                # Update the vegetob density
                cell = cell_grid[i][j]

                cell.vegetobDensity += planisuss_constants.GROWING
                if cell.vegetobDensity > 100:
                    cell.vegetobDensity = 100

                #get the grid of the neighborhood
                neighborhood = np.array([[cell_grid[i+ii][j+jj] if cell_grid[i+ii][j+jj] is not None else 0 for jj in range(-planisuss_constants.NEIGHBORHOOD,planisuss_constants.NEIGHBORHOOD+1)] for ii in range(-planisuss_constants.NEIGHBORHOOD,planisuss_constants.NEIGHBORHOOD+1)])
                
                if i == len(cell_grid)-2 and j == len(cell_grid)-2:
                    print(neighborhood.astype(int))

    # Update the display
    im.set_data(gridToVegetobArrey(cell_grid))
    return [im]

# Create the display
# rgb_grid = gridToRgbArrey(cell_grid)

vegetob_grid = np.array([[cell_grid[i][j].vegetobDensity if cell_grid[i][j] is not None else 0 for j in range(planisuss_constants.NUMCELLS)] for i in range(planisuss_constants.NUMCELLS)])
# carviz_grid = np.array([[len(cell_grid[i][j].pride) if cell_grid[i][j] is not None else 0 for j in range(planisuss_constants.NUMCELLS)] for i in range(planisuss_constants.NUMCELLS)])
# erbast_grid = np.array([[len(cell_grid[i][j].herd) if cell_grid[i][j] is not None else 0 for j in range(planisuss_constants.NUMCELLS)] for i in range(planisuss_constants.NUMCELLS)])

fig, ax = plt.subplots()
im = ax.imshow(vegetob_grid, cmap='Greens', vmax=100, vmin=0)

anim = animation.FuncAnimation(fig, update, frames=1, interval=1000, blit=True)

ax_pause = plt.axes([0.8, 0, 0.20, 0.085]) # type: ignore
bpause = Button(ax_pause, 'Stop')

def pause(event):
    anim.pause()

bpause.on_clicked(pause)

plt.show()
