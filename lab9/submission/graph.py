from vertex import Vertex

class Graph:
    """
    A class representing a graph used in the simulation of paintball interactions between cows.
    """
    
    slots = ("vertices", "count", "num_cows", "num_balls")

    def __init__(self):
        """
        Initializes a Graph instance with empty vertex information.
        """
        self.count = 0  
        self.num_cows = 0 
        self.num_balls = 0
        self.vertices = {}

    def add_vertex(self, obj):
        """
        Adds a vertex to the graph based on the given object.

        :param obj: The object representing the vertex (either a Cow or Paintball instance).
        :type obj: Cow or Paintball

        :return: The Vertex object corresponding to the added vertex.
        :rtype: Vertex
        """
        if obj.id not in self.vertices:
            self.vertices[obj.id] = Vertex(obj)
            self.count += 1
            if obj.type == "cow":
                self.num_cows += 1
            elif obj.type == "ball":
                self.num_balls += 1

        return self.vertices[obj.id]

    def get_type(self, id):
        """
        Retrieves the type of a vertex based on its ID.

        :param id: The ID of the vertex.
        :type id: str

        :return: The type of the vertex ("cow" or "ball").
        :rtype: str
        """
        vtx = self.get_vertex(id)
        return vtx.type

    def get_vertex(self, id):
        """
        Retrieves a vertex based on its ID.

        :param id: The ID of the vertex.
        :type id: str

        :return: The Vertex object corresponding to the specified ID.
        :rtype: Vertex or None
        """
        return self.vertices.get(id, None)

    def __contains__(self, id):
        """
        Checks if a vertex with the given ID exists in the graph.

        :param id: The ID of the vertex.
        :type id: str

        :return: True if the vertex exists, False otherwise.
        :rtype: bool
        """
        return id in self.vertices

    def add_edge(self, src, dest, weight = 0):
        """
        Adds an edge between source and destination vertices.

        :param src: The source vertex.
        :type src: Vertex
        :param dest: The destination vertex.
        :type dest: Vertex
        :param weight: The weight of the edge (default is 0).
        :type weight: int

        :return: None
        """
        if src.id not in self.vertices:
            self.add_vertex(src)

        if dest not in self.vertices: 
            self.add_vertex(dest)

        # srcVertex.neighbors[destVertex] = weight
        self.vertices[src.id].add_neighbor(self.vertices[dest.id], weight)
        
    def __iter__(self):
        """
        Allows iteration over the vertices in the graph.

        :return: An iterator over the Vertex objects in the graph.
        :rtype: iter
        """
        return iter(self.vertices.values())

    def stat(self):
        """
        Returns a string containing statistics about the graph (number of vertices, cows, and paintballs).

        :return: A string with graph statistics.
        :rtype: str
        """
        return f"Number of vertices: {self.count}, cows: {self.num_cows}, paint balls: {self.num_balls}"
    
    def find_paths(self, start, end):
        """
        Finds paths from the start vertex to the end vertex using depth-first search.

        :param start: The starting vertex.
        :type start: Vertex
        :param end: The ending vertex.
        :type end: Vertex

        :return: A list of vertices representing a path from start to end.
        :rtype: list
        """
        if start == None or end == None: 
            return []
        
        visited = set()
        visited.add(start.id)
        return self.dfs(start, end, visited)


    def dfs(self, current, goal, visited):
        """
        Performs depth-first search to find paths between vertices.

        :param current: The current vertex being explored.
        :type current: Vertex
        :param goal: The goal vertex to reach.
        :type goal: Vertex
        :param visited: A set of visited vertices.
        :type visited: set

        :return: A list of vertices representing a path from current to goal.
        :rtype: list
        """
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
        """
        Returns a string representation of the graph, including statistics and vertex information.

        :return: A string representation of the graph.
        :rtype: str
        """
        sep = "----------------------------------------------------"
        graph_str = self.stat() + "\n" + sep + "\n"

        for vx in self:
            graph_str += str(vx) + "\n"

        return graph_str[:-1]
