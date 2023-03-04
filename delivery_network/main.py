"""from projet-de-programmation-ENSAE-1A-delivery_network.graph import representation_graph"""
from graph import Graph, graph_from_file,representation_graph


data_path = "projet-de-programmation-ENSAE-1A-/input/"
file_name = "network.03.in"

g = graph_from_file(data_path + file_name)
print(g)

"""g.add_edge("Paris", "Palaiseau", 4, 20)
print(g) # affichage du graphe
print(g.connected_components())"""



"""print(g.trajets(2,3,21))
print(g)"""
print(g.get_path_with_power(2,4,8))
representation_graph(file_name,data_path,1,4,11)
"""print(g.get_path_with_power(5,4,8))"""
print(g.min_power(2,4))
"""g.explore_with_power(2)"""
