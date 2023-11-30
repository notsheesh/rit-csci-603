class Vertex: 
    """
    A class representing a vertex in a graph, either a Cow or Paintball object.
    """

    slots = ("id", "loc", "type", "neighbors")

    def __init__(self, obj):
        """
        Initializes a new Vertex instance based on a provided object (Cow or Paintball).

        :param obj: The object representing the vertex (either a Cow or Paintball instance).
        :type obj: Cow or Paintball
        """
        self.id = obj.id
        self.loc = obj.loc
        self.type = obj.type
        self.r = obj.r
        self.neighbors = {}

        if self.type == "cow":
            self.painted_by = []

        if self.type == "ball":
            self.triggered = False

    def add_neighbor(self, nbr, weight = 0): 
        """
        Adds a neighboring vertex with an optional edge weight.

        :param nbr: The neighboring vertex.
        :type nbr: Vertex
        :param weight: The edge weight (default is 0).
        :type weight: int

        :return: None
        """
        self.neighbors[nbr] = weight

    def eu_dist(self, point):
        """
        Calculates the Euclidean distance between the vertex and another point.

        :param point: Another point (e.g., a Vertex) to calculate the distance to.
        :type point: object

        :return: The Euclidean distance between the vertex and the specified point.
        :rtype: float
        """
        x1, y1 = self.loc
        x2, y2 = point.loc
        return  ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5

    def will_splash(self, point):
        """
        Checks if the object will splash on another point based on distance.

        :param point: Another point (e.g., a Vertex) to check for splashing.
        :type point: object

        :return: True if the object will splash on the specified point, False otherwise.
        :rtype: bool
        """
        return self.eu_dist(point) <= self.r
    
    def get_neighbors(self):
        """
        Retrieves a list of neighboring vertices.

        :return: A list of neighboring Vertex objects.
        :rtype: list
        """
        return self.neighbors.keys()
    

    def get_weight(self, nbr):
        """
        Retrieves the edge weight to a specific neighboring vertex.

        :param nbr: The neighboring vertex.
        :type nbr: Vertex

        :return: The edge weight to the specified neighboring vertex.
        :rtype: int
        """
        return self.neighbors[nbr]

    def __str__(self):
        """
        Returns a string representation of the vertex, including its neighbors.

        :return: A string representing the vertex and its neighbors.
        :rtype: str
        """
        return f"{str(self.id)} neighbors: {[nbr.id for nbr in self.get_neighbors()]}"