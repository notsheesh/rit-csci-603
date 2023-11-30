class Paintball:
    """
    A class representing a paintball object with a unique identifier, location, radius, and type.
    """
    def __init__(self, id, loc, r):
        """
        Initializes a new Paintball instance.

        :param id: A unique identifier for the paintball.
        :type id: str
        :param loc: A tuple representing the (x, y) coordinates of the paintball's location.
        :type loc: tuple
        :param r: The radius of the paintball.
        :type r: float
        """
        self.id = id
        self.loc = loc
        self.r = r
        self.type = "ball"

    def eu_dist(self, point):
        """
        Calculates the Euclidean distance between the paintball and another point.

        :param point: Another point (e.g., a Vertex) to calculate the distance to.
        :type point: object

        :return: The Euclidean distance between the paintball and the specified point.
        :rtype: float
        """
        x1, y1 = self.loc
        x2, y2 = point.loc
        return  ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5

    def will_splash(self, point):
        """
        Checks if the paintball will splash on another point based on distance.

        :param point: Another point (e.g., a Vertex) to check for splashing.
        :type point: object

        :return: True if the paintball will splash on the specified point, False otherwise.
        :rtype: bool
        """
        return self.eu_dist(point) <= self.r

    def __str__(self):
        """
        Returns a string representation of the paintball based on its unique identifier.

        :return: A string representing the paintball's unique identifier.
        :rtype: str
        """
        return self.id