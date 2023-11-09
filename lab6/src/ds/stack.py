from ds.linked_node import LinkedNode

class SimpleStack: 
    __slot__ = 'storage', 'top'
    storage = None
    top = None

    def __init__(self, storage = None):
        self.storage = []

    def push(self, value):
        self.storage.append(value)

    def pop(self):
        result = None
        if len(self.storage) > 0:
            result = self.peek()
            self.storage = self.storage[:-1]
        return result

    def peek(self):
        result = None
        if len(self.storage) > 0:
            result = self.storage[-1]
        return result
    
    def get_values(self):
        return self.storage
    
class Stack:
    __slot__ = "tos"
    tos: 'LinkedNode' # top of the stack

    def __init__(self):
        self.tos = None
    
    def push(self, value):
        new_node = LinkedNode(value, None)

        # If stack empty
        if self.is_empty():
            # before: tos -> None
            # after: tos -> new_node -> None
            self.tos = new_node
            return new_node

        if not self.is_empty():
            # before: tos -> second -> first 
            new_node.set_link(self.tos) # new_node -> tos == third
            # after: tos -> new_node -> third -> second -> first
            self.tos = new_node 
            return new_node
    
    def pop(self):
        assert not self.is_empty()
        # tos -> A -> B -> C 
        # pop_node = tos == A 
        pop_node = self.tos
        # tos = A.link == B 
        # tos -> B -> C 
        self.tos = pop_node.get_link()
        return pop_node.get_value()

    def peek(self):
        return self.tos.get_value()
    
    def __str__(self):
        return "[{}]".format(self.convert_to_str())
    
    def convert_to_str(self):
        pretty_str = ""
        

        curr = self.tos
        while curr != None:
            
            pretty_str += "{}, ".format(curr.get_value())
            curr = curr.get_link()

        return pretty_str[:-2]
        
    def is_empty(self):
        return self.tos == None
    
def testStack():
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