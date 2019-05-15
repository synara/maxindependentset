class Node (object):
    def __init__(self, label):
        self.label = label
        self.nodes = []

    
    def add_node(self, node):
        self.nodes.append(node)

    def get_degree(self):
        return len(self.nodes)

def get_degree(node):
    return node.get_degree()

def get_max_set(nodes):
    result = []
    nodes = sorted(nodes, key = get_degree)

    for n1 in nodes:
        found = False
        for n2 in result:
            if n2 in n1.nodes:
                found = True
                break            
        if not found:
            result.append(n1)

    return result

if __name__ == '__main__':
    nodes = []
    n1 = Node('A')
    nodes.append(n1)
    n2 = Node('B')
    nodes.append(n2)
    n3 = Node('C')
    nodes.append(n3)
    n4 = Node('D')
    nodes.append(n4)
    n5 = Node('E')
    nodes.append(n5)
    n6 = Node('F')
    nodes.append(n6)
    n7 = Node('G')
    nodes.append(n7)

    n1.add_node(n3)
    n2.add_node(n3)
    n2.add_node(n5)
    n3.add_node(n1)
    n3.add_node(n2)
    n3.add_node(n4)
    n3.add_node(n7)
    n4.add_node(n3)
    n5.add_node(n2)
    n5.add_node(n6)
    n6.add_node(n5)
    n7.add_node(n3)
    
    result = get_max_set(nodes)
    for node in result:
        print(node.label)
