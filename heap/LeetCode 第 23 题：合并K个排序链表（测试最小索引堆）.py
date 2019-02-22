class IndexMinHeap:

    def __init__(self, capacity):
        self.data = [0 for _ in range(capacity + 1)]
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

        self.indexes[self.count + 1] = i
        # 注意：反向查找表是如何更新的
        self.reverse[i] = self.count + 1

        self.count += 1
        self.__shift_up(self.count)

    def __shift_up(self, k):
        while k > 1 and self.data[self.indexes[k // 2]] > self.data[self.indexes[k]]:
            self.indexes[k // 2], self.indexes[k] = self.indexes[k], self.indexes[k // 2]
            # 只要索引发生交换，反向查找表也要更新
            self.reverse[self.indexes[k // 2]] = k // 2
            self.reverse[self.indexes[k]] = k

            k //= 2

    def extract_min(self):
        if self.count == 0:
            raise Exception('堆里没有可以取出的元素')
        # 里面套一层 indexes
        ret = self.data[self.indexes[1]]
        # 交换的是索引
        self.indexes[1], self.indexes[self.count] = self.indexes[self.count], self.indexes[1]
        # 只要索引发生交换，反向查找表也要更新
        self.reverse[self.indexes[1]] = 1
        self.reverse[self.indexes[self.count]] = self.count

        # 设置失效
        self.reverse[self.indexes[self.count]] = 0

        self.count -= 1
        self.__shift_down(1)
        return ret

    def __shift_down(self, k):
        while 2 * k <= self.count:
            j = 2 * k
            # 比较的是 data ，交换的是 indexes
            if j + 1 <= self.count and self.data[self.indexes[j + 1]] < self.data[self.indexes[j]]:
                j = j + 1
            if self.data[self.indexes[k]] <= self.data[self.indexes[j]]:
                break
            self.indexes[k], self.indexes[j] = self.indexes[j], self.indexes[k]

            # 只要索引发生交换，反向查找表也要更新
            self.reverse[self.indexes[k]] = k
            self.reverse[self.indexes[j]] = j

            k = j

    # 新增方法
    def extract_min_index(self):
        assert self.count > 0
        # 减 1 是为了符合用户视角
        ret = self.indexes[1] - 1
        self.indexes[1], self.indexes[self.count] = self.indexes[self.count], self.indexes[1]

        # 只要索引发生交换，反向查找表也要更新
        self.reverse[self.indexes[1]] = 1
        self.reverse[self.indexes[self.count]] = self.count

        # 设置失效
        self.reverse[self.indexes[self.count]] = 0

        self.count -= 1
        self.__shift_down(1)
        return ret

    # 新增方法
    def get_min_index(self):
        return self.indexes[1] - 1

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


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeKLists(self, lists: 'List[ListNode]') -> 'ListNode':

        # 这一步是去掉空链表
        new_lists = []
        for i in range(len(lists)):
            if lists[i]:
                new_lists.append(lists[i])

        size = len(new_lists)
        index_min_heap = IndexMinHeap(size)
        for i in range(size):
            index_min_heap.insert(i,new_lists[i].val)

        dummy = ListNode(-1)
        cur = dummy
        while index_min_heap.size() > 0:
            index = index_min_heap.get_min_index()

            print(index, index_min_heap.data,new_lists[index].val)
            cur.next = ListNode(new_lists[index].val)
            cur = cur.next
            if new_lists[index].next is None:
                # 如果后面没有元素，就可以删掉了
                index_min_heap.extract_min_index()
            else:
                index_min_heap.change(index, new_lists[index].next.val)
                new_lists[index] = new_lists[index].next
        return dummy.next


def create_linked_list(nums):
    if len(nums) == 0:
        return None
    head = ListNode(nums[0])
    cur = head
    for i in range(1, len(nums)):
        cur.next = ListNode(nums[i])
        cur = cur.next
    return head


def print_linked_list(list_node):
    if list_node is None:
        return

    cur = list_node
    while cur:
        print(cur.val, '->', end=' ')
        cur = cur.next
    print('null')


if __name__ == '__main__':
    sorted_linked1 = create_linked_list([i for i in range(1, 20, 3)])
    sorted_linked2 = create_linked_list([i for i in range(2, 20, 3)])
    sorted_linked3 = create_linked_list([i for i in range(3, 20, 3)])

    print_linked_list(sorted_linked1)
    print_linked_list(sorted_linked2)
    print_linked_list(sorted_linked3)

    solution = Solution()

    result = solution.mergeKLists(lists=[sorted_linked1, sorted_linked2, sorted_linked3])
    print_linked_list(result)

    sorted_linked1 = create_linked_list([1,2,3])
    sorted_linked2 = create_linked_list([4,5,6,7])
    sorted_linked3 = create_linked_list([])

    solution = Solution()

    result = solution.mergeKLists(lists=[sorted_linked1, sorted_linked2,sorted_linked3])
    print_linked_list(result)
