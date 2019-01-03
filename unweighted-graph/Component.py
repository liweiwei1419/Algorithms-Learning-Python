# 使用深度优先遍历计算连通分量
class Component:
    def __init__(self, graph):
        self.graph = graph
        # 记录深度优先遍历的过程中结点是否被访问过
        self.vistied = [False for _ in range(self.graph.V())]
        # 每个结点对应的连通分量的标记，一开始设置为 -1 ，从 0 开始编号，设置成 0 是不正确的
        self.id = [-1] * self.graph.V()
        # 一开始连通分量设置为 0
        self.ccount = 0

        # 下面是深度优先遍历的模板代码
        # 求图的连通分量
        for i in range(self.graph.V()):
            if not self.vistied[i]:
                self.__dfs(i)
                # 一次深度优先遍历完成以后，连通分量 + 1
                self.ccount += 1

    def __dfs(self, v):
        self.vistied[v] = True
        self.id[v] = self.ccount

        for neighbour_index in self.graph.iterator(v):
            print(v, neighbour_index, self.vistied)
            if not self.vistied[neighbour_index]:
                self.__dfs(neighbour_index)

    def is_connected(self, v, w):
        assert 0 <= v < self.graph.V;
        assert 0 <= w < self.graph.V;
        return self.id[v] == self.id[w]
