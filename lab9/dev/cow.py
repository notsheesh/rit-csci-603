class Cow:
    """
    Represents a cow with a unique identifier, location, orientation, and type.
    """

    def __init__(self, id, loc):
        """
        Initializes a new Cow instance.

        :param id: A unique identifier for the cow.
        :type id: str
        :param loc: A tuple representing the (x, y) coordinates of the cow's location.
        :type loc: tuple
        """
        self.id = id
        self.loc = loc
        self.r = 0
        self.type = "cow"

    def __str__(self):
        """
        Returns a string representation of the cow based on its unique identifier.

        :return: A string representing the cow's unique identifier.
        :rtype: str
        """
        return self.id
