from time import perf_counter
from graph import Graph, graph_from_file,representation_graph,open_route,time_counter, kruskal, union_find, min_power2,time_counter2,parents


data_path = "input/"
file_name = "network.2.in"
file_name2= "routes.2.in"

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
90.27095479999844

499.4082939

242.1338109999997

([37816, 22303, 2992, 2442, 2021, 174, 63, 56, 35, 13, 3, 1, 7, 111, 133, 304, 385, 1065, 5536, 17409, 19930, 25638, 69365, 77493], 97570.0)
([25416, 18608, 2165, 1431, 631, 109, 18, 5, 1, 6, 36, 42, 54, 126, 205, 328, 342, 1258, 1420, 8338, 11491, 55780], 96804.0)
([21116, 3778, 1922, 1583, 1145, 915, 846, 295, 186, 60, 40, 35, 13, 3, 1, 2, 4, 9, 30, 32, 46, 80, 122, 257, 981, 11641, 12109, 14374, 19317], 97746.0)
([56195, 13249, 9988, 1742, 665, 77, 34, 5, 1, 3, 13, 35, 56, 134, 572, 708, 7401], 93594.0)
([39868, 13514, 1618, 1295, 805, 786, 716, 561, 503, 26, 7, 1, 3, 13, 87, 541, 598, 1862, 2075, 2077, 5662, 36558], 89786.0)
([5825, 102, 100, 56, 35, 13, 3, 1, 5, 18, 109, 250, 1455, 1631, 10511, 12169], 93594.0)
([88854, 47567, 43032, 42663, 33553, 10292, 6705, 3023, 216, 102, 100, 56, 35, 13, 3, 1, 6, 36, 42, 54, 72, 436, 1259, 1864, 4944, 62546], 96899.0)
([51203, 37152, 13911, 7737, 7509, 3533, 774, 288, 152, 136, 80, 46, 32, 30, 9, 4, 16, 17, 162, 730, 2255, 22668, 27998, 59584], 97822.0)
([73304, 46214, 31414, 30741, 10299, 393, 193, 70, 24, 9, 4, 16, 151, 237, 568, 804, 813, 1270, 1350, 1689, 2136, 32604, 46073, 47442, 73447], 97746.0)
([28004, 312, 2, 8, 10, 20, 31, 404, 485, 1075, 1157, 1663, 4906], 70043.0)
([74337, 59198, 50793, 42125, 21330, 15778, 3240, 2304, 2017, 574, 139, 42, 36, 6, 1, 5, 310, 341, 537, 13933, 19161], 99341.0)
([1220, 1125, 227, 195, 6, 1, 2, 43, 47, 453, 1668, 2234, 5387, 5588, 30498, 46952], 97499.0)
([35940, 27432, 8570, 1781, 992, 502, 418, 344, 75, 52, 2, 4, 16, 45, 680, 7217, 23154, 33777, 38874, 98391], 97294.0)
([1429, 71, 59, 47, 43, 2, 1, 3, 13, 35, 40, 60, 149, 1083, 3511, 5823, 59890], 99981.0)
([23683, 9715, 8696, 896, 341, 310, 5, 1, 3, 13, 35, 56, 100, 102, 35546, 71102, 74712], 93594.0)

23.310666632217664"""