"""Abstract Base Class of Union-Find operation

Raises:
    ValueError: element is out of bounds (<0 or >= length)

Returns:
    BOOL: True if two elements are connected else False
"""
from abc import ABC, abstractmethod


class UnionFind(ABC):
    """Union-Find API Abstract Base Class Implementation

    Args:
        ABC (abc): Python defined Abstract Base Class

    Raises:
        ValueError: element is out of bounds (<0 or >= length)

    Returns:
        [bool]: True if two elements are connected else False
    """
    @abstractmethod
    def __init__(self, number_of_elements):
        """Initialize array according to the number of elements provided

        Args:
            number_of_elements (int): Total number of integers in the workspace
        """
        self.id_store = number_of_elements

    @property
    @abstractmethod
    def id_store(self):
        """Get id_store (array consisting of canonical parents of each element)

        Returns:
            list: array consisting of canonical parents of each element
        """
        return self._id_store

    @id_store.setter
    @abstractmethod
    def id_store(self, number_of_elements):
        """Set id_store to default values of each element

        Args:
            number_of_elements (int): Total number of integers in the workspace
        """
        self._id_store = list((i for i in range(number_of_elements)))

    @abstractmethod
    def _validate(self, index):
        """Validate if the element is within 0 and number_of_elements

        Args:
            index (int): element to validate

        Raises:
            ValueError: element is out of bounds (<0 or >= length)
        """
        length = len(self._id_store)
        if index < 0 or index >= length:
            raise ValueError(
                f"Index {index} is not between {0} and {length-1}")

    @abstractmethod
    def find(self, index):
        """Find the canonical parent of the element

        Args:
            index (int): element to find parent of
        """

    @abstractmethod
    def connected(self, index_1, index_2):
        """Check if two elements are connected

        Args:
            index_1 (int): element to compare
            index_2 (int): element to compare

        Returns:
            bool: True if elements have same parent else False
        """
        self._validate(index_1)
        self._validate(index_2)
        return self._id_store[index_1] == self._id_store[index_2]

    @abstractmethod
    def union(self, index_1, index_2):
        """Perform union operation of two elements

        Args:
            index_1 (int): element to perform union operation
            index_2 (int): element to perform union operation
        """
