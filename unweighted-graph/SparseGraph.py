from iterator import SparseGraphIterator


class SparseGraph:
    def __init__(self, n, directed):
        assert n > 0
        # 结点数
        self.n = n
        # 边数
        self.m = 0
        # 是否是有向图
        self.directed = directed
        # 图的具体数据
        self.g = [[] for _ in range(n)]

    def add_edge(self, v, w):
        assert 0 <= v < self.n
        assert 0 <= w < self.n

        # 在邻接表的实现中，has_edge 方法要进行遍历
        # 这一步的时间复杂度是比较高的
        # 我们在学习的时候，可以不进行判断，即允许平行边
        # 我们这里暂时保留
        if self.has_edge(v, w):
            return

        v_neighbours = self.g[v]
        v_neighbours.append(w)

        # 如果是无向图，维护无向图的对称性
        # v != w 不允许自环边
        if v != w and not self.directed:
            w_neighbours = self.g[w]
            w_neighbours.append(v)
        self.m += 1

    def has_edge(self, v, w):
        assert 0 <= v < self.n
        assert 0 <= w < self.n

        # v 的所有相邻结点的集合
        v_neighbours = self.g[v]
        for neighbour in v_neighbours:
            if neighbour == w:
                return True
        return False

    def show(self):
        for v in range(self.n):
            print("顶点", v, end=": ")
            for neighbour in self.g[v]:
                print(neighbour, end=',')
            print()

    def iterator(self, v):
        return SparseGraphIterator(self, v)
