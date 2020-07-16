"""
Write a function that takes a 2D binary array and returns the number of 1 islands. An island consists of 1s that are connected to the north, south, east or west. For example:

islands = [[0, 1, 0, 1, 0],
           [1, 1, 0, 1, 1],
           [0, 0, 1, 0, 0],
           [1, 0, 1, 0, 0],
           [1, 1, 0, 0, 0]]
island_counter(islands) # returns 4
"""

# What are the nodes? 1s
# What are the edges? Connected to N / S / E / W
# What are islands? Connected components

islands = [[0, 1, 0, 1, 0],
           [1, 1, 0, 1, 1],
           [0, 0, 1, 0, 0],
           [1, 0, 1, 0, 0],
           [1, 1, 0, 0, 0]]

def get_neighbors(node, matrix):
  row, col = node
  neighbors = []

  stepNorth = stepSouth = stepWest = stepEast = False

  if row > 0:
    stepNorth = row - 1
  
  if row < len(matrix) - 1:
    stepSouth = row + 1

  if col < len(matrix[row]) - 1:
    stepEast = col + 1
  
  if col > 0:
    stepWest = col - 1

  if stepNorth is not False and matrix[stepNorth][col] == 1:
    neighbors.append((stepNorth, col))
  
  if stepSouth is not False and matrix[stepSouth][col] == 1:
    neighbors.append((stepSouth, col))
  
  if stepEast is not False and matrix[row][stepEast] == 1:
    neighbors.append((row, stepEast))

  if stepWest is not False and matrix[row][stepWest] == 1:
    neighbors.append((row, stepWest))
  
  return neighbors

def dft_recursive(node, visited, matrix):
  if node not in visited:
    visited.add(node)

    neighbors = get_neighbors(node, matrix)

    for neighbor in neighbors:
      dft_recursive(neighbor, visited, matrix)

def islands_counter(isles):
  visited = set()
  number_islands = 0

  # Iterate through matrix
  for row in range(len(isles)):
    for col in range(len(isles[row])):
      node = (row, col)

      # When a 1 appears, if it's not in visited traverse through "island"
      if node not in visited and isles[row][col] == 1:
        number_islands += 1
        dft_recursive(node, visited, isles)

  return number_islands

print(islands_counter(islands))