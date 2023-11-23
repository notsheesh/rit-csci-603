class Cow:
    """
    Represents a cow with a unique identifier, location, orientation, and type.

    Attributes:
    - id (str): A unique identifier for the cow.
    - loc (tuple): A tuple representing the (x, y) coordinates of the cow's location.
    - r (int): An integer representing the orientation or rotation of the cow (default is 0).
    - type (str): A string indicating the type of the object (default is "cow").

    Methods:
    - __init__(self, id, loc): Initializes a new Cow instance with the provided identifier and location.
    - __str__(self): Returns a string representation of the cow based on its unique identifier.
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
