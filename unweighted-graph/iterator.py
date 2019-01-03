# 稀疏图迭代器
class SparseGraphIterator:
    def __init__(self, graph, v):
        self.graph = graph
        self.neighbours = self.graph.g[v]
        # print(self.neighbours)
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.neighbours):
            item = self.neighbours[self.index]
            self.index += 1
            return item
        else:
            raise StopIteration


# 稠密图迭代器
class DenseGraphIterator:
    def __init__(self, graph, v):
        self.graph = graph
        self.neighbours = self.graph.g[v]
        self.index = -1
        self.l = len(self.neighbours)

    def __iter__(self):
        return self

    def __next__(self):
        self.index += 1
        if self.index == self.l:
            raise StopIteration
        while not self.neighbours[self.index]:
            self.index += 1
            if self.index == self.l:
                raise StopIteration
        return self.index
