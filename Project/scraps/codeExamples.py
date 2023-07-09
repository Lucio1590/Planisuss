def grow():
  for i in range(NUMCELLS):
    for j in range(NUMCELLS):
      if cells[i][j] == 1:
        vegetab[i][j] += GROWING

def move():
  for i in range(NUMCELLS):
    for j in range(NUMCELLS):
      if erbast[i][j] > 0:
        # Calculate the probability of moving
        probability = erbast / MAX_ENERGY
        # If the probability is greater than 0.5, move
        if np.random.random() > 0.5:
          # Choose a random direction
          direction = np.random.randint(4)
          # Move in the chosen direction
          if direction == 0:
            i -= 1
          elif direction == 1:
            i += 1
          elif direction == 2:
            j -= 1
          elif direction == 3:
            j += 1
          # If the new cell is not water, move there
          if cells[i][j] != 0:
            erbast[i][j] -= 1
            erbast[i][j] = np.clip(erbast[i][j], 0, MAX_ENERGY)
            erbast[i][j] += 1

def graze():
  for i in range(NUMCELLS):
    for j in range(NUMCELLS):
      if erbast[i][j] > 0 and vegetab[i][j] > 0:
        erbast[i][j] += vegetab[i][j] / 100
        vegetab[i][j] -= vegetab[i][j] / 100

def struggle():
  for i in range(NUMCELLS):
    for j in range(NUMCELLS):
      if carviz[i][j] > 0 and erbast[i][j] > 0:
        # Calculate the probability of winning the fight
        probability = carviz[i][j] / (erbast[i][j] + carviz[i][j])
        # If the probability is greater than 0.5, win the fight
        if np.random.random() > 0.5:
          # Erbast dies
          erbast[i][j] = 0
          # Carviz gains energy
          carviz[i][j] += 1

def spawn():
  for i in range(NUMCELLS):
    for j in range(NUMCELLS):
      if erbast[i][j] > 0:
        # Calculate the probability of spawning
        probability = erbast[i][j] / MAX_ENERGY
        # If the probability is greater than 0.5, spawn
        if np.random.random() > 0.5:
          # Choose a random direction
          direction = np.random.randint(4)
          # Spawn in the chosen direction
          if direction == 0:
            erbast[i - 1][j] += 1
          elif direction == 1:
            erbast[i + 1][j] += 1
          elif direction == 2:
            erbast[i][j - 1] += 1
          elif direction == 3:
            erbast[i][j + 1] += 1

# Run the simulation
for day in range(NUMDAYS):
  # Grow the vegetab
  grow()
  # Move the erbast
  move()
  # Graze the erbast
  graze()
  # Struggle
  struggle()
  # Spawn
  spawn()

# Plot the results
plt.figure()
plt.imshow(erbast)
plt.title("Erbast")
plt.show()

plt.figure()
plt.imshow(carviz)
plt.title("Carviz")
plt.show()