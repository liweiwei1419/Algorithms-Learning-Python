from DenseGraph import DenseGraph
from SparseGraph import SparseGraph


class ReadGraph:
    def __init__(self, graph, filename):
        self.g = graph
        with open(filename, 'r') as fr:
            V, E = fr.readline().split(',')
            print('图的顶点数和边数：', V, E, end='')
            for line in fr.readlines():
                v, w = line.split(',')
                # print(v, w, end='')
                self.g.add_edge(int(v), int(w))


if __name__ == '__main__':
    filename = 'graph1.txt'
    # g = DenseGraph(13, False)
    # g = SparseGraph(13, False)

    # rg = ReadGraph(g, filename)
    # g.show()

    # for item in g.iterator(0):
    #     print(item)

    # 求图的连通分量测试代码

    # filename = 'graph2.txt'
    # g = SparseGraph(7, False)
    # rg = ReadGraph(g, filename)
    # g.show()
    # from g.Component import Component
    # c =  Component(g)
    # print(c.ccount)
    # print(c.id)

    # 测试连通分量
    filename = 'graph1.txt'
    g = SparseGraph(13, False)
    rg = ReadGraph(g, filename)
    g.show()
    from g.Component import Component

    c = Component(g)
    print(c.ccount)
    print(c.id)

    # 测试寻路算法

    print("测试寻路算法")
    from g.Path import Path

    p = Path(g, 0)
    p.show_path(6)
