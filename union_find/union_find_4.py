# 并查集第 4 版：设置 parent 数组，在第 2 版的基础上，增加 rank 数组，
# 合并的时候，rank 少的指向 rank 多的，以避免节点的高度越来越高，在 find 上多消耗时间。
# 参考：慕课网：liuyubobobo。


class UnionFind4:

    def __init__(self, n):
        # 直接就初始化了，每个元素的 id 就是自己
        # 有多少个元素，就有多少个类
        self.parent = [i for i in range(n)]
        self.rank = [i for i in range(n)]
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

        if self.rank[p_id] < self.rank[q_id]:
            self.parent[p_id] = q_id
        elif self.rank[p_id] > self.rank[q_id]:
            self.parent[q_id] = p_id
        else:
            self.parent[p_id] = q_id
            self.rank[q_id] += 1
