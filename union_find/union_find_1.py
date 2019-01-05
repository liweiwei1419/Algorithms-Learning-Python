# 并查集第 1 版：设置 id 数组，查找很快，合并的时候要遍历完整个 id 数组。
# 参考：慕课网：liuyubobobo。


class UnionFind1:
    def __init__(self, n):
        # 直接就初始化了，每个元素的 id 就是自己
        # 有多少个元素，就有多少个类
        self.id = [i for i in range(n)]
        self.count = n  # 数据的个数

    def find(self, p):
        """
        查找元素 p 所对应的集合的编号
        O(1)复杂度
        :param p:
        :return:
        """
        assert 0 <= p < self.count
        return self.id[p]

    def is_connected(self, p, q):
        """
        查询元素 p 和 q 是否属于同一个集合
        O(1)复杂度
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
            for i in range(self.count):
                if self.id[i] == p_id:
                    self.id[i] = q_id
