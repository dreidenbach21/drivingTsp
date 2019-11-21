class UnionNode(object):

    def __init__(self, label):
        self.vertices = []  # current num of elements
        self.edges = [] # the number of disjoint sets or components
        self.label = label

    def edges(self):
        return self.edges
    def vertices(self):
        return self.vertices
