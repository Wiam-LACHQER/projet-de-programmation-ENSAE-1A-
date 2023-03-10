from time import perf_counter
from graph import Graph, graph_from_file,representation_graph,open_route,time_counter


data_path = "input/"
file_name = "network.1.in"
file_name2= "routes.1.in"

g = graph_from_file(data_path + file_name)
# print(g)

"""g.add_edge("Paris", "Palaiseau", 4, 20)
print(g) # affichage du graphe
print(g.connected_components())"""



"""print(g.trajets(2,3,21))
print(g)"""
"""print(g.get_path_with_power(2,4,8))"""

# representation_graph(file_name,data_path,2,17,757)

print(time_counter(20,data_path+file_name2))

# g.explore_with_power(2)

# print(open_route(data_path+file_name2))
# print(g.min_power(16,13))
