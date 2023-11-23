class Vertex: 

    slots = ("id", "loc", "type", "neighbors")

    def __init__(self, obj):
        self.id = obj.id
        self.loc = obj.loc
        self.type = obj.type
        self.r = obj.r
        self.neighbors = {}

    def add_neighbor(self, nbr, weight = 0): 
        self.neighbors[nbr] = weight

    def eu_dist(self, point):
        x1, y1 = self.loc
        x2, y2 = point.loc
        return  ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5

    def will_splash(self, point):
        return self.eu_dist(point) <= self.r
    
    def get_neighbors(self):
        return self.neighbors.keys()
    
    # def get_neighbors_str(self):
    #     nbr_str = ''
    #     nbrs = [v.id for v in self.get_neighbors()]
    #     for i in range(len(nbrs)):
    #         nbr_str += f"{nbrs[i]}, "
    #     return nbr_str[:-2]

    def get_weight(self, nbr):
        return self.neighbors[nbr]

    def __str__(self):
        return f"{str(self.id)} neighbors: {[nbr.id for nbr in self.get_neighbors()]}"
