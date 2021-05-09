"""Implementation of Quick Union algorithm

Returns:
    Bool: True if two elements are connected else False
"""
from union_find import UnionFind


class QuickUnion(UnionFind):
    """Implementation of Quick Union algorithm

    Args:
        UnionFind (class): ABC import of Union Find
    """
    def find(self, index):
        """Find the canonical parent of the element

        Args:
            index (int): element to find parent of

        Returns:
            int: returns the canonical parent of element at index
        """
        self._validate(index)
        while index != self._id_store[index]:
            index = self._id_store[index]

        return index

    def union(self, index_1, index_2):
        """Perform union operation of two elements

        Args:
            index_1 (int): element to perform union operation
            index_2 (int): element to perform union operation
        """
        parent_1 = self.find(index_1)
        parent_2 = self.find(index_2)

        if parent_1 == parent_2:
            return
        self._id_store[parent_1] = parent_2

        self._count -= 1

    def connected(self, index_1, index_2):
        """Check if two elements are connected

        Args:
            index_1 (int): element to compare
            index_2 (int): element to compare

        Returns:
            bool: True if elements have same parent else False
        """
        return self.find(index_1) == self.find(index_2)


if __name__ == "__main__":
    QU = QuickUnion(3)
    QU.union(1, 2)
    print(QU.connected(1, 2))
    print(QU.find(1))
    print(QU.count)
    print(QU.id_store)
