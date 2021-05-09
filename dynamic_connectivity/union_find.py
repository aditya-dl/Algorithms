from abc import ABC

class UnionFind(ABC):
    @abstractmethod
    def __init__(self, N):
        self.id = N
    
    @property
    @abstractmethod
    def id(self):
        return self._id

    @id.setter
    @abstractmethod
    def id(self, N):
        self._id = [i for i in range(N)]

    @abstractmethod
    def _validate(self, p):
        length = len(self._id)
        if p < 0 or p >= length:
            raise ValueError(f"Index {p} is not between {0} and {length-1}")

    @abstractmethod
    def find(self, p):
        pass

    @abstractmethod
    def connected(self, p, q):
        self._validate(p)
        self._validate(q)
        return self._id[p] == self._id[q]
    
    @abstractmethod
    def union(self, p, q):
        pass
