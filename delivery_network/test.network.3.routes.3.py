from time import perf_counter
from graph import Graph, graph_from_file,representation_graph,open_route,time_counter, kruskal, union_find, min_power2,time_counter2,parents


data_path = "input/"
file_name = "network.2.in"
file_name2= "routes.2.in"

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

Création du graphe:                                         400.0265255999984
Création de l arbre couvrant minimal (kruskal):             1339.887115999998 
définition des parents et des rangs:                        407.8878979000001
le temps moyen pour trouver tous les trajets de routes.2:   999.9366666306742
"""
# les chemins trouvés et les puissances minimales sont également affichés dans le terminal