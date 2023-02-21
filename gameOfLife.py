import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


# Create a universe of randomly distributed black and white cells.
def create_universe(N=50, p=0.5):
    if p > 1 or p < 0:
        raise ValueError("p must be between 0 and 1")
    return np.random.choice([0, 1], size=(N, N), p=[1-p, p])

# Update the universe using the rules of the game.
def update_universe(universe):
    new_universe = np.zeros((N, N))
    for i in range(N):
        for j in range(N):
            n = (universe[(i+1)%N][j] + universe[(i-1)%N][j]
                 + universe[i][(j+1)%N] + universe[i][(j-1)%N]
                 + universe[(i+1)%N][(j+1)%N] + universe[(i-1)%N][(j-1)%N]
                 + universe[(i+1)%N][(j-1)%N] + universe[(i-1)%N][(j+1)%N])
            if universe[i][j] == 0 and n == 3:
                new_universe[i][j] = 1
            elif universe[i][j] == 1 and (n < 2 or n > 3):
                new_universe[i][j] = 0
            else:
                new_universe[i][j] = universe[i][j]
    return new_universe

# Create an animation of the universe evolving over time.
def animate(frame, universe, img):
    new_universe = update_universe(universe)
    img.set_data(new_universe)
    universe[:] = new_universe[:]
    return img
# Create a 50 x 50 universe of cells
N = 50
universe = create_universe(N=N, p=0.5)

# Create the plot
fig = plt.figure(figsize=(7, 7))
ax = plt.axes()
img = ax.imshow(universe, interpolation='nearest')

# Create the animation
ani = FuncAnimation(fig, animate, fargs=(universe, img,),
                    frames=200, interval=200, save_count=50)
plt.show()