import matplotlib.pyplot as plt
from perlin_noise import PerlinNoise
import numpy as np

noise = PerlinNoise(octaves=10, seed=np.random.randint(0,100))
pix = 100
pic = [[int((noise([i/pix, j/pix])+1)*25) for j in range(pix)] for i in range(pix)]

# print every value in our 2D list
print(pic)
print(np.array(pic).shape)

plt.imshow(pic, cmap='Greens')
plt.colorbar()
plt.show()