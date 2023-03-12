from time import perf_counter
from graph import Graph, graph_from_file,representation_graph,open_route,time_counter, kruskal, union_find, min_power2


data_path = "input/"
file_name = "network.2.in"
file_name2= "routes.1.in"

t1_start= perf_counter()
g = graph_from_file(data_path + file_name)
t1_stop = perf_counter()
print(t1_stop-t1_start)
# print(g)

"""g.add_edge("Paris", "Palaiseau", 4, 20)
print(g) # affichage du graphe
print(g.connected_components())"""



"""print(g.trajets(2,3,21))
print(g)"""
"""print(g.get_path_with_power(2,4,8))"""

# representation_graph(data_path,1,1,50,file_name)

# print(time_counter(20,data_path+file_name2))

# g.explore_with_power(2)

# print(open_route(data_path+file_name2))
# print(g.min_power(16,13))
# print(kruskal(g))
# representation_graph(data_path,1,1,757,"tree",kruskal(g))

"""t1_start = perf_counter()
print(min_power2(kruskal(g),3,17))
t1_stop = perf_counter()
print(t1_stop-t1_start)"""

t1_start = perf_counter()
print(g.min_power(3,17))
t1_stop = perf_counter()
print(t1_stop-t1_start)
