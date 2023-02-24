from graph import Graph, graph_from_file


data_path = "projet-de-programmation-ENSAE-1A-/input/"
file_name = "network.01.in"

g = graph_from_file(data_path + file_name)
print(g)

g.add_edge("Paris", "Palaiseau", 4, 20)
print(g) # affichage du graphe
print(g.connected_components_set())


print(g.trajets(4,6,3))
g.get_path_with_power(4,6,3)