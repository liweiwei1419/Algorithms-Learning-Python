# 冒泡排序
from sort.sort_helper import swap
from sort.sort_helper import test_your_sort_algorithm


# 8,7,5,4

def bubble_sort_1(nums):
    n = len(nums)
    for i in range(0, n - 1):
        for j in range(0, n - i - 1):  # 注意临界值的选取
            if nums[j] > nums[j + 1]:
                swap(nums, j, j + 1)


def bubble_sort_2(nums):
    n = len(nums)
    for i in range(0, n - 1):
        sorted = True  # 假设数组是排好序的

        for j in range(0, n - i - 1):  # 注意临界值的选取
            if nums[j] > nums[j + 1]:
                swap(nums, j, j + 1)
                sorted = False  # 只要发现有元素交换，就说明假设是错误的
        # 如果一轮下来都没有元素交换，那么接下来的几轮就没有必要进行比较了
        if sorted:
            break


if __name__ == '__main__':
    test_your_sort_algorithm(bubble_sort_1)
    # test_your_sort_algorithm(bubble_sort_2)
