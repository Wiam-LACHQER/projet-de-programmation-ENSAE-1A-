
from graph import Graph, graph_from_file,representation_graph


data_path = "input/"
file_name = "network.04.in"

g = graph_from_file(data_path + file_name)
print(g)

"""g.add_edge("Paris", "Palaiseau", 4, 20)
print(g) # affichage du graphe
print(g.connected_components())"""



"""print(g.trajets(2,3,21))
print(g)"""
print(g.get_path_with_power(2,4,8))

representation_graph(file_name,data_path,2,4,11)
print(g.get_path_with_power(2,4,14))


"""print(g.min_power(2,4))"""
"""g.explore_with_power(2)"""
