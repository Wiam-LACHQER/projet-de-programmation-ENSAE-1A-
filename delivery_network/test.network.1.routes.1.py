from time import perf_counter
from graph import Graph, graph_from_file,representation_graph,open_route,time_counter, kruskal, union_find, min_power2,time_counter2,parents


data_path = "input/"
file_name = "network.1.in"
file_name2= "routes.1.in"


g = graph_from_file(data_path + file_name)
tree=kruskal(g)
representation_graph(data_path,1,1,757,"tree",tree)
print("Le temps nécessaire pour trouver tous les trajets de routes.1 par min_power:  ",time_counter2(15,data_path+file_name2,tree))
print("Le temps nécessaire pour trouver tous les trajets de routes.1 par min_power2:  ",time_counter(15,data_path+file_name2))

