from sorting.sorting_util import SortingUtil
from sorting.examples import GenerateRandomArrayStrategy


class BubbleSort:
    def __str__(self):
        return "冒泡排序"

    @SortingUtil.cal_time
    def sort(self, arr):
        size = len(arr)
        for i in range(0, size - 1):
            for j in range(0, size - i - 1):  # 注意临界值的选取
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]


class BubbleSortOptimizer:
    def __str__(self):
        return "冒泡排序（优化）"

    @SortingUtil.cal_time
    def sort(self, arr):
        size = len(arr)
        for i in range(0, size - 1):
            sorted_flag = True  # 假设数组是排好序的
            for j in range(0, size - i - 1):  # 注意临界值的选取
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
                    sorted_flag = False  # 只要发现有元素交换，就说明假设是错误的
            # 如果一轮下来都没有元素交换，那么接下来的几轮就没有必要进行比较了
            if sorted_flag:
                break


if __name__ == '__main__':
    SortingUtil.test_sorting_algorithm(BubbleSort(), GenerateRandomArrayStrategy(3000))
    SortingUtil.test_sorting_algorithm(BubbleSortOptimizer(), GenerateRandomArrayStrategy(3000))

    arr = [1, 2, 3]
    arr.sort()
