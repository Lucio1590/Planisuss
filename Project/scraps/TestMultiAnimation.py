import matplotlib.pyplot as plt
from matplotlib import animation
import numpy as np

# Create two matrices
A = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
B = np.array([[10, 20, 30], [40, 50, 60], [70, 80, 90]])

# Create two figures and two axes
fig, ax = plt.subplots(2,2)

# Plot the matrices
im1 = ax[0][0].imshow(A)
im2 = ax[1][1].imshow(B)

# Define the animation functions
def animate1(i):
  # Get new data
  new_data = np.random.randint(0, 10, (3, 3))

  # Update the matrix
  A = new_data

  # Update the plot
  im1.set_data(A)

def animate2(i):
  # Get new data
  new_data = np.random.randint(10, 100, (3, 3))

  # Update the matrix
  B = new_data

  # Update the plot
  im2.set_data(B)

# Create the animations
anim1 = animation.FuncAnimation(fig, animate2, frames=1, interval=1000)
anim2 = animation.FuncAnimation(fig, animate1, frames=1, interval=1000)

# Show the animations
plt.show()