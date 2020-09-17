"""In this exercise you'll need to add functions to a Graph class
 to return various representations of the same graph. Your graph will have two different components: Nodes and Edges."""

class Node():
    def __init__(self, value):
        self.value = value 
        self.edges = []

class Edge():
    def __init__(self, value, node_from, node_to):
        self.value = value 
        self.node_from = node_from 
        self.node_to = node_to 

class Graph():
    def __init__(self, nodes=[], edges=[]):
        self.nodes = nodes
        self.edges = edges 
    
    def insert_node(self, new_node_value):
        new_node = Node(new_node_value)
        self.nodes.append(new_node)
    
    def insert_edge(self, new_edge_value, node_from_value, node_to_value):
        from_found = None 
        to_found = None
        for node in self.nodes:
            if node.value == node_from_value:
                from_found = node 
            if node.value == node_to_value:
                to_found = node 
        if from_found == None: 
            from_found = Node(node_from_value)
            self.nodes.append(from_found)
        if to_found == None:
            to_found = Node(node_to_value)
            self.nodes.append(to_found)
        new_edge = Edge(new_edge_value, from_found, to_found)
        from_found.edges.append(new_edge)
        to_found.edges.append(new_edge)
        self.edges.append(new_edge)

    def get_edge_list(self):
        """Don't return a list of edge objects!
        Return a list of triples that looks like this:
        (Edge Value, From Node Value, To Node Value)"""
        l = []
        for edge in self.edges:
            triples = (edge.value, edge.node_from.value, edge.node_to.value)
            l.append(triples)
        return l 

    def get_adjacency_list(self):
        """Don't return any Node or Edge objects!
        You'll return a list of lists.
        The indecies of the outer list represent
        "from" nodes.
        Each section in the list will store a list
        of tuples that looks like this:
        (To Node, Edge Value)"""
        n = len(self.nodes) # max(self.nodes)??
        outer = []
        for i in range(n+1):
            inner = []
            for edge in self.edges:
                if edge.node_from.value == i:
                    inner.append((edge.node_to.value, edge.value))
            if inner:
                outer.append(inner)
            else:
                outer.append(None)    
        return outer
    
    def get_adjacency_matrix(self):
        """Return a matrix, or 2D list.
        Row numbers represent from nodes,
        column numbers represent to nodes.
        Store the edge values in each spot,
        and a 0 if no edge exists."""
        n = len(self.nodes)
        outer = []
        for node_from in range(n+1):
            inner = [0]*(n+1)
            for edge in self.edges:
                if edge.node_from.value == node_from:
                    inner[edge.node_to.value] = edge.value 
            outer.append(inner)

        return outer

if __name__ == "__main__":
    graph = Graph()
    graph.insert_edge(100, 1, 2)
    graph.insert_edge(101, 1, 3)
    graph.insert_edge(102, 1, 4) 
    graph.insert_edge(103, 3, 4)
    # Should be [(100, 1, 2), (101, 1, 3), (102, 1, 4), (103, 3, 4)]
    print(graph.get_edge_list())
    # Should be [None, [(2, 100), (3, 101), (4, 102)], None, [(4, 103)], None]
    print(graph.get_adjacency_list())
    # Should be [[0, 0, 0, 0, 0], [0, 0, 100, 101, 102], [0, 0, 0, 0, 0], [0, 0, 0, 0, 103], [0, 0, 0, 0, 0]]
    print(graph.get_adjacency_matrix())




    


    


    

    