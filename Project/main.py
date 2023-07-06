# Import the necessary libraries
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation
from planisuss_constants import NUMCELLS, NEIGHBORHOOD, GROWING
from Cells import Cell, Erbast, Carviz
from matplotlib.widgets import Button
from perlin_noise import PerlinNoise
import random


# FUNCTIONS
def createGrid(numCells):
    return np.empty((NUMCELLS,NUMCELLS),dtype=Cell)

def getNoiseMap():
    noise = PerlinNoise(octaves=NUMCELLS/10, seed=np.random.randint(0,100))
    pix = NUMCELLS
    noise_map = [[int((noise([i/pix, j/pix])+1)*50) for j in range(pix)] for i in range(pix)]
    return noise_map

def populateGrid(grid):
    noise_map = getNoiseMap()
    for i in range(NUMCELLS):
        for j in range(NUMCELLS):
            if i == 0 or i == NUMCELLS-1 or j == 0 or j == NUMCELLS-1:
                grid[i][j] = None
            else:
                grid[i][j] = Cell(i,j,"land",noise_map[i][j])
                #for each cell assign a herd of erbast
                grid[i][j].herd = [Erbast(5,50,0,random.choice([0,1]) ) for _ in range(0,random.randint(0,15))]
                grid[i][j].pride = [Carviz(5,50,0,random.choice([0,1]) ) for _ in range(0,random.randint(0,15))]

def getRgbGtidByCellType(grid, cellType):
    if(cellType == "vegetob_grid"):
        return np.array([[grid[i][j].vegetobDensity if grid[i][j] is not None else 0 for j in range(NUMCELLS)] for i in range(NUMCELLS)])
    elif(cellType == "erbast_grid"):
        return np.array([[len(grid[i][j].herd) if grid[i][j] is not None else 0 for j in range(NUMCELLS)] for i in range(NUMCELLS)])
    elif(cellType == "carviz_grid"):
        return np.array([[len(grid[i][j].pride) if grid[i][j] is not None else 0 for j in range(NUMCELLS)] for i in range(NUMCELLS)])
    else:
        return np.array([[grid[i][j].RGB() if grid[i][j] is not None else [0,0,0] for j in range(NUMCELLS)] for i in range(NUMCELLS)]).astype(np.uint8)

#INITIALIZATION
cell_grid = createGrid(NUMCELLS)
populateGrid(cell_grid)               

#ANIMATION
def update(frame,grid):
    for i in range(NUMCELLS):
        for j in range(NUMCELLS):
            if grid[i][j] is not None: # check only land cells
                # Update the vegetob density
                cell = grid[i][j]

                cell.vegetobDensity += GROWING
                if cell.vegetobDensity > 100:
                    cell.vegetobDensity = 100

    im.set_data(getRgbGtidByCellType(grid, "vegetob_grid"))
    # im1.set_data(getRgbGtidByCellType(cell_grid, "erbast_grid"))
    # im2.set_data(getRgbGtidByCellType(cell_grid, "carviz_grid"))
    im3.set_data(getRgbGtidByCellType(grid, "rgb_grid"))
    return [im]


vegetob_grid = getRgbGtidByCellType(cell_grid, "vegetob_grid")

#PLOT SETUP
fig, ax = plt.subplots(2,2)
ax[0][0].set_title("Vegetob Density")
im = ax[0][0].imshow(vegetob_grid, cmap='Greens', vmax=100, vmin=0)
ax[0][1].set_title("Erbast Density")
im1 = ax[0][1].imshow(getRgbGtidByCellType(cell_grid, "erbast_grid"), cmap='Blues', vmax=100, vmin=0)
ax[1][0].set_title("Carviz Density")
im2 = ax[1][0].imshow(getRgbGtidByCellType(cell_grid, "carviz_grid"), cmap='Reds', vmax=100, vmin=0)
ax[1][1].set_title("Overall Density")
im3 = ax[1][1].imshow(getRgbGtidByCellType(cell_grid, "rgb_grid"))
#ANIMATION
# anim = animation.FuncAnimation(fig, update, frames=1, interval=1000, blit=True)
anim = animation.FuncAnimation(fig, update, fargs=(cell_grid,), frames=1, interval=1000, blit=True)

# #STOP BUTTON
# ax_pause = plt.axes((0.8, 0, 0.20, 0.085))
# bpause = Button(ax_pause, 'Stop')
# bpause.on_clicked(anim.pause)


plt.show()
