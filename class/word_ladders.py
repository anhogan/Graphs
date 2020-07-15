import string

class Queue():
    def __init__(self):
        self.queue = []

    def enqueue(self, value):
        self.queue.append(value)

    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None

    def size(self):
        return len(self.queue)

word_list = set()

for word in words:
  word_list.add(word.lower())

# For every letter in the word, swap with a letter in the alphabet
# If new word in word list, add as neighbor
def get_neighbors(word):
  neighbors = []

  for index in range(len(word)):
    for letter in string.ascii_lowercase:
      word_list = list(word)
      word_list[index] = letter

      new_word = ''.join(word_list)

      if new_word in word_list:
        neighbors.append(new_word)
  
  return neighbors

def word_ladders(start_word, end_word):
  q = Queue()
  visited = set()

  q.enqueue([start_word])

  while q.size() > 0:
    current_path = q.dequeue()
    current_word = current_path[-1]

    if current_word == end_word:
      return current_path

    if current_word not in visited:
      visited.add(current_word)
  
  neighbors = get_neighbors(current_word)
  # For neighbor in neihbors, enqueue(current_path + [neighbor])
  for neighbor in neighbors:
    q.enqueue(current_path + [neighbor])