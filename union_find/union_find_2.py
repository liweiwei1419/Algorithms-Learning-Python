# 并查集第 2 版：设置 parent 数组，查找就变得慢了一些，得一直向上查找；
# 合并的时候，就快了，把其中一个节点的父节点指向另一个节点即可。
# 参考：慕课网：liuyubobobo。


class UnionFind2:
    def __init__(self, n):
        # 直接就初始化了，每个元素的 id 就是自己
        # 有多少个元素，就有多少个类
        self.parent = [i for i in range(n)]
        self.count = n  # 数据的个数

    def find(self, p):
        """
        查找元素 p 根节点的编号
        :param p:
        :return:
        """
        assert 0 <= p < self.count
        while p != self.parent[p]:
            p = self.parent[p]
        return p

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
        else:
            # 任意将其中一个结点的父结点指向另一个结点的父结点
            self.parent[p_id] = q_id
