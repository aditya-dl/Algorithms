"""Implementation of Quick Find algorithm

Returns:
    Bool: True if two elements are connected else False
"""
from union_find import UnionFind


class QuickFind(UnionFind):
    """Implementation of Quick Find algorithm

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
        return self._id_store[index]

    def union(self, index_1, index_2):
        """Perform union operation of two elements

        Args:
            index_1 (int): element to perform union operation
            index_2 (int): element to perform union operation
        """
        self._validate(index_1)
        self._validate(index_2)

        id_1 = self._id_store[index_1]
        id_2 = self._id_store[index_2]

        for i in range(len(self._id_store)):
            if self._id_store[i] == id_1:
                self._id_store[i] = id_2

        self._count -= 1


if __name__ == "__main__":
    QF = QuickFind(3)
    QF.union(1, 2)
    print(QF.connected(1, 2))
    print(QF.find(1))
    print(QF.count)
    print(QF.id_store)
