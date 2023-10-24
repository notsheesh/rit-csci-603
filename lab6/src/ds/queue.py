from ds.linked_node import LinkedNode

class SimpleQueue:
    __slot__ = 'storage', 'id', 'count'
    storage: list 
    count: int
    
    def __init__(self, storage = None):
        self.storage = []
        self.count = 0
    
    def enqueue(self, value):
        self.count += 1
        self.storage.append(value)

    def dequeue(self):
        result = None
        if not self.is_empty():
            self.count -= 1
            result = self.storage[0]
            self.storage = self.storage[1:]
        return result
    
    def get_values(self):
        return self.storage

    def is_empty(self):
        return self.count == 0

    def __str__(self):
        return str([x.get_ticket_number() for x in self.get_values()])
    
class Queue:
    __slot__ = "count", "head", "tail"
    count: int
    head: LinkedNode
    tail: LinkedNode

    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0

    def enqueue(self, value):
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
        assert not self.is_empty() # Make sure list isn't empty 
        dq_node = self.head # Get node at head, to be dqed
        self.head = dq_node.get_link() # head -> first.link == second 
        self.count -= 1
        return dq_node.get_value()
    
    def peek(self):
        return self.head.get_value()

    def is_empty(self):
        # print("self.head == None: {}".format(self.head == None))
        # print("self.capacity == 0: {}".format(self.count == 0))
        return self.head == None

    def __str__(self):
        return "[{}]".format(self.convert_to_str()) 
    
    def get_values(self):
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

def testQueue():
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