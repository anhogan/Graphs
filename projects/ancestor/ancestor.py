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
    
    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        return self.vertices[vertex_id]

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

class Stack():
    def __init__(self):
        self.stack = []

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        if self.size() > 0:
            return self.stack.pop()
        else:
            return None

    def size(self):
        return len(self.stack)

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

# CLASS SOLUTION
# def build_graph(ancestors):
#     graph = Graph()

#     for parent, child in ancestors:
#         graph.add_vertex(parent)
#         graph.add_vertex(child)
#         graph.add_edge(child, parent)
    
#     return graph

# def earliest_ancestor(ancestors, starting_node):
#     graph = build_graph(ancestors)

#     s = Stack()
#     s.push([starting_node])

#     visited = set()

#     longest_path = []
#     earliest_ancestor = -1

#     while s.size() > 0:
#         path = s.pop()
#         current = path[-1]

#         if (len(path) > len(longest_path)) or (len(path) == len(longest_path)) and current < earliest_ancestor:
#             longest_path = path
#             earliest_ancestor = longest_path[-1]

#         if current not in visited:
#             visited.add(current)

#             parents = graph.get_neighbors(current)

#             for parent in parents:
#                 new_path = path + [parent]
#                 s.push(new_path)
    
#     return earliest_ancestor