from sorting.sorting_util import SortingUtil
from sorting.examples import GenerateRandomArrayStrategy
from sorting.examples import GenerateNearlySortedArrayStrategy

from sorting.selecting_sort import SelectionSort


class InsertionSort:

    def __str__(self):
        return "插入排序"

    @SortingUtil.cal_time
    def sort(self, arr):
        """
        插入排序第 1 版：相比选择排序而言，插入排序的内层循环可以提前终止。
        但是这个版本有个缺点，交换次数太多，每一次交换做了 3 次赋值。
        """
        size = len(arr)
        for i in range(1, size):
            for j in range(i, 0, -1):
                # 只要前面的比后面的“严格”大，就要交换它们的位置
                if arr[j - 1] > arr[j]:
                    arr[j], arr[j - 1] = arr[j - 1], arr[j]
                else:
                    break


class InsertionSortOptimizer:

    def __str__(self):
        return "插入排序（优化）"

    @SortingUtil.cal_time
    def sort(self, arr):
        size = len(arr)
        for i in range(1, size):
            # 每一轮先让这个元素去别的地方休息一下
            temp = arr[i]
            # 从 i 的前一个元素开始看
            j = i
            while j > 0 and arr[j - 1] > temp:
                arr[j] = arr[j - 1]
                j -= 1
            # 因为已经看到索引 j 的值小于等于 temp 了
            # 因此空出来的位置是 j，要把 temp 放在这里
            arr[j] = temp


if __name__ == '__main__':
    # 测试插入排序算法的正确性
    # SortingUtil.test_sorting_algorithm(InsertionSort(), GenerateRandomArrayStrategy(5000))

    # 比较插入排序算法与选择排序
    # SortingUtil.compare_sorting_algorithms(GenerateRandomArrayStrategy(5000),
    #                                        SelectionSort(),
    #                                        InsertionSort())

    # 验证插入排序算法对于几乎有序的数组，越有序越好
    SortingUtil.test_sorting_algorithm(InsertionSortOptimizer(), GenerateRandomArrayStrategy(5000))

    SortingUtil.compare_sorting_algorithms(GenerateRandomArrayStrategy(5000),
                                           SelectionSort(),
                                           InsertionSort(),
                                           InsertionSortOptimizer())

    SortingUtil.compare_sorting_algorithms(GenerateNearlySortedArrayStrategy(5000),
                                           SelectionSort(),
                                           InsertionSort(),
                                           InsertionSortOptimizer())
