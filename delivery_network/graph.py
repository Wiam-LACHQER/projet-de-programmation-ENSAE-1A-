from time import perf_counter
import graphviz as gv
class Graph:
    """
    A class representing graphs as adjacency lists and implementing various algorithms on the graphs. Graphs in the class are not oriented. 
    Attributes: 
    -----------
    nodes: NodeType
        A list of nodes. Nodes can be of any immutable type, e.g., integer, float, or string.
        We will usually use a list of integers 1, ..., n.
    graph: dict
        A dictionnary that contains the adjacency list of each node in the form
        graph[node] = [(neighbor1, p1, d1), (neighbor1, p1, d1), ...]
        where p1 is the minimal power on the edge (node, neighbor1) and d1 is the distance on the edge
    nb_nodes: int
        The number of nodes.
    nb_edges: int
        The number of edges. 
    """

    def __init__(self, nodes=[]):
        """
        Initializes the graph with a set of nodes, and no edges. 
        Parameters: 
        -----------
        nodes: list, optional
            A list of nodes. Default is empty.
        """
        self.nodes = nodes
        self.graph = dict([(n, []) for n in nodes])
        self.nb_nodes = len(nodes)
        self.nb_edges = 0
    

    def __str__(self):
        """Prints the graph as a list of neighbors for each node (one per line)"""
        if not self.graph:
            output = "The graph is empty"            
        else:
            output = f"The graph has {self.nb_nodes} nodes and {self.nb_edges} edges.\n"
            for source, destination in self.graph.items():
                output += f"{source}-->{destination}\n"
        return output
    
    def add_edge(self, node1, node2, power_min, dist=1):
        """
        Adds an edge to the graph. Graphs are not oriented, hence an edge is added to the adjacency list of both end nodes. 

        Parameters: 
        -----------
        node1: NodeType
            First end (node) of the edge
        node2: NodeType
            Second end (node) of the edge
        power_min: numeric (int or float)
            Minimum power on this edge
        dist: numeric (int or float), optional
            Distance between node1 and node2 on the edge. Default is 1.
        """
        self.nb_edges += 1
        if node1 not in self.nodes and node2 in self.nodes:
              self.nodes.append(node1)
              self.graph[node2]+=[(node1,power_min,dist)]
              self.graph[node1]=[(node2,power_min,dist)]
              self.nb_nodes +=1
        elif node2 not in self.nodes and node1 in self.nodes:
              self.nodes.append(node2)
              self.graph[node1]+=[(node2,power_min,dist)]
              self.graph[node2]=[(node1,power_min,dist)]
              self.nb_nodes +=1
        elif node2 not in self.nodes and node1 not in self.nodes:
              self.nodes.append(node1)
              self.nodes.append(node2)
              self.graph[node2]=[(node1,power_min,dist)]
              self.graph[node1]=[(node2,power_min,dist)]
              self.nb_nodes +=2
        else:
              self.graph[node1]+=[(node2,power_min,dist)]
              self.graph[node2]+=[(node1,power_min,dist)] 
        return(self.graph)
     
    """def trajets(self,src,dest,power):
        for compenent in self.connected_components():
            if src in compenent:
                if dest not in compenent:
                    return None        
        if src==dest:
            return [[src]]           
        trajets_possibles=[]
        for neighbor in self.graph[src]:
            p=neighbor[1]
            power=power-p
            print(power)
            print(neighbor[0])
            print(self.graph[neighbor[0]])
            print((src,neighbor[1],neighbor[2]))
            if (src,neighbor[1],neighbor[2]) in self.graph[neighbor[0]]:
                self.graph[neighbor[0]].remove((src,neighbor[1],neighbor[2]))           
            trajet=self.trajets(neighbor[0], dest, power)
            if type(trajet) != "NoneType":              
                for t in trajet:
                    trajets_possibles.append([src]+t)
                    print(trajets_possibles)
        return trajets_possibles"""

    
    def get_path_with_power(self, src, dest, power, visited=[]):
        """Cette fonction est récursive
        
        Parameters:
        ----------
        src: (source) début du chemin
        dest:(destination) fin du chemin
        power: puissance du camion, elle détermine si il peut faire le trajet ou non
        visited: liste des sommets visités dans un chemin donné
        
        idée:
        -----
        Si src et dest ne sont pas dans la même composante connectée, ou si power<0: le trajet est infaisable.
        On visite un voisin de source, on le marque visité, puis on cherche à atteindre la destination à partir de ce voisin
        tout en mettant à jour la valeur de power, si c est impossible (power insuffisante ou trajet impossible sans passer 
        par la source), on passe à un autre voisin de source.
        """
        """La complexité est O(nb-nodes)"""
        for compenent in self.connected_components():
            if src in compenent:
                if dest not in compenent:
                    return None
        if src==dest:
            return [src]           
        visited.append(src)
        for neighbor in self.graph[src]:
            if neighbor[0] not in visited:
                if power>=neighbor[1]:   
                    trajet=self.get_path_with_power(neighbor[0],dest,power,visited)
                    if trajet!=None:
                        trajet=[src]+trajet
                        return trajet
                    else:
                        visited.remove(neighbor[0])

  

    
    def explorer(self,node,compenent=[]):
        """La fonction explorer permet de récupérer la composante de graphe associée au noeud fourni en parametre"""
        compenent.append(node)
        for neighbor in self.graph[node]:
            if neighbor[0] not in compenent:
                compenent=self.explorer(neighbor[0],compenent)
        return compenent
    
   

    def connected_components(self):
        """Cette fonction permet de récupérer une liste de listes, chacune représente une composante du graphe"""
        nodes1=self.nodes
        compenents=[]
        while nodes1!=[]:
            compenent=self.explorer(nodes1[0],[])
            for elem in compenent:
                nodes1.remove(elem) 
            compenents.append(compenent)
        return compenents


    def connected_components_set(self):
        """
        The result should be a set of frozensets (one per component), 
        For instance, for network01.in: {frozenset({1, 2, 3}), frozenset({4, 5, 6, 7})}
        """
        return set(map(frozenset,self.connected_components()))
    
   
    def explore_with_power(self,node,compenent=[],power=0):
        """cette fonction fait un parcours en profondeur en sommant les puissances des chemins"""
        compenent.append(node)       
        for neighbor in self.graph[node]:
            if neighbor[0] not in compenent:
                (compenent,power)=self.explore_with_power(neighbor[0],compenent,max(power,neighbor[1]))
        return (compenent,power)
    
    
    def min_power(self, src, dest):
        """
        Should return path, min_power. 
        """
        power_max=self.explore_with_power(src,[],0)[1]
        power_min=0
        while power_max > 1+power_min :
            power=(power_max+power_min)//2   
            condition=self.get_path_with_power(src,dest,power,[])
            if condition==None:
                power_min=power
            else:
                power_max=power   
        path=self.get_path_with_power(src,dest,power_max,[])
        return (path,power_max)
   
    def edges(self):
        edges=[]
        keys=self.graph.keys()
        for key in keys:
            neighbors=self.graph[key]
            for neighbor in neighbors:
                if (neighbor[0],key,neighbor[1],neighbor[2]) not in edges:
                    edges.append((key,neighbor[0],neighbor[1],neighbor[2]))
        return edges


def graph_from_file(filename):
    """
    Reads a text file and returns the graph as an object of the Graph class.

    The file should have the following format: 
        The first line of the file is 'n m'
        The next m lines have 'node1 node2 power_min dist' or 'node1 node2 power_min' (if dist is missing, it will be set to 1 by default)
        The nodes (node1, node2) should be named 1..n
        All values are integers.

    Parameters: 
    -----------
    filename: str
        The name of the file

    Outputs: 
    -----------
    G: Graph
        An object of the class Graph with the graph from file_name.
    """

    fichier = open (filename, "r")
    f=fichier.read()
    graph=Graph([]) 
    """Lignes est la liste des lignes du fichier"""
    Lignes=f.split("\n")
    """Entiers est une liste de listes des elements de chaque ligne"""
    Entiers=[]
    for elem in Lignes: 
        if elem !="":
            T = elem.split(" ")
            Entiers.append(T)
    nb_nodes = int(Entiers[0][0])  
    for i in range(1,len(Entiers)):
        node1=int(Entiers[i][0])
        node2=int(Entiers[i][1])
        power_min=float(Entiers[i][2])
        dist=1
        if len(Entiers[i])==4:
            dist=float(Entiers[i][3])
        graph.add_edge(node1, node2, power_min, dist)
    """Probleme des points isolés, comme dans network.02.in"""
    graph.nodes=[i for i in range(1,nb_nodes+1)]
    for j in graph.nodes:
        if j not in graph.graph.keys():
            graph.graph[j]=[]

    fichier.close()
    return graph


def representation_graph(datapath,src,dest,power,filename="tree",g=Graph([])):
    if filename!="tree":
        g=graph_from_file(datapath+filename)
    dot = gv.Graph(filename,format='png')
    keys=g.graph.keys()
    edges=[]
    path=g.get_path_with_power(src, dest, power,[])
    for key in keys:
        if key in path:
            dot.node(str(key), color= "red", style= 'filled')
        else:
            dot.node(str(key))
        neighbors=g.graph[key]
        for neighbor in neighbors:
            if (str(neighbor[0]),str(key)) not in edges:
                dot.edge(str(key), str(neighbor[0]),label=str(neighbor[1]))
                edges.append((str(key), str(neighbor[0])))
    dot.view()
 
def open_route(filename):
    trajets=[]
    route = open (filename, "r")
    f=route.read()
    Lignes=f.split("\n")
    for i in range(1,int(Lignes[0])+1): 
        if Lignes[i] !="":
            trajet = Lignes[i].split(" ")
            trajet[0]=int(trajet[0])
            trajet[1]=int(trajet[1])
            trajet[2]=float(trajet[2])
            trajets.append(trajet)
    L=filename.split(".")
    numero=L[1]
    return (trajets,numero,int(Lignes[0]))


def time_counter(number,filename):
    numero=open_route(filename)[1]
    filenamenet="input/network."+numero+".in"
    g=graph_from_file(filenamenet)
    trajets=open_route(filename)[0]
    t1_start = perf_counter()
    for i in range (number):
        src=trajets[i][0]
        dest=trajets[i][1]
        print(g.min_power(src, dest))
    t1_stop = perf_counter()
    mean=(t1_stop-t1_start)/number
    lignes=open_route(filename)[2]
    return(mean*lignes)


class union_find:
    def __init__(self):
        self.parent={}
        self.rang={}
    def __str__(self):
        """Prints the graph as a list of neighbors for each node (one per line)"""       
        output = " "
        for source, destination in self.parent.items():
            output += f"{source}-->{destination}\n"
        for elem, rang in self.rang.items():
            output += f"{elem}-->{rang}\n"
        return (output)
    def MakeSet(self,x):
       self.parent[x]=x
       self.rang[x]=0
    def Union(self,x,y):
        xRacine=self.Find(x)
        yRacine=self.Find(y)
        if xRacine!=yRacine:
            if self.rang[xRacine]<self.rang[yRacine]:
                self.parent[xRacine]=yRacine
            else:   
                self.parent[yRacine]=xRacine
            if self.rang[xRacine]==self.rang[yRacine]:
                self.rang[xRacine]= self.rang[xRacine] + 1
    def Find(self,x):
        if self.parent[x]!=x:
            self.parent[x]=self.Find(self.parent[x])
        return(self.parent[x])

def kruskal(g=Graph([])):
    tree=Graph([])
    edges_sort=sorted(g.edges(), key=lambda edge: edge[2])
    classes=union_find()
    no=g.nodes
    for node in no:
        classes.MakeSet(node)
    for edge in edges_sort:
        if classes.Find(edge[0])!=classes.Find(edge[1]):
            tree.add_edge(edge[0], edge[1], edge[2], edge[3])
            classes.Union(edge[0],edge[1])
    return tree

def parents(tree,racine):
    """Cette fonction définit les relations pere/fils ainsi que les rangs des noeuds dans un arbre, un parcours en largeur"""
    parent={}
    rang={}
    parent[racine]=(racine,0)
    rang[racine]=0
    visited=[]
    file=[]
    file.append(racine)
    visited.append(racine)
    while file!=[]:
        s=file.pop(0)
        neighbors=tree.graph[s]
        for neighbor in neighbors:
            if neighbor[0] not in visited:
                parent[neighbor[0]]=(s,neighbor[1])
                rang[neighbor[0]]=rang[s]+1
                file.append(neighbor[0])
                visited.append(neighbor[0])
    return(parent,rang)

def min_power2(src,dest,parent,rang):
    path0=[]
    path1=[]
    power=0
    while src!=dest :
        p1=parent[dest]
        p0=parent[src]
        if rang[src]>rang[dest]:
            path0.append(src)
            src=p0[0]
        elif rang[src]<rang[dest]:
            path1=[dest]+path1
            dest=p1[0]
        else:           
            path0.append(src)
            path1=[dest]+path1
            dest=p1[0]
            src=p0[0]
        power0=p0[1]
        power1=p1[1]       
        if power<power1 or power<power0:
            power=max(power1,power0)      
    return (path0+[src]+path1,power)  

def time_counter2(number,filename,tree=[]):
    """Cette fonction extrait les informations du fichier routes.x.in, elle définit les relations pere/fils ainsi que les
    rangs des noeuds par la fonction parents, elle affiche le temps nécessaire pour exécuter parents.
    Enfin, elle exécute min-power2 pour les number premieres lignes de routes.x.in, calcule la moyenne et la multiplie par le 
    nombre de lignes, et affiche le résultat.
    """
    trajets=open_route(filename)[0]
    myFile = open(filename[6:15]+"out", "w")
    
    t0_start = perf_counter()
    par,rang=parents(tree,3)
    t0_stop = perf_counter()   
    print(t0_stop-t0_start)
    
    t1_start = perf_counter()    
    for i in range (number):
        src=trajets[i][0]
        dest=trajets[i][1]
        myFile.write(str(min_power2(src,dest,par,rang)[1])+"\n")
    t1_stop = perf_counter()
    myFile.close()
    mean=(t1_stop-t1_start)/number
    lignes=open_route(filename)[2]
    return(mean*lignes)


