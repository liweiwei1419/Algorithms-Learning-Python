# 路径压缩比较好理解的版本。
# 参考：极客时间：覃超。


class UnionFind7:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.count = n

    def find(self, p):
        """
        查找元素 p 根节点的编号
        :param p:
        :return:
        """
        assert 0 <= p < self.count
        root = p
        while root != self.parent[root]:
            root = self.parent[root]
        # 此时 root 就是大 boss
        # 下面这一步就是最直接的路径压缩：
        # 把沿途查找过的结点都指向 root
        while p != self.parent[p]:
            temp = self.parent[p]
            self.parent[p] = root
            p = temp
        return root

    def is_connected(self, p, q):
        """
        查询元素 p 和 q 是否属于同一个集合
        有共同的父亲，就表示它们属于同一个集合
        :param p:
        :param q:
        :return:
        """
        return self.find(p) == self.find(q)

    def union(self, p, q):
        """
        合并元素 p 和元素 q 所属于的集合
        O(n)复杂度
        :param p:
        :param q:
        :return:
        """

        p_id = self.find(p)
        q_id = self.find(q)
        if p_id == q_id:
            return
        # 任意指向即可
        self.parent[p_id] = q_id
