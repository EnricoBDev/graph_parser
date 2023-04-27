from bs4 import BeautifulSoup
import numpy as np

from Edge import Edge
from Node import Node

filename = input("Inserisci il nome del file:")

with open(filename) as xml_file:
    soup = BeautifulSoup(xml_file, "xml")

def find_node_list() -> list:
    node_element_list = soup.find_all("section", {"name": "node"})
    node_list = list()

    # get id and label from each node
    for i in node_element_list:
        node_id = int(i.find("attribute", {"key": "id", "type": "int"}).get_text())
        str_node_label = i.find("attribute", {"key": "label", "type": "String"}).get_text()
        int_node_label = int(str_node_label[1:])

        single_node = Node(node_id = node_id, str_label = str_node_label, int_label = int_node_label)
        node_list.append(single_node)

    return node_list

def find_edge_id_list() -> list:
    edge_element_list = soup.findAll("section", {"name": "edge"})
    edge_list = list()

    # used later when creating matrix
    edge_is_directed = False
    edge_weight = -1

    for i in edge_element_list:
        # get source and target from each edge
        edge_source = int(i.find("attribute", {"key": "source", "type": "int"}).get_text())
        edge_target = int(i.find("attribute", {"key": "target", "type": "int"}).get_text())


        # finds graphic arrow to check if edge is directed
        if(i.find("section", {"name": "graphics"}) \
           .find("attribute", {"key": "targetArrow", "type": "String"})):
            edge_is_directed = True

        # finds graphic label to check if edge is weighted
        if(i.find("section", {"name": "LabelGraphics"})):
            edge_weight = int(i.find("section", {"name": "LabelGraphics"}) \
                .find("attribute", {"key": "text", "type": "String"}) \
                .get_text())
            
        edge = Edge(
            edge_source = edge_source,
            edge_target = edge_target,
            is_directed = edge_is_directed,
            weight = edge_weight)
        edge_list.append(edge)

        # used later when creating matrix
        edge_is_directed = False
        edge_weight = -1
    return edge_list

# get parsed data
edge_list = find_edge_id_list()
node_list = find_node_list()

# create empty matrix
nodes_number = len(find_node_list())
adj_matrix = np.zeros((nodes_number, nodes_number), dtype=int)


# populate the matrix
for edge in edge_list:
    source = edge.get_edge_source()
    target = edge.get_edge_target()
    weight = edge.get_weight()
    
    for node in node_list:
        if(source == node):
            source = node.get_int_label() - 1 # -1 because arrays indexes start at 0
            break
    for node in node_list:
        if(target == node):
            target = node.get_int_label() - 1 # -1 because arrays indexes start at 0
            break

    if(edge.get_weight() != -1):
        adj_matrix[source][target] = weight
        if(not edge.get_is_directed()):
            adj_matrix[target][source] = weight
    else:
        adj_matrix[source][target] = 1
        if(not edge.get_is_directed()):
            adj_matrix[target][source] = 1

# write to file
with open ("output.txt", "w") as output_file:
    output_file.write("# nodes number:\n")
    output_file.write(str(nodes_number))
    output_file.write("\n")
    output_file.write("# matrix:\n")
    for i in range(0, len(adj_matrix)):
        for j in range(0, len(adj_matrix)):
            output_file.write(str(adj_matrix[i,j]) + " ")
        output_file.write("\n")
