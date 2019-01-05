# 并查集第 5 版：路径压缩的版本 1，在 find 的时候，同时修改树的内部结构，使得树的高度越来越小。
# 基于循环，在 find 的时候，只有一行代码：self.parent[p] = self.parent[self.parent[p]]
# 参考：慕课网：liuyubobobo。


class UnionFind5:
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
            # 仔细体会这句代码的意思，理解这句代码的技巧是，画一个图出来就可以了
            # 把这个元素的父节点，指向它父节点的父节点
            # 此时 rank 语义发生了变化，我们不去维护它，但是仍然可以作为合并时候的一个参考值
            self.parent[p] = self.parent[self.parent[p]]
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
