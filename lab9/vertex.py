class Vertex: 

    slots = ("id", "cnts")

    def __init__(self, id) -> None:
        self.id = id
        self.neighbors = {}

    def add_neighbor(self, nbr, weight = 0): 
        self.neighbors[nbr] = weight
    
    def get_connections(self):
        return self.neighbors.keys()

    def get_weight(self, nbr):
        return self.neighbors[nbr]

    def __str__(self):
        nbr_str = str([nbr.id for nbr in self.get_connections()])
        return "'" + str(self.id) + "'" + " connected to " + nbr_str

def test():
    vA = Vertex("A")
    vB = Vertex("B")
    vC = Vertex("C")
    vD = Vertex("D")

    vA.add_neighbor(vB, 3)
    vA.add_neighbor(vC, 1)
    vB.add_neighbor(vA, 4)
    vB.add_neighbor(vC, 2)
    vC.add_neighbor(vD, 5)

    print("\nTest - String")
    print(vA)
    print(vD)

    print("\nTest - Weight")
    print(f"A -> B weight == 3: {3 == vA.get_weight(vB)}")
    print(f"C -> D weight == 5: {5 == vC.get_weight(vD)}")

    print("\nTest - Connections")
    print(f"B's neighbors: {[nbr.id for nbr in vB.get_connections()]}")
    print(f"D's neighbors: {[nbr.id for nbr in vD.get_connections()]}")


if __name__ == "__main__":
    test()