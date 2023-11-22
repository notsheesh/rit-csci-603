from vertex import Vertex

class Graph:
    
    slots = ("vertices", "count")

    def __init__(self):
        self.count = 0 
        self.vertices = {}

    def add_vertex(self, id):
        if id not in self.vertices:
            self.vertices[id] = Vertex(id)
            self.count += 1
        return self.vertices[id]

    def get_vertex(self, id):
        return self.vertices.get(id, None)

    def __contains__(self, id):
        return id in self.vertices

    def add_edge(self, src, dest, weight = 0):
        if src not in self.vertices:
            self.add_vertex(src)

        if dest not in self.vertices: 
            self.add_vertex(dest)

        # srcVertex.neighbors[destVertex] = weight
        self.vertices[src].add_neighbor(self.vertices[dest], weight)
    
    def get_vertices(self):
        return [v.id for v in self]
    
    def __iter__(self):
        return iter(self.vertices.values())

def test():
    STATES = {
        'CT': ('MA', 'RI'),
        'MA': ('CT', 'NH', 'RI', 'VT'),
        'ME': ('NH', ),
        'NH': ('MA', 'ME', 'VT'),
        'RI': ('CT', 'MA'),
        'VT': ('MA', 'NH') 
    }

    northeast = Graph()
    for state, neighbors in STATES.items():
        for neighbor in neighbors:
            northeast.add_edge(state, neighbor)

    print("Graph: ")
    for state in northeast:
        print(state)

    print(f"\nStates: {northeast.get_vertices()}")

    print()

    print(f"'MA' in northeast (True)?: {'MA' in northeast}")
    print(f"'ZE' in northeast (False)?: {'ZE' in northeast}")

    print()

    print(f"'MA' Vertex: {northeast.get_vertex('MA')}")

if __name__ == "__main__":
    test()
