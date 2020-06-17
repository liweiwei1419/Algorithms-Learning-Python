from sorting.examples import GenerateRandomArrayStrategy
from sorting.sorting_util import SortingUtil


class MergeSort:

    def __str__(self):
        return "归并排序"

    def __merge_of_two_sorted_array(self, arr, left, mid, right):
        # Python 中切片即复制，复制到一个临时数组中
        nums_for_compare = arr[left:right + 1]
        i = 0
        j = mid - left + 1
        # 通过 nums_for_compare 数组中设置两个指针 i、j 分别表示两个有序数组的开始
        # 覆盖原始数组
        for k in range(left, right + 1):
            if i > mid - left:
                arr[k] = nums_for_compare[j]
                j += 1
            elif j > right - left:
                arr[k] = nums_for_compare[i]
                i += 1
            elif nums_for_compare[i] <= nums_for_compare[j]:
                # 注意：这里使用 <= 是为了保证归并排序算法的稳定性
                arr[k] = nums_for_compare[i]
                i += 1
            else:
                assert nums_for_compare[i] >= nums_for_compare[j]
                arr[k] = nums_for_compare[j]
                j += 1

    def __merge_sort(self, arr, left, right):
        if left >= right:
            return
        # 这是一个陷阱，如果 left 和 right 都很大的话，left + right 容易越界
        # Python 中整除使用 // 2
        mid = (left + right) // 2
        self.__merge_sort(arr, left, mid)
        self.__merge_sort(arr, mid + 1, right)
        self.__merge_of_two_sorted_array(arr, left, mid, right)

    @SortingUtil.cal_time
    def sort(self, arr):
        """
        归并排序的入口函数
        """
        size = len(arr)
        self.__merge_sort(arr, 0, size - 1)


class MergeSortOptimizer:

    def __str__(self):
        return "归并排序的优化"

    def __merge_of_two_sorted_array(self, arr, left, mid, right):
        # 将原数组 [left, right] 区间内的元素复制到辅助数组
        for index in range(left, right + 1):
            nums_for_compare[index] = arr[index]

        i = left
        j = mid + 1
        for k in range(left, right + 1):
            if i == mid + 1:
                # i 用完了，就拼命用 j
                arr[k] = nums_for_compare[j]
                j += 1
            elif j > right:
                # j 用完了，就拼命用 i
                arr[k] = nums_for_compare[i]
                i += 1
            elif nums_for_compare[i] <= nums_for_compare[j]:
                arr[k] = nums_for_compare[i]
                i += 1
            else:
                assert nums_for_compare[i] > nums_for_compare[j]
                arr[k] = nums_for_compare[j]
                j += 1

    def insert_sort_for_sub_interval(self, arr, left, right):
        """多次赋值的插入排序"""
        for i in range(left + 1, right + 1):
            temp = arr[i]
            j = i
            # 注意：这里 j 最多到 left
            while j > left and arr[j - 1] > temp:
                arr[j] = arr[j - 1]
                j -= 1
            arr[j] = temp

    def __merge_sort(self, arr, left, right):
        if right - left <= 15:
            self.insert_sort_for_sub_interval(arr, left, right)
            return
        mid = left + (right - left) // 2
        self.__merge_sort(arr, left, mid)
        self.__merge_sort(arr, mid + 1, right)
        if arr[mid] <= arr[mid + 1]:
            return
        self.__merge_of_two_sorted_array(arr, left, mid, right)

    @SortingUtil.cal_time
    def sort(self, arr):
        global nums_for_compare
        size = len(arr)
        nums_for_compare = list(range(size))
        self.__merge_sort(arr, 0, size - 1)


class MergeSortBU:

    def __str__(self):
        return "自底向上的归并排序"

    def __merge_of_two_sorted_array(self, arr, left, mid, right):
        for index in range(left, right + 1):
            nums_for_compare[index] = arr[index]
        i = left
        j = mid + 1
        for k in range(left, right + 1):
            if i == mid + 1:
                arr[k] = nums_for_compare[j]
                j += 1
            elif j > right:
                arr[k] = nums_for_compare[i]
                i += 1
            elif nums_for_compare[i] <= nums_for_compare[j]:
                arr[k] = nums_for_compare[i]
                i += 1
            else:
                assert nums_for_compare[i] > nums_for_compare[j]
                arr[k] = nums_for_compare[j]
                j += 1

    @SortingUtil.cal_time
    def sort(self, arr):
        size = len(arr)
        global nums_for_compare
        nums_for_compare = list(range(size))
        sz = 1
        # sz = 1, 2, 4, 8
        while sz < size:
            # left = 0, 2, 4, 6
            left = 0
            while left < size - sz:
                self.__merge_of_two_sorted_array(arr, left, left + sz - 1, min(left + sz + sz - 1, size - 1))
                left += 2 * sz
            sz *= 2


if __name__ == '__main__':
    # 测试基本的归并排序算法正确
    # SortingUtil.test_sorting_algorithm(MergeSort())

    # 比较插入排序与归并排序，可以看出归并排序快很多
    # SortingUtil.compare_sorting_algorithms(GenerateRandomArrayStrategy(),
    #                                        InsertionSortOptimizer(),
    #                                        MergeSort())

    # 比较归并排序与归并排序的优化
    # SortingUtil.compare_sorting_algorithms(GenerateRandomArrayStrategy(),
    #                                        MergeSort(),
    #                                        MergeSortOptimizer())

    # 测试自底向上的归并排序
    # SortingUtil.test_sorting_algorithm(MergeSortBU())

    # 比较自顶向下的归并排序（递归实现）与自底向上的归并排序（循环实现）
    # 自底向上的归并排序更耗时，因为分割不均匀
    SortingUtil.compare_sorting_algorithms(GenerateRandomArrayStrategy(),
                                           MergeSortOptimizer(),
                                           MergeSortBU())
