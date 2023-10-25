from ds.linked_node import LinkedNode

class Stack:
    """
    A stack data structure implemented using linked nodes.

    Attributes:
    - tos (LinkedNode): The top of the stack.

    Methods:
    - __init__(self): Initializes an empty stack.
    - push(self, value): Pushes an element onto the stack.
    - pop(self): Pops and returns the element from the top of the stack.
    - peek(self): Returns the element at the top of the stack without removing it.
    - is_empty(self): Checks if the stack is empty.
    - __str__(self): Returns a string representation of the stack.
    - convert_to_str(self): Converts the elements of the stack to a formatted string.

    Example:
    >>> stack = Stack()
    >>> stack.push(1)
    >>> stack.push(2)
    >>> stack.get_values()
    [1, 2]
    >>> stack.pop()
    2
    >>> stack.get_values()
    [1]
    """
    __slot__ = "tos"
    tos: 'LinkedNode' # top of the stack

    def __init__(self):
        self.tos = None
    
    def push(self, value):
        """
        Pushes an element onto the stack.

        :param value: The element to be pushed onto the stack.
        :return: The LinkedNode that was pushed onto the stack.
        """
        new_node = LinkedNode(value, None)

        # If stack empty
        if self.is_empty():
            # before: tos -> None
            # after: tos -> new_node -> None
            self.tos = new_node
            return new_node

        if not self.is_empty():
            # before: tos -> third -> second -> first 
            new_node.set_link(self.tos) # new_node -> tos == third
            self.tos = new_node # tos -> new_node -> third -> second -> first
            return new_node
    
    def pop(self):
        """
        Pops and returns the element from the top of the stack.

        :return: The element at the top of the stack.
        """
        assert not self.is_empty()
        # tos -> A -> B -> C 
        # pop_node = tos == A 
        pop_node = self.tos
        # tos = A.link == B 
        # tos -> B -> C 
        self.tos = pop_node.get_link()
        return pop_node.get_value()

    def peek(self):
        """
        Returns the element at the top of the stack without removing it.

        :return: The element at the top of the stack.
        """
        return self.tos.get_value()
    
    def __str__(self):
        """
        Returns a string representation of the stack.

        :return: A string representation of the elements of the stack.
        """
        return "[{}]".format(self.convert_to_str())
    
    def convert_to_str(self):
        """
        Converts the elements of the stack to a formatted string.

        :return: A string representation of the elements in the stack.
        """
        pretty_str = ""
        

        curr = self.tos
        while curr != None:
            
            pretty_str += "{}, ".format(curr.get_value())
            curr = curr.get_link()

        return pretty_str[:-2]
        
    def is_empty(self):
        """
        Checks if the stack is empty.

        :return: True if the stack is empty, False otherwise.
        """
        return self.tos == None
    

class SimpleStack: 
    """
    A simple implementation of a stack using a list.

    Attributes:
    - storage (list): A list to store the elements of the stack.

    Methods:
    - __init__(self, storage=None): Initializes an empty stack.
    - push(self, value): Pushes an element onto the stack.
    - pop(self): Pops and returns the element from the top of the stack.
    - peek(self): Returns the element at the top of the stack without removing it.
    - get_values(self): Returns the elements of the stack as a list.

    Example:
    >>> stack = SimpleStack()
    >>> stack.push(1)
    >>> stack.push(2)
    >>> stack.get_values()
    [1, 2]
    >>> stack.pop()
    2
    >>> stack.get_values()
    [1]
    """
    __slot__ = 'storage', 'top'
    storage = None
    top = None

    def __init__(self, storage = None):
        self.storage = []

    def push(self, value):
        """
        Pushes an element onto the stack.

        :param value: The element to be pushed onto the stack.
        """
        self.storage.append(value)

    def pop(self):
        """
        Pops and returns the element from the top of the stack.

        :return: The element at the top of the stack.
        """
        result = None
        if len(self.storage) > 0:
            result = self.peek()
            self.storage = self.storage[:-1]
        return result

    def peek(self):
        """
        Returns the element at the top of the stack without removing it.

        :return: The element at the top of the stack.
        """
        result = None
        if len(self.storage) > 0:
            result = self.storage[-1]
        return result
    
    def get_values(self):
        """
        Returns the elements of the stack as a list.

        :return: A list containing the elements of the stack.
        """
        return self.storage
    
def testStack():
    """
    Function to test the Stack class.
    """
    s = Stack()
    print("Pushing")
    for i in range(4):
        print(i, end=' -> ')
        print(s, end=' => ')
        s.push(i)
        print(s)
    
    print()
    print("Popping")
    for i in range(4):
        print(s.peek(), end=' <- ')
        print(s, end=' => ')
        s.pop()
        print(s)
        

def main():
    testStack()

if __name__ == '__main__':
    main()