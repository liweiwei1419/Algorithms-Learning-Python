# 并查集第 6 版：路径压缩的版本 2，在 find 的时候，同时修改树的内部结构，使得树的高度越来越小。
# 基于递归，在 find 的时候，如果不是根节点，就把这个节点指向根节点，注意，递归的方法，应该返回父亲节点
# 参考：慕课网：liuyubobobo。


class UnionFind6:
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
        # 不太好理解，要多读几遍
        # 1、find 函数的定义应该这样理解：只要不是根节点，就把它的父亲节点指向它的根节点；
        # 2、self.find(self.parent[p]) 一定返回的是根
        # 3、记住这个递归函数最终在做什么，最后构成的是一棵只有一层的数
        if p != self.parent[p]:
            self.parent[p] = self.find(self.parent[p])
        return self.parent[p]

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
