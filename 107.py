from collections import namedtuple

PINF = 0xFFFFFFFF

class Graph(object):

    def __init__(self):
        self.vertices = []
        self.edges = set()

    def total_weight(self):
        return sum([weight for a,b,weight in self.edges])/2

    def add_vertice(self, vertice):
        self.vertices.append(vertice)

    def add_edge(self, vert1, vert2, weight):
        self.edges.add((vert1, vert2, weight))
        self.edges.add((vert2, vert1, weight))

    # Prim's algorithm
    def msp(self):
        g = Graph()

        CostObject = namedtuple("CostObject", ["vid", "cost", "edge"])
        cheapest = [CostObject(v, PINF, None) for v in self.vertices]

        remaining = { i: v for i,v in enumerate(self.vertices) }
        while len(remaining) > 0:
            min_cost = CostObject(-1, PINF, None)
            for i in remaining.keys():
                if cheapest[i].cost <= min_cost.cost:
                    min_cost = cheapest[i]

            del remaining[min_cost.vid]

            g.add_vertice(self.vertices[min_cost.vid])
            if min_cost.edge: g.add_edge(*min_cost.edge)

            for a,b,weight in self.edges:
                if a != min_cost.vid: continue
                if not b in remaining.values(): continue
                if weight > cheapest[b].cost: continue

                cheapest[b] = CostObject(b, weight, (a,b,weight))

        return g


with open("p107_network.txt") as fh:
#with open("107.data") as fh:

    rows = [x.strip().split(",") for x in fh.read().split("\n") if x]

    print "vertice count: %d" % len(rows)

    g = Graph()
    for i in xrange(len(rows)): g.add_vertice(i)

    for i, row in enumerate(rows):
        for j, weight in enumerate(row[0:i]):
            if weight == "-": continue
            g.add_edge(g.vertices[j], g.vertices[i], int(weight))

    print "Initial weight: %d" % g.total_weight()
    msp = g.msp()
    print "MSP weight: %d" % msp.total_weight()
    print "Saving: %d" % (g.total_weight() - msp.total_weight())
    #print msp.edges
    #print msp.vertices
