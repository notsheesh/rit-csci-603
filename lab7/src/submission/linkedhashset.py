"""
Lab 7: LinkedHashSet

A Python implementation of a linked hash set, which combines the properties of a set and a hash table.

author: Shreesh Tripathi, st4083
"""
from set import SetType
import sys

from collections.abc import Iterable, Iterator

class ChainNode():
    """
    Represents a node in a doubly linked list for use in a LinkedHashSet.

    Attributes:
    - obj: The object stored in the node.
    - prev: The previous node in the linked list.
    - next: The next node in the linked list.
    - fwd: A forward pointer to the next node with the same hash value.

    Methods:
    - get_object(node): Returns the object stored in a given node.
    - __str__(): Returns a string representation of the node.
    - __repr__(): Returns a detailed string representation of the node.
    """

    def __init__(self, obj, prev=None, next=None, fwd=None):
        """
        Initialize a ChainNode object.

        :param obj: The object to be stored in the node.
        :param prev: The previous node in the linked list.
        :param next: The next node in the linked list.
        :param fwd: The forward node in the linked list (used for chaining in hash collisions).
        """
        self.obj = obj
        self.prev = prev
        self.next = next
        self.fwd = fwd

    def get_object(self, node):
        """
        Get the object stored in a ChainNode.

        :param node: The ChainNode object.

        :return: The object stored in the node, or None if the node is None.
        """
        if node == None:
            return None
        else:
            return node.obj
    
    def __str__(self):
        """
        Return a string representation of the ChainNode.

        :return: A string representation of the ChainNode.
        """
        if self == None: 
            return "None"

        str_str = "[prev:  {}, obj: {}, next: {}, fwd: {}]".format(
            self.get_object(self.prev),
            self.get_object(self),
            self.get_object(self.next),
            self.get_object(self.fwd)
        )
        return str_str
    
    def __repr__(self):
        """
        Return a string representation of the linked list.

        :return: A string representation of the linked list.
        """
        if self == None:
            return "None"
        
        repr_str = "" 
        curr_node: ChainNode = self
        # node1 -> node2 -> node3 -> None 
        while curr_node.fwd != None:
            repr_str += "{" + str(curr_node.obj) + "} -> "
            curr_node = curr_node.fwd
        repr_str += "{" + str(curr_node.obj) + "}"
        return repr_str
        

class LinkedHashSet(SetType, Iterable):

    def __init__(
            self, 
            initial_num_buckets = 100, 
            load_limit = 0.75, 
            hash_function = hash,
            DEBUG = False
            ):
        """
        Initialize a LinkedHashSet object.

        :param initial_num_buckets: The initial number of buckets in the hash table.
        :param load_limit: The load factor limit for rehashing.
        :param hash_function: The hash function to use for indexing objects.
        :param DEBUG: Whether to enable debugging output.
        """
        
        super().__init__()
        # Hash table
        self.initial_num_buckets = initial_num_buckets
        self.number_of_buckets = self.initial_num_buckets 
        self.table = [None] * self.number_of_buckets 
        self.load_limit = load_limit
        self.hash_function = hash_function
        self.DEBUG = DEBUG

        # Linked list 
        self.front = None
        self.back = None

        if self.DEBUG:
            print("> Init LinkedHashSet")
            print(repr(self))
    
    def calculate_load_factor(self):
        """
        Calculate the load factor of the hash table.

        :return: The load factor as a float.
        """
        return self.size / self.number_of_buckets

    def calculate_bucket_index(self, obj, divisor):
        """
        Calculate the bucket index for an object.

        :param obj: The object for which to calculate the bucket index.
        :param divisor: The divisor used to calculate the index.

        :return: The bucket index as an integer.
        """
        hash_value = self.hash_function(obj)
        bucket_index = hash_value % divisor
        return bucket_index

    def add(self, obj):
        """
        Add an object to the LinkedHashSet.

        :param obj: The object to add to the set.

        :return: True if the object was added successfully, False if it already exists in the set.
        """
        if self.DEBUG:
            print("> Attempting to add '{}'".format(obj))
        
        # Skip if duplicate
        if self.contains(obj):
            if self.DEBUG:
                print("> '{}' already exists. No change.".format(obj))
            return False
        
        # Node to be added [obj, prev, next, fwd]
        new_node = ChainNode(obj)

        # Add element to linked list (empty)
        # want: front -> new_node <- back 
        if self.front == None and self.back == None: 
            new_node.next = self.front
            new_node.prev = self.back
            self.front = new_node
            self.back = new_node

        else:
            # want: front -> node1 -> node2 <--> [new_node <- back] -> null
            new_node.prev = self.back # node2 <- new_node
            self.back.next = new_node # node2 -> new_node
            self.back = new_node # node2 -> new_node <- back
        
        # Add element to hash table
        bucket_index = self.calculate_bucket_index(obj, self.number_of_buckets)
        if self.table[bucket_index] == None:
            self.table[bucket_index] = new_node
        
        else: 
            # index: node1 -> node2 -> node3 [obj, fwd = None] -> None
            curr_node: ChainNode = self.table[bucket_index]
            # Grab the last node
            while curr_node.fwd != None:
                curr_node = curr_node.fwd
            new_node.fwd = curr_node.fwd
            curr_node.fwd = new_node
        
        self.size += 1
        if self.DEBUG:
            print("> '{}' added successfully.".format(obj))
            
        # Is rehashing required?
        if self.calculate_load_factor() > self.load_limit:
            if self.DEBUG:
                print(repr(self))
                print("> Load factor ({}) crossed load limit".format(
                    self.calculate_load_factor()
                ))
                print("> Rehashing up")
            self.rehash("up")
        
        return True

    def contains(self, obj):
        """
        Check if the set contains a specific object.

        :param obj: The object to check for in the set.

        :return: True if the object is in the set, False otherwise.
        """
        # Is object the parent of the chain? O(1) case 
        bucket_index = self.calculate_bucket_index(obj, self.number_of_buckets)
        test_node = self.table[bucket_index]
        if test_node != None and obj == test_node.obj:
            return True
        
        # If object at beginning or end of linked list? O(1) case 
        if (
            self.front != None and obj == self.front.obj 
            or
            self.back != None and obj == self.back.obj
        ):
            return True
        
        # Else, O(n) case 
        curr_node = self.front
        # node1 -> node2 -> node3 -> obj -> node4 -> null 
        while curr_node != None: 
            if obj == curr_node.obj:
                return True
            curr_node = curr_node.next

        # Object not found
        return False

    def rehash(self, mode = "up"):
        """
        Rehash the hash table to increase or decrease the number of buckets.

        :param mode: The rehashing mode, either "up" to increase the number of buckets or "down" to decrease it.
        """
        if mode == "up":
            number_of_buckets = self.number_of_buckets * 2
        if mode == "down":
            number_of_buckets = self.number_of_buckets // 2

        rehashedState = LinkedHashSet(
            initial_num_buckets=number_of_buckets, 
            load_limit=self.load_limit,
            hash_function=self.hash_function,
        )

        curr_node = self.front
        while curr_node != None: 
            rehashedState.add(curr_node.obj)
            curr_node = curr_node.next

        # Update LHS
        self.number_of_buckets = rehashedState.number_of_buckets
        self.table = rehashedState.table
        self.initial_num_buckets = rehashedState.initial_num_buckets
        self.load_limit = rehashedState.load_limit
        self.hash_function = rehashedState.hash_function
        self.front = rehashedState.front
        self.back = rehashedState.back

    def remove(self, obj):
        """
        Remove an object from the LinkedHashSet.

        :param obj: The object to remove from the set.

        :return: True if the object was removed successfully, False if it does not exist in the set.
        """
        if self.DEBUG:
            print("> Attempting to remove '{}'".format(obj))

        if not self.contains(obj):
            if self.DEBUG:
                print("> Error. '{}' does not exist in the set.".format(obj))
            return False


        bucket_index = self.calculate_bucket_index(obj, self.number_of_buckets)

        # If obj is parent of the chained link - O(1) case
        test_node = self.table[bucket_index]
        if test_node != None and obj == test_node.obj:
            # bucket: node -> None
            # Remove from hashtable 
            if test_node.fwd == None: 
                self.table[bucket_index] = None    
            else: 
                self.table[bucket_index] = test_node.fwd
            target_node = test_node
        
        # If obj is bw linked list and obj is not chained link parent 
        else:
            # node1 -> node2 -> obj -> node4 -> null
            behind_target_node = self.table[bucket_index]
            while behind_target_node.fwd != None and obj != behind_target_node.fwd.obj:
                behind_target_node = behind_target_node.fwd
            # Remove from hashtable 
            target_node = behind_target_node.fwd
            behind_target_node.fwd = target_node.fwd

        # Update linked list
        # prv -> target -> next
        prev_node = target_node.prev # prev -> target 
        next_node = target_node.next # target -> next
        if prev_node == None:
            # front -> first_node -> second_node
            self.front = next_node 
        else:
            prev_node.next = next_node # prev -> next 
            
        if next_node != None: 
            next_node.prev = prev_node # prev <- next

        self.size -=1 
        if self.DEBUG:
            print("> '{}' removed successfully.".format(obj))

        # Is rehashing required?
        if self.calculate_load_factor() < 1-self.load_limit:
            if self.DEBUG:
                print(repr(self))
                print("> Load factor ({}) dropped below (1 - load_limit) ({})".format(
                    self.calculate_load_factor(), 1-self.load_limit
                ))
                print("> Rehashing down")
            self.rehash("down")

        # Remove complete
        return True
        
    def __len__(self):
        """
        Return the number of elements in the LinkedHashSet.

        :return: The number of elements as an integer.
        """
        return self.size

    def __repr__(self): 
        """
        Return a string representation of the LinkedHashSet.

        :return: A string representation of the LinkedHashSet.
        """
        heading = "String generated\n----------------\n"
        specs = "Capacity: {}, Size: {}, Load Factor: {}, Load Limit: {}".format(
            self.number_of_buckets, self.size, self.calculate_load_factor(), self.load_limit
        )
        space = "    "
        sub_heading = "\n\n" + space + "Hash table\n" + space + "----------\n"

        hashtable = ""
        for i in range(self.number_of_buckets):
            node_obj = repr(self.table[i]).replace("{", "'").replace("}", "'")
            if node_obj != "None":
                node_obj += " -> None"
            hashtable += space + str(i) + ": " + node_obj + "\n"

        if self.DEBUG:
            repr_str = "> " + specs + sub_heading + hashtable
        else:
            repr_str = heading + specs + sub_heading + hashtable

        return repr_str
        
    def __str__(self):
        """
        Return a string representation of the LinkedHashSet.

        :return: A string representation of the LinkedHashSet.
        """
        str_str = "{"
        curr_node = self.front

        if curr_node == None: 
            return "{}"
        else:
            # node1 -> node2 -> node3 -> node4 -> null
            while curr_node.next != None:
                str_str += str(curr_node.obj) + ", "
                curr_node = curr_node.next
            str_str += str(curr_node.obj) + "}"
        return str_str

    def __iter__(self):
        """
        Return an iterator for the LinkedHashSet.

        :return: An iterator for the LinkedHashSet.
        """
        return LinkedHashSet.Iter(self)
    
    class Iter(Iterator):

        def __init__(self, linked_hashset):
            self.curr_node = linked_hashset.front
        
        def __next__(self):
            if self.curr_node != None:
                obj = self.curr_node.obj
                self.curr_node = self.curr_node.next
                return  obj
            else:
                raise StopIteration

if __name__ == "__main__":
    pass