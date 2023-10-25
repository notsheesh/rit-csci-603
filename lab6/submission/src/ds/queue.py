from ds.linked_node import LinkedNode


class Queue:
    """
    A queue data structure implemented using linked nodes.

    Attributes:
    - count (int): The number of elements in the queue.
    - head (LinkedNode): The front of the queue.
    - tail (LinkedNode): The end of the queue.

    Methods:
    - __init__(self): Initializes an empty queue.
    - enqueue(self, value): Adds an element to the end of the queue.
    - dequeue(self): Removes and returns the element from the front of the queue.
    - peek(self): Returns the element at the front of the queue without removing it.
    - is_empty(self): Checks if the queue is empty.
    - __str__(self): Returns a string representation of the queue.
    - get_values(self): Returns the elements of the queue as a list.
    - convert_to_str(self): Converts the elements of the queue to a formatted string.

    Example:
    >>> q = Queue()
    >>> q.enqueue(1)
    >>> q.enqueue(2)
    >>> q.get_values()
    [1, 2]
    >>> q.dequeue()
    1
    >>> q.get_values()
    [2]
    """
    __slot__ = "count", "head", "tail"
    count: int
    head: LinkedNode
    tail: LinkedNode

    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0

    def enqueue(self, value):
        """
        Adds an element to the end of the queue.

        :param value: The element to be added to the queue.
        """
        new_node = LinkedNode(value)

        # If queue empty
        if self.is_empty():
            # head -> new_node <- tail 
            self.head = new_node # head -> new_node
            self.tail = new_node # new_node <- tail 
            self.count += 1
            return

        # If queue has elements
        if not self.is_empty():
            # fourth node
            # head -> first -> second -> third <- tail
            self.head = self.head # remains unchanged 
            self.tail.set_link(new_node) # third -> fourth
            self.tail = new_node # ... third -> fourth <- tail 
            self.count += 1
            return

    def dequeue(self):
        """
        Removes and returns the element from the front of the queue.

        :return: The element at the front of the queue.
        """
        assert not self.is_empty() # Make sure list isn't empty 
        dq_node = self.head # Get node at head, to be dqed
        self.head = dq_node.get_link() # head -> first.link == second 
        self.count -= 1
        return dq_node.get_value()
    
    def peek(self):
        """
        Returns the element at the front of the queue without removing it.

        :return: The element at the front of the queue.
        """
        return self.head.get_value()

    def is_empty(self):
        """
        Checks if the queue is empty.

        :return: True if the queue is empty, False otherwise.
        """
        return self.head == None

    def __str__(self):
        """
        Returns a string representation of the queue.

        :return: A string representation of the elements of the queue.
        """
        return "[{}]".format(self.convert_to_str()) 
    
    def get_values(self):
        """
        Returns the elements of the queue as a list.

        :return: A list containing the elements of the queue.
        """
        lst = []
        if self.is_empty():
            return lst
        else: 
            curr = self.head
            # first -> second last element
            while curr != self.tail:
                lst.append(curr.get_value()) 
                curr = curr.get_link() 
            # last element
            lst.append(self.tail.get_value())
            return lst

    def convert_to_str(self):
        """
        Converts the elements of the queue to a formatted string.

        :return: A string representation of the elements in the queue.
        """
        pretty_str = ""
        if self.is_empty():
            return pretty_str
        
        else:
            # curr == head -> first -> second -> third -> fourth <- tail 
            curr = self.head

            # first -> second last element
            while curr != self.tail:
                pretty_str += str(curr.get_value()) + ", "
                curr = curr.get_link() 
            # last element
            pretty_str += str(self.tail.get_value())
            return pretty_str        

class SimpleQueue:
    """
    A simple implementation of a queue using a list.

    Attributes:
    - storage (list): A list to store the elements of the queue.
    - count (int): The number of elements in the queue.

    Methods:
    - __init__(self, storage=None): Initializes an empty queue.
    - enqueue(self, value): Adds an element to the end of the queue.
    - dequeue(self): Removes and returns the element from the front of the queue.
    - get_values(self): Returns the elements of the queue as a list.
    - is_empty(self): Checks if the queue is empty.
    - __str__(self): Returns a string representation of the queue.

    Example:
    >>> sq = SimpleQueue()
    >>> sq.enqueue(1)
    >>> sq.enqueue(2)
    >>> sq.get_values()
    [1, 2]
    >>> sq.dequeue()
    1
    >>> sq.get_values()
    [2]
    """
    __slot__ = 'storage', 'id', 'count'
    storage: list 
    count: int
    
    def __init__(self, storage = None):
        self.storage = []
        self.count = 0
    
    def enqueue(self, value):
        """
        Adds an element to the end of the queue.

        :param value: The element to be added to the queue.
        """
        self.count += 1
        self.storage.append(value)

    def dequeue(self):
        """
        Removes and returns the element from the front of the queue.

        :return: The element at the front of the queue.
        """
        result = None
        if not self.is_empty():
            self.count -= 1
            result = self.storage[0]
            self.storage = self.storage[1:]
        return result
    
    def get_values(self):
        """
        Returns the elements of the queue as a list.

        :return: A list containing the elements of the queue.
        """
        return self.storage

    def is_empty(self):
        """
        Checks if the queue is empty.

        :return: True if the queue is empty, False otherwise.
        """
        return self.count == 0

    def __str__(self):
        """
        Returns a string representation of the queue.

        :return: A string representing the elements of the queue.
        """
        return str([x.get_ticket_number() for x in self.get_values()])
    

def testQueue():
    """
    Function to test the Queue class.
    """
    q = Queue()
    print("\nEnqueuing")
    for i in range(4):
        q.enqueue(i)
        print(q)

    print("\nDequeuing")

    for i in range(4):
        print(q.dequeue(), end = " ")
        print(q)
    print(q)

def testSimpleQueue():
    """
    Function to test the SimpleQueue class.
    """
    sq = SimpleQueue()
    print("\nEnqueuing")
    for i in range(4):
        sq.enqueue(i)
        print(sq.get_values())
    print("\nDequeuing")
    for i in range(5):
        print(sq.dequeue(), end = " ")
        print(sq.get_values())


def main():
    # testSimpleQueue()
    testQueue()

if __name__ == '__main__':
    main()