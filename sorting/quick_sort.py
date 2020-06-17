from sorting.sorting_util import SortingUtil


class QuickSort:

    def __str__(self):
        return "最基本的快速排序"

    def __partition(self, arr, left, right):
        """对区间 [left, right] （包括左右端点）执行 partition 操作，将 pivot 挪到它最终应该在的位置"""
        pivot = arr[left]
        lt = left
        # 循环不变式
        # [left, lt - 1] < pivot，初始时，lt - 1 = left - 1
        # [lt, i) >= pivot，初始时，[left, left + 1)
        # i 的性质在循环开始的时候，不能推测出，我们就是要在循环中保持这个性质
        for i in range(left + 1, right + 1):
            if arr[i] < pivot:
                lt += 1
                arr[lt], arr[i] = arr[i], arr[lt]

        arr[left], arr[lt] = arr[lt], arr[left]
        return lt

    def __quick_sort(self, nums, left, right):
        """在区间 [left, right] （包括左右端点）执行快速排序操作"""
        if left >= right:
            return
        p_index = self.__partition(nums, left, right)
        self.__quick_sort(nums, left, p_index - 1)
        self.__quick_sort(nums, p_index + 1, right)

    def sort(self, arr):
        size = len(arr)
        self.__quick_sort(arr, 0, size - 1)


# 快速排序
# 在 partition 的过程中使用指针对撞的
# 特别注意，与标定点相等的元素的处理

# 双路快排：
# 随机将与标定点相等的元素分配到左边和右边
# 针对有许多重复键值的数组进行排序
class QuickSortTwoWays:

    def __str__(self):
        return "双路快排"

    def __partition(self, arr, left, right):
        p = arr[left]
        le = left + 1
        ge = right
        while True:
            # 针对索引进行判断的时候，要考虑是否越界
            while le <= right and arr[le] < p:
                le += 1
            while ge >= left + 1 and arr[ge] > p:
                ge -= 1
            if le > ge:
                break
            arr[le], arr[ge] = arr[ge], arr[le]
            le += 1
            ge -= 1
        # 注意：这里交换 left 与 ge 的位置
        arr[left], arr[ge] = arr[ge], arr[left]
        return ge

    def __quick_sort(self, arr, left, right):
        if left >= right:
            return
        p_index = self.__partition(arr, left, right)
        self.__quick_sort(arr, left, p_index - 1)
        self.__quick_sort(arr, p_index + 1, right)

    def sort(self, arr):
        size = len(arr)
        self.__quick_sort(arr, 0, size - 1)

# 快速排序
# 三路快速排序，在有很多相等元素的情况下，最优
# 特别注意，与标定点相等的元素的处理



class QuickSortThreeWays:

    def __str__(self):
        return "三路快排"

    def __partition(self, arr, left, right):
        p = arr[left]
        # 循环不变式
        # (left, lt] < pivot
        # [lt + 1, i) = pivot
        # [gt, right] > pivot

        lt = left
        gt = right + 1
        i = left + 1
        while i < gt:
            if arr[i] < p:
                lt += 1
                arr[i], arr[lt] = arr[lt], arr[i]
                i += 1
            elif arr[i] == p:
                i += 1
            else:
                gt -= 1
                arr[i], arr[gt] = arr[gt], arr[i]
        arr[left], arr[lt] = arr[lt], arr[left]
        return lt, gt

    def __quick_sort(self, arr, left, right):
        if left >= right:
            return
        lt, gt = self.__partition(arr, left, right)
        # 在有很多重复元素的排序任务中，lt 和 gt 可能会相距很远
        # 因此后序递归调用的区间变小
        # 递归的深度也大大降低了
        self.__quick_sort(arr, left, lt - 1)
        self.__quick_sort(arr, gt, right)

    def sort(self, arr):
        size = len(arr)
        self.__quick_sort(arr, 0, size - 1)


if __name__ == '__main__':
    SortingUtil.test_sorting_algorithm(QuickSort())
    SortingUtil.test_sorting_algorithm(QuickSortTwoWays())
    SortingUtil.test_sorting_algorithm(QuickSortThreeWays())
