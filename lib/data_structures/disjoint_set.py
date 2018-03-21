"""Implements a Union/Find Disjoint Set class, used in other algorithms."""


class DisjointSet(object):
    """Implements an efficient disjoint set collection."""

    _label_counter = 0
    _set_counter = 0
    _forest = None

    def __init__(self):
        # We are using the implicit parent-pointer structure to store the trees
        self._forest = {}

    def __len__(self):
        return self._set_counter

    def __str__(self):
        return str(self._forest)

    def add_set(self):
        """Adds a new set to the forest.
        Returns a label by which the new set can be referenced
        """
        self._label_counter += 1
        new_label = self._label_counter
        self._forest[new_label] = -1  # All new sets have their parent set to themselves
        self._set_counter += 1
        return new_label

    def find(self, node_label):
        """Finds the set containing the node_label.
        Returns the set label.
        """
        queue = []
        current_node = node_label
        while self._forest[current_node] >= 0:
            queue.append(current_node)
            current_node = self._forest[current_node]
        root_node = current_node

        # Path compression
        for n in queue:
            self._forest[n] = root_node

        return root_node

    def union(self, label_a, label_b):
        """Joins two sets into a single new set.
        label_a, label_b can be any nodes within the sets
        """
        # Base case to avoid work
        if label_a == label_b:
            return

        # Find the tree root of each node
        root_a = self.find(label_a)
        root_b = self.find(label_b)

        # Avoid merging a tree to itself
        if root_a == root_b:
            return

        self._union(root_a, root_b)
        self._set_counter -= 1

    def _union(self, root_a, root_b):
        """Internal function to join two set trees specified by root_a and root_b.
        Assumes root_a and root_b are distinct.
        """
        # Merge the trees, smaller to larger
        update_rank = False
        # Determine the larger tree
        rank_a = self._forest[root_a]
        rank_b = self._forest[root_b]
        if rank_a < rank_b:
            larger, smaller = root_b, root_a
        else:
            larger, smaller = root_a, root_b
            if rank_a == rank_b:
                update_rank = True
        # Make the smaller tree a subtree of the larger tree
        self._forest[smaller] = larger
        # Update the rank of the new tree (if necessary)
        if update_rank:
            self._forest[larger] -= 1
