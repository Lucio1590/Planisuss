 
import numpy as np
import matplotlib.pyplot as plt

A = np.asarray([[5, 9, 6, 1, 6, 7], [6, 4, 0, 5, 9, 8],
                [3, 6, 8, 8, 2, 7], [0, 9, 5, 9, 6, 8], [1, 2, 3, 4, 5, 9]])

plt.figure(2)
plt.imshow(A)
plt.yticks([0, 1, 2, 3, 4])
plt.colorbar()
plt.show()

