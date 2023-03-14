from time import perf_counter
from graph import Graph, graph_from_file,representation_graph,open_route,time_counter, kruskal, union_find, min_power2,time_counter2,parents


data_path = "input/"
file_name = "network.3.in"
file_name2= "routes.3.in"

t1_start= perf_counter()
g = graph_from_file(data_path + file_name)
t1_stop = perf_counter()
print(t1_stop-t1_start)

t1_start= perf_counter()
tree=kruskal(g)
t1_stop = perf_counter()
print(t1_stop-t1_start)

print(time_counter2(15,data_path+file_name2,tree))

""" 
Résultats obtenus

Création du graphe:                                         240.9951740999968
Création de l arbre couvrant minimal (kruskal):             1005.7318303999928
définition des parents et des rangs:                        342.6782616000128
le temps moyen pour trouver tous les trajets de routes.3:   76.56333327759057
"""
# le fichier routes.3.out est également généré