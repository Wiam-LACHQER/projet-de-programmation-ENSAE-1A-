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
    

    def get_path_with_power(self, src, dest, power):
        raise NotImplementedError
    
    """La fonction explorer permet de récupérer la composante de graphe associée au noeud fourni en parametre"""
    def explorer(self,node,compenent=[]):
        compenent.append(node)
        for neighbor in self.graph[node]:
            if neighbor[0] not in compenent:
                compenent=self.explorer(neighbor[0],compenent)
        return compenent
    
    """Cette fonction permet de récupérer une liste de listes, chacune représente une composante du graphe"""
    def connected_components(self):
        nodes1=self.nodes
        compenents=[]
        while nodes1!=[]:
            compenent=self.explorer(nodes1[0],[])
            print(compenent) 
            """print sert seulement à visualiser les listes intermédiaires"""
            for elem in compenent:
                nodes1.remove(elem)
            print(nodes1) 
            """print sert seulement à visualiser les listes intermédiaires"""
            compenents.append(compenent)
        return compenents


    def connected_components_set(self):
        """
        The result should be a set of frozensets (one per component), 
        For instance, for network01.in: {frozenset({1, 2, 3}), frozenset({4, 5, 6, 7})}
        """
        return set(map(frozenset, self.connected_components()))
    
    def min_power(self, src, dest):
        """
        Should return path, min_power. 
        """
        raise NotImplementedError


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
    """Entiers est une liste de listes des entiers de chaque ligne"""
    Entiers=[]
    for elem in Lignes: 
        T = elem.split(" ")
        Z = [int(i) for i in T]
        Entiers.append(Z)

    nb_nodes = Entiers[0][0]
    nb_edges = Entiers[0][1]
    nodes=[i for i in range(1,nb_nodes+1)]
    for i in range(1,len(Entiers)):
        node1=Entiers[i][0]
        node2=Entiers[i][1]
        power_min=Entiers[i][2]
        graph.add_edge(node1, node2, power_min, dist=1)


    fichier.close()
    return graph