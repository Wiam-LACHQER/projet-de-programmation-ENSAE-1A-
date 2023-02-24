from graph import Graph, graph_from_file


data_path = "input/"
file_name = "network.01.in"

g = graph_from_file(data_path + file_name)
print(g)

g.add_edge("Paris", "Palaiseau", 4, 20)
print(g) # affichage du graphe

print(g.connected_components_set())