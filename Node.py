class Node():
    def __init__(self, node_id, str_label, int_label):
        self.node_id = node_id
        self.str_label = str_label
        self.int_label = int_label
    
    def get_int_label(self) -> int:
        return self.int_label

    def __eq__(self, __o: int) -> bool:
        return self.node_id == __o

    def __repr__(self) -> str:
        return "{id=" + str(self.node_id) + " label=" + str(self.str_label) + " int_label="+ str(self.int_label) + "}"