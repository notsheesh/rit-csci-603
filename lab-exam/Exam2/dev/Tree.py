"""
     author: Shreesh Tripathi, st4083
"""
class TreeNode:
     __slots__ = 'val', 'children', 'parent'

     def __init__(self, val, 
                  parent = None # Part A - Shreesh Tripathi
                  ): 
          self.val = val
          self.children = []
          self.parent = parent # Part A - Shreesh Tripathi

     def getStringRep(self): #do not modify
          return self._getStringRep(0)
     
     def _getStringRep(self,depth ): #do not modify
          ret = self.val
          for c in self.children:
               
               ret +="\n"+"    "*depth+"x---"+(c._getStringRep(depth+1))
          return ret
     
     def __str__(self): #do not modify
          return str(self.val)
     
     def __repr__(self): #do not modify
          return str(self.val)
     
     def __eq__(self, other): #do not modify
          if type(self) != type(other):
               return False
          return self.val == other.val

class Tree:
     __slots__ = 'root', 'nodeLookup'

     def __init__(self):  #do not modify
          self.root = None
          self.nodeLookup = dict()

     def getStringRep(self):  #do not modify
          if self.root:
               return self.root.getStringRep()
          return "[empty]"

     def getNodeByValue(self, value):  #do not modify
          return self.nodeLookup[value]

     def addRoot(self, value): #do not modify
          """
          Creates a new node using the value and places it at the root
          :param value: the value of the root
          """
          assert  value not in self.nodeLookup and not self.root 
          assert type(value) == str
          node = TreeNode(value)
          self.nodeLookup[value]=node
          self.root = node

     def addChildTo(self, newChildValue, parentValue):
          """
          Creates a new node using the newChildValue and adds it to the node representing the parentValue
          :param newChildValue: The value of the new child node
          :param parentValue: The value of the intended parent

          """

          assert parentValue in self.nodeLookup and newChildValue not in self.nodeLookup  
          assert type(newChildValue) == str and type(parentValue) == str
          # Part B - Shreesh Tripathi 
          # Node Look Up -> value -> ptrToNode 
          # Attach child -> parent
          ptrParentNode: TreeNode = self.getNodeByValue(parentValue)
          ptrNewChildNode = TreeNode(newChildValue, parent=ptrParentNode)
          # Add child to nodeLookUp
          self.nodeLookup[newChildValue] = ptrNewChildNode
          # Add child -> parent children 
          ptrParentNode.children.append(ptrNewChildNode)

     def getHeight(self, node):
          """ Calculates the height of the tree"""
          if node == None:
               return -1
          else:
               maxNodeHeight = -1
               for child_node in node.children:
                    maxNodeHeight = max(maxNodeHeight, self.getHeight(child_node))
               return 1 + maxNodeHeight

     def getPathToAncestor(self,nodeValue,ancValue ):
          """
           Finds the path (if it exists) between the node specified by nodeValue and the ancestor node specified by ancValue
          :param nodeValue: The value of the node
          :param ancValue: The value of the ancestor node
          :return: A list of nodes representing the path between the node and its ancestor or an empty list if the ancestor node given is not actually an ancestor
          """
          assert nodeValue in self.nodeLookup and ancValue in self.nodeLookup
          assert type(nodeValue) == str and type(ancValue) == str
          
          trace_lst = []
          # Add child
          trace_lst.append(nodeValue)

          # Add all in between 
          ptrNode: TreeNode = self.getNodeByValue(nodeValue)
          while ptrNode.parent != None and ptrNode.val != ancValue:
               ptrNode = ptrNode.parent
               trace_lst.append(ptrNode.val)

          if ancValue not in trace_lst:
               print("[!!!] Ancestor doesn't exist for the given descendent")
               return [nodeValue]
          
          return trace_lst
          

def test():
     t = Tree()
     t.addRoot("thing")
     #add children here
     t.addChildTo("animal","thing")
     
     #add the rest here
     # Part C - Shreesh Tripathi
     # children of animal 
     t.addChildTo("mammal","animal")
     t.addChildTo("fish","animal")

     # children of mammal
     t.addChildTo("dog","mammal")
     t.addChildTo("cat","mammal")
     t.addChildTo("human","mammal")

     # children of fish
     t.addChildTo("tuna","fish")

     t.addChildTo("plant","thing")


     print(t.getStringRep())
#height
     print(t.getHeight(t.root))

     # Extra test cases for height - Shreesh Tripathi
     print("\n\nExtra test cases for height - Shreesh Tripathi")
     t.addChildTo("human-baby","human")
     t.addChildTo("foetus","human-baby")
     print(t.getStringRep())
     print(t.getHeight(t.root))
     
     t.addChildTo("baby","tuna")
     t.addChildTo("egg","baby")
     t.addChildTo("zygot","egg")
     print(t.getStringRep())
     print(t.getHeight(t.root))
     # Extra test cases for height - Shreesh Tripathi

     print("getPathToAncestor('animal','thing') =",t.getPathToAncestor('animal','thing'))

     # Extra test cases for getPathToAncestor() - Shreesh Tripathi
     print("\n\nExtra test cases for getPathToAncestor - Shreesh Tripathi")
     print("getPathToAncestor('dog','mammal') =",t.getPathToAncestor('dog','mammal'))
     print("getPathToAncestor('animal','thing') =",t.getPathToAncestor('animal','thing'))
     print("getPathToAncestor('cat','fish') =",t.getPathToAncestor('cat','fish'))
     print("getPathToAncestor('tuna','plant') =",t.getPathToAncestor('tuna','plant'))
     print("getPathToAncestor('plant','thing') =",t.getPathToAncestor('plant','thing'))
     print("getPathToAncestor('zygot','animal') =",t.getPathToAncestor('zygot','animal'))
     # Extra test cases for getPathToAncestor() - Shreesh Tripathi


if __name__ == '__main__':
     test()
