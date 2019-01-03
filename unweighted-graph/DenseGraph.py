from iterator import DenseGraphIterator


class DenseGraph:
    def __init__(self, n, directed):
        assert n > 0
        # 结点数
        self.n = n
        # 边数
        self.m = 0
        # 是否是有向图
        self.directed = directed
        # 图的具体数据
        self.g = [[False for _ in range(n)] for _ in range(n)]

    def add_edge(self, v, w):
        assert 0 <= v < self.n
        assert 0 <= w < self.n
        # 如果已经有了结点 v 到结点 w 的边
        # 就直接返回，不再添加邻边，和 m + 1
        if self.has_edge(v, w):
            return
        self.g[v][w] = True
        # 如果是无向图，维护无向图的对称性
        if not self.directed:
            self.g[w][v] = True
        self.m += 1

    def has_edge(self, v, w):
        assert 0 <= v < self.n
        assert 0 <= w < self.n
        return self.g[v][w]

    def show(self):
        for i in range(self.n):
            for j in range(self.n):
                if self.g[i][j]:
                    print('1', end=' ')
                else:
                    print('0', end=' ')
            print()

    def iterator(self, v):
        return DenseGraphIterator(self, v)
