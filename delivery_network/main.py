from time import perf_counter
from graph import Graph, graph_from_file,representation_graph,open_route,time_counter, kruskal, union_find, min_power2,time_counter2,parents


data_path = "input/"
file_name = "network.1.in"
file_name2= "routes.1.in"

t1_start= perf_counter()
g = graph_from_file(data_path + file_name)
t1_stop = perf_counter()
print(t1_stop-t1_start)
# print(g)

t1_start= perf_counter()
tree=kruskal(g)
t1_stop = perf_counter()
print(t1_stop-t1_start)
"""g.add_edge("Paris", "Palaiseau", 4, 20)
print(g) # affichage du graphe
print(g.connected_components())"""


"""print(g.trajets(2,3,21))
print(g)"""
# print(g.get_path_with_power(2,4,3))

# representation_graph(data_path,4,9,9,file_name)

# print(time_counter(20,data_path+file_name2))

# g.explore_with_power(2)

# print(open_route(data_path+file_name2))
# print(g.min_power(16,13))
# kruskal(g)
# representation_graph(data_path,1,1,757,"tree",tree)

"""t1_start = perf_counter()
print(min_power2(tree,1,7))
t1_stop = perf_counter()
print(t1_stop-t1_start)"""

"""t1_start = perf_counter()
print(g.min_power(11,9))
t1_stop = perf_counter()
print(t1_stop-t1_start)"""

print(time_counter2(15,data_path+file_name2,tree))

"""
Resultat routes2

création du graphe   90.27095479999844
kruskal  499.4082939    
parents  242.1338109999997
la boucle de min-power2(voir time-counter2)   23.310666632217664

Resultat de routes3

400.0265255999984
1339.887115999998
407.8878979000001
999.9366666306742"""