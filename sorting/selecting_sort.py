from sorting.sorting_util import SortingUtil
from sorting.examples import GenerateRandomArrayStrategy


class SelectionSort:

    # 选择排序：每一轮选择最小的元素排在前面

    def __str__(self):
        return "选择排序"

    @SortingUtil.cal_time
    def sort(self, arr):
        size = len(arr)
        for i in range(size - 1):
            min_index = i
            for j in range(i + 1, size):
                if arr[j] < arr[min_index]:
                    min_index = j
            arr[i], arr[min_index] = arr[min_index], arr[i]


if __name__ == '__main__':
    SortingUtil.test_sorting_algorithm(SelectionSort(), GenerateRandomArrayStrategy(5000))
    SortingUtil.test_sorting_algorithm(SelectionSort(), GenerateRandomArrayStrategy(10000))
