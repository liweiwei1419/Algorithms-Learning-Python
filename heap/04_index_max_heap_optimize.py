#
class IndexMaxHeap:
    def __init__(self, capacity):
        self.data = [None for _ in range(capacity + 1)]
        # 初值设置为 0 ，表示该位置还没有放置元素
        self.indexes = [0 for _ in range(capacity + 1)]
        self.reverse = [0 for _ in range(capacity + 1)]
        self.count = 0
        self.capacity = capacity

    def size(self):
        return self.count

    def is_empty(self):
        return self.count == 0

    # 此时 insert 要给一个索引位置
    def insert(self, i, item):
        if self.count + 1 > self.capacity:
            raise Exception('堆的容量不够了')
        i += 1
        self.data[i] = item

        # 这一步很关键，在内部索引数组的最后设置索引数组的索引
        self.indexes[self.count + 1] = i
        self.reverse[i] = self.count + 1

        self.count += 1
        self.__shift_up(self.count)

    def __shift_up(self, k):
        while k > 1 and self.data[self.indexes[k // 2]] < self.data[self.indexes[k]]:
            self.indexes[k // 2], self.indexes[k] = self.indexes[k], self.indexes[k // 2]

            self.reverse[self.indexes[k // 2]] = k // 2
            self.reverse[self.indexes[k]] = k

            k //= 2

    def extract_max(self):
        if self.count == 0:
            raise Exception('堆里没有可以取出的元素')
        ret = self.data[self.indexes[1]]
        self.indexes[1], self.indexes[self.count] = self.indexes[self.count], self.indexes[1]
        self.reverse[self.indexes[1]] = 1
        self.reverse[self.indexes[self.count]] = self.count


        self.reverse[self.indexes[self.count]] = 0

        self.count -= 1
        self.__shift_down(1)
        return ret

    def __shift_down(self, k):
        while 2 * k <= self.count:
            j = 2 * k
            if j + 1 <= self.count and self.data[self.indexes[j + 1]] > self.data[self.indexes[j]]:
                j = j + 1
            if self.data[self.indexes[k]] >= self.data[self.indexes[j]]:
                break
            self.indexes[k], self.indexes[j] = self.indexes[j], self.indexes[k]

            self.reverse[self.indexes[k]] = k
            self.reverse[self.indexes[j]] = j

            k = j

    # 新增方法
    def extract_max_index(self):
        assert self.count > 0
        # 减 1 是为了符合用户视角
        ret = self.indexes[1] - 1
        self.indexes[1], self.indexes[self.count] = self.indexes[self.count], self.indexes[1]
        self.count -= 1
        self.__shift_down(1)
        return ret

    # 新增方法
    def get_item(self, i):
        # 内部数组的索引比用户视角多 1
        return self.data[i + 1]

    # 新增方法
    def change(self, i, new_item):
        # 把用户视角改成内部索引
        i += 1
        self.data[i] = new_item

        # 重点：下面这一步是找原来数组中索引是 i 的元素
        # 在索引数组中的索引是几，这是一个唯一值，找到即返回
        # 优化：可以引入反向查找技术优化

        j = self.reverse[i]
        self.__shift_down(j)
        self.__shift_up(j)


if __name__ == '__main__':
    index_max_heap = IndexMaxHeap(10)

    data = [15, 17, 19, 13, 22, 16, 28, 30, 41, 62]

    for i, val in enumerate(data):
        index_max_heap.insert(i, val)
    print([i for i in range(10)])
    print(index_max_heap.indexes)
    print(index_max_heap.reverse)
    print(index_max_heap.data)
