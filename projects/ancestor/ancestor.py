class Graph:
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        if vertex_id not in self.vertices:
            self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        if v1 and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            print(f'Vertices must be valid')

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

def earliest_ancestor(ancestors, starting_node):
    # Build ancestor graph
    graph = Graph()

    for parent, child in ancestors:
        graph.add_vertex(parent)
        graph.add_vertex(child)
        graph.add_edge(child, parent)
    
    # BFS
    q = Queue()
    q.enqueue([starting_node])

    longest_path = 1
    earliest_ancestor = -1

    # If no parents, return -1
    if len(graph.vertices[starting_node]) == 0:
        return earliest_ancestor

    while q.size() > 0:
        path = q.dequeue()
        current = path[-1]
        
        if len(path) == longest_path:
            # If current is smaller than earliest ancestor, update earliest ancestor is current
            if current <= earliest_ancestor:
                longest_path = len(path)
                earliest_ancestor = current
        
        # If path is longer than previously visited path, update earliest ancestor to be current
        if len(path) > longest_path:
            longest_path = len(path)
            earliest_ancestor = current

        neighbors = graph.vertices[current]

        for ancestor in neighbors:
            path_copy = path.copy()
            path_copy.append(ancestor)
            q.enqueue(path_copy)
    
    return earliest_ancestor