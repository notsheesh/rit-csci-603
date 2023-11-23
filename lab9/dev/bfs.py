from graph import Graph
from vertex import Vertex

def bfs(graph, src, dest):
    src = graph.get_vertex(src)
    dest = graph.get_vertex(dest)

    queue = []
    queue.append(src)

    predecessor = {}
    predecessor[src] = None

    while len(queue) > 0:
        current: Vertex = queue.pop(0)

        if current == dest:
            break
        else:
            for neighbor in current.get_neighbors():
                if neighbor not in predecessor:
                    predecessor[neighbor] = current
                    queue.append(neighbor)

    if dest in predecessor:
        path = []
        current = dest
        while current != src:
            path.insert(0, current.id)
            current = predecessor[current]
        path.insert(0, src.id)
    else: 
        path = []

    return path

def main():
    g = Graph()
    # A 
    g.add_edge('A', 'B')
    g.add_edge('A', 'C')
    g.add_edge('A', 'G')

    # B
    g.add_edge('B', 'D')

    # C
    g.add_edge('C', 'F')

    # D
    g.add_edge('D', 'H')

    # E
    g.add_edge('E', 'H')

    # F
    g.add_edge('F', 'E')

    # G
    g.add_edge('G', 'F')

    print(g)

    print(f"BFS: {bfs(g, 'A', 'H')}")


if __name__ == "__main__":
    main()