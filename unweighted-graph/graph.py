from abc import ABCMeta, abstractmethod


class Graph(metaclass=ABCMeta):

    @property
    @abstractmethod
    def V(self):
        pass

    @property
    @abstractmethod
    def E(self):
        pass

    @abstractmethod
    def add_edge(self, v, w):
        pass

    @abstractmethod
    def has_edge(self, v, w):
        pass

    @abstractmethod
    def show(self):
        pass
