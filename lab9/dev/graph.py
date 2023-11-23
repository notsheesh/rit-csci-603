from vertex import Vertex

class Graph:
    
    slots = ("vertices", "count", "num_cows", "num_balls")

    def __init__(self):
        self.count = 0  
        self.num_cows = 0 
        self.num_balls = 0
        self.vertices = {}

    def add_vertex(self, obj):
        if obj.id not in self.vertices:
            self.vertices[obj.id] = Vertex(obj)
            self.count += 1
            if obj.type == "cow":
                self.num_cows += 1
            elif obj.type == "ball":
                self.num_balls += 1

        return self.vertices[obj.id]

    def get_type(self, id):
        vtx = self.get_vertex(id)
        return vtx.type

    def get_vertex(self, id):
        return self.vertices.get(id, None)

    def __contains__(self, id):
        return id in self.vertices

    def add_edge(self, src, dest, weight = 0):
        if src.id not in self.vertices:
            self.add_vertex(src)

        if dest not in self.vertices: 
            self.add_vertex(dest)

        # srcVertex.neighbors[destVertex] = weight
        self.vertices[src.id].add_neighbor(self.vertices[dest.id], weight)
        
    def __iter__(self):
        return iter(self.vertices.values())

    def stat(self):
        return f"Number of vertices: {self.count}, cows: {self.num_cows}, paint balls: {self.num_balls}"
    
    def find_paths(self, start, end):
        visited = set()
        visited.add(start.id)
        return self.dfs(start, end, visited)


    def dfs(self, current, goal, visited):
        if current.id == goal.id:
            return [goal]
        
        for neighbor in current.get_neighbors():
            if neighbor.id not in visited:
                visited.add(neighbor.id)
                path = self.dfs(neighbor, goal, visited)

                if path != None:
                    path.insert(0, current)
                    return path
        return None
    def __str__(self):
        sep = "----------------------------------------------------"
        graph_str = self.stat() + "\n" + sep + "\n"

        for vx in self:
            graph_str += str(vx) + "\n"

        return graph_str[:-1]
