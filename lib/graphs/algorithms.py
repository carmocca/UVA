
from lib.data_structures import DisjointSet, PriorityQueue
from lib.graphs.utils import get_connected_components


def minimum_spanning_tree(graph):
    """Calculates a minimum spanning tree for a graph.
    Returns a list of edges that define the tree.
    Returns an empty list for an empty graph.
    """
    mst = []

    if graph.num_nodes() == 0:
        return mst
    if graph.num_edges() == 0:
        return mst

    connected_components = get_connected_components(graph)
    if len(connected_components) > 1:
        raise ValueError('There are no connected components in this graph')

    edge_list = kruskal_mst(graph)

    return edge_list


def kruskal_mst(graph):
    """Implements Kruskal's Algorithm for finding minimum spanning trees.
    Assumes a non-empty, connected graph.
    """
    edges_accepted = 0
    ds = DisjointSet()
    pq = PriorityQueue()
    accepted_edges = []
    label_lookup = {}

    nodes = graph.get_all_node_ids()
    num_vertices = len(nodes)
    for n in nodes:
        label = ds.add_set()
        label_lookup[n] = label

    edges = graph.get_all_edge_objects()
    for e in edges:
        pq.put(e['id'], e['cost'])

    while edges_accepted < (num_vertices - 1):
        edge_id = pq.get()

        edge = graph.get_edge(edge_id)
        node_a, node_b = edge['vertices']
        label_a = label_lookup[node_a]
        label_b = label_lookup[node_b]

        a_set = ds.find(label_a)
        b_set = ds.find(label_b)

        if a_set != b_set:
            edges_accepted += 1
            accepted_edges.append(edge_id)
            ds.union(a_set, b_set)

    return accepted_edges
