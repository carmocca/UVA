"""Implements finding connected components."""

from collections import deque


def get_connected_components(graph):
    """Finds all connected components of the graph.
    Returns a list of lists, each containing the nodes that form a connected component.
    Returns an empty list for an empty graph.
    """

    list_of_components = []
    component = []  # Not strictly necessary due to the while loop structure, but it helps the automated analysis tools

    # Store a list of all unreached vertices
    unreached = set(graph.get_all_node_ids())
    to_explore = deque()

    while len(unreached) > 0:
        # This happens when we reach the end of a connected component and still have more vertices to search through
        if len(to_explore) == 0:
            n = unreached.pop()
            unreached.add(n)
            to_explore.append(n)
            component = []
            list_of_components.append(component)

        # This is the BFS that searches for connected vertices
        while len(to_explore) > 0:
            n = to_explore.pop()
            if n in unreached:
                component.append(n)
                unreached.remove(n)
                nodes = graph.neighbors(n)
                for n in nodes:
                    if n in unreached:
                        to_explore.append(n)

    return list_of_components
