class MaxHeap:
    def __init__(self, nums):
        self.capacity = len(nums)
        self.data = [None] * (self.capacity + 1)
        self.count = len(nums)
        self.__heapify(nums)

    def __heapify(self, nums):
        # 挨个赋值
        for i in range(self.capacity):
            self.data[i + 1] = nums[i]
        for i in range(self.count // 2, 0, -1):
            self.__sink(i)

    def size(self):
        return self.count

    def is_empty(self):
        return self.count == 0

    def insert(self, item):
        if self.count + 1 > self.capacity:
            raise Exception('堆的容量不够了')
        self.count += 1
        self.data[self.count] = item
        self.__swim(self.count)

    def __swim(self, k):
        temp = self.data[k]
        while k > 1 and self.data[k // 2] < temp:
            self.data[k] = self.data[k // 2]
            k //= 2
        self.data[k] = temp

    def extract_max(self):
        if self.count == 0:
            raise Exception('堆里没有可以取出的元素')
        ret = self.data[1]
        self.data[1], self.data[self.count] = self.data[self.count], self.data[1]
        self.count -= 1
        self.__sink(1)
        return ret

    def __sink(self, k):
        # 下沉
        temp = self.data[k]
        while 2 * k <= self.count:
            j = 2 * k
            if j + 1 < self.count and self.data[j + 1] > self.data[j]:
                j += 1
            if temp >= self.data[j]:
                break
            self.data[k] = self.data[j]
            k = j
        self.data[k] = temp

    def check_if_max_heap(self):
        for i in range(1, self.count // 2 + 1):
            if (2 * i <= self.capacity and self.data[i] < self.data[2 * i]) or \
                    (2 * i + 1 <= self.capacity and self.data[i] < self.data[2 * i + 1]):
                raise Exception('不是最大堆！')
        print('是最大堆！')

    def print_heap(self):
        print(self.data)


if __name__ == '__main__':
    nums = [184, 168, 110, 63, 121, 65, 108, 4, 25, 2]
    max_heap = MaxHeap(nums=nums)
    max_heap.print_heap()
    max_heap.check_if_max_heap()
