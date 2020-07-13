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

    for pair in ancestors:
        parent = pair[0]
        child = pair[1]
        graph.add_vertex(parent)
        graph.add_vertex(child)
        graph.add_edge(child, parent)
    
    # BFS
    q = Queue()
    q.enqueue([starting_node])

    longest_path = 1
    earliest_ancestor = -1

    while q.size() > 0:
        path = q.dequeue()
        current = path[-1]
        
        if len(path) >= longest_path:
            if current <= earliest_ancestor:
                longest_path = len(path)
                earliest_ancestor = current
        
        if len(path) > longest_path:
            longest_path = len(path)
            earliest_ancestor = current

        neighbors = graph.vertices[current]

        for ancestor in neighbors:
            path_copy = path.copy()
            path_copy.append(ancestor)
            q.enqueue(path_copy)
    
    return earliest_ancestor

# ** ALTERNATE SOLUTION **

# def earliest_ancestor(ancestors, starting_node):
#     ancestor_graph = {}

#     # For each ancestor, create a dictionary identifying it's parent nodes - (Child, Parent)
#     for parent, child in ancestors:
#         if child in ancestor_graph:
#             ancestor_graph[child].add(parent)
#         else:
#             ancestor_graph[child] = set()
#             ancestor_graph[child].add(parent)

#     # If no parent nodes, return -1
#     if starting_node not in ancestor_graph.keys():
#         return -1
    
#     # Else, traverse up the graph until parent has no parent nodes
#     current = starting_node
#     # Smaller parent has equal, or longer, path to ancestors
#     parent = min(ancestor_graph[current])

#     # If parent has parents, continue examining the tree
#     while parent in ancestor_graph.keys():
#         current = parent
#         parent = min(ancestor_graph[current])
    
#     return parent