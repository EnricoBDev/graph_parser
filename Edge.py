class Edge:
    def __init__(self, edge_source, edge_target, is_directed, weight):
        self.edge_source = edge_source
        self.edge_target = edge_target
        self.is_directed = is_directed
        self.weight = weight
    
    def get_edge_source(self) -> int:
        return self.edge_source
    
    def get_edge_target(self) -> int:
        return self.edge_target
    
    def get_is_directed(self) -> bool:
        return self.is_directed
    
    def get_weight(self) -> int:
        return self.weight

    def __repr__(self) -> str:
        return "{(" + str(self.edge_source) + " " + str(self.edge_target) + ")" + ", isDirected=" + str(self.is_directed)  + ", weight=" + str(self.weight) + "}"