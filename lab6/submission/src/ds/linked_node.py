from typing import Any
class LinkedNode: 
    """
    A class representing a node in a linked list.

    Attributes:
    - value (Any): The value contained in the node.
    - link (LinkedNode): The reference to the next node in the linked list.

    Methods:
    - __init__(self, value, link=None): Initializes a new LinkedNode with the given value and an optional reference to the next node.
    - set_link(self, link): Sets the reference to the next node.
    - get_link(self): Gets the reference to the next node.
    - set_value(self, value): Sets the value of the node.
    - get_value(self): Gets the value of the node.
    - __str__(self): Returns a string representation of the node (the value).

    Example:
    >>> node = LinkedNode(42)
    >>> node.get_value()
    42
    >>> node.get_link()
    None
    """
    __slots__ = "value", "link"
    value: Any
    link: 'LinkedNode'

    def __init__(self, value, link = None):
        self.value = value
        self.link = link
    
    def set_link(self, link):
        """
        Set the reference to the next node in the linked list.

        :param link: The next LinkedNode to link to.
        """
        self.link = link
    
    def get_link(self):
        """
        Get the reference to the next node in the linked list.

        :return: The next LinkedNode in the list.
        """
        return self.link

    def set_value(self, value):
        """
        Set the value contained in the node.

        :param value: The new value to be set.
        """
        self.value = value
    
    def get_value(self):
        """
        Get the value contained in the node.

        :return: The value stored in the node.
        """
        return self.value
    
    def __str__(self):
        """
        Get a string representation of the node (the value).

        :return: A string representation of the value stored in the node.
        """
        return "{}".format(self.get_value())
    
def test():
    pass

def main():
    """
    The main function for execution. If this script is run as the main program, this function is called.
    """
    pass
if __name__ == '__main__':
    main()